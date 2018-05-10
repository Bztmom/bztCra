# -*- coding: utf-8 -*-

############################################
##
# defination of new crawler framework
##
##
#############################################


import re
from XX_Crawler.XXNewsETL import *
from XX_Crawler.Utils import *
import logging
import time


class XHCJNewsCrawler(NewsCrawler):

    def __init__(self, **params):
        NewsCrawler.__init__(self, **params)
        self.list_pattern = re.compile(
            "<dl>(.|\n)*?<dt><a href=\"(.*?)\">(.*?)<\/a><\/dt>(.|\n)*?<span(.|\n)*?>(.*?)<\/span>(.|\n)*?<\/dl>")
        self.is_first_page = True
        self.cur_url = ""

    # overwrite to generate new list page url
    def generate_next_list_url(self):
        if self.page_num==0:
            self.page_num+=1
            self.list_url_tpl+='%d'
        ret_url = self.list_url_tpl % (self.page_num)
        yield ret_url

    # overwrite to parse list page
    def parse_list_page(self, content):
        self.logger.debug("start zzw parse list page")
        json_part_pattern = re.compile("\(((.|\n)*)\)")
        matched = json_part_pattern.search(content)
        if matched:
            self.logger.debug("found:"+matched.group(1))
            json_obj = json.loads(matched.group(1))
            if json_obj["status"] == 0:
                news_list = json_obj["data"]["list"]
                self.logger.debug("found %d news in page %d"%(len(news_list), self.page_num))
                for news_info in news_list:
                    news_info["pub_date"] = datetime.strptime(news_info["PubTime"],"%Y-%m-%d %H:%M:%S")
                    if news_info["LinkUrl"] is not None and news_info["LinkUrl"].startswith("http"):
                        news_info["title"] = news_info["Title"]
                        news_info["url"] = news_info["LinkUrl"]
                        news_info["author"] = news_info["Author"]
                        news_info["source"] = news_info["SourceName"]
                    else :continue
                    logging.debug("found news %s=> %s"%(news_info["title"], news_info["url"]))
                    yield news_info


class XHCJNewsContentParser(NewsProcessor):

    def __init__(self, logger=None):
        NewsProcessor.__init__(self, logger)
        pass

    def process(self, news_info):
        '''parse news page
           auther and source pattern:<span><em>(.*?)：<\/em>(.*?)<\/span>
           date pattern : <span class="Ff">(.*?)<\/span>
           content pattern :<div class="artical_c">(.|\n)*?<!-- 附件列表 -->
           page count pattern：var currentPage = (\d+)(.|\n)*?var countPage = (\d+)
        '''
        try:
            page_content = news_info["content"]
            page_content_pattern = re.compile("作者：((.|\n)*?)<\/span>(.|\n)*?important\">(.|n)*?<\/div>((.|\n)*?)<!--")
            other_page_content_pattern = re.compile("time\">(.*?)<\/span>(.|\n)*?来源：((.|\n)*?)<\/span>(.|\n)*?<\/div>(.|\n)*?(<p(.|\n)*?)<div(.|\n)*?编辑：((.|\n)*?)<")
            date_str = ""
            author = ""
            pure_page = ""
            content_data = page_content_pattern.search(page_content)
            other_content_data = other_page_content_pattern.search(page_content)
            if content_data:
                pure_page = content_data.group(5)
                news_info["author"] = content_data.group(1)
                news_info["content"] = pure_page
            elif other_content_data:
                pure_page = other_content_data.group(7)
                news_info["author"] = other_content_data.group(10)
                news_info["source"] = other_content_data.group(3)
                news_info["inner_page_date"] = other_content_data.group(1)
                news_info["content"] = pure_page
        except Exception as e:
            raise NewsProcessor.ProcessorException(
                "Fail to parse url: %s: "%(news_info["url"]) + e.message)
            return None
