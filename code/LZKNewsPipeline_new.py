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


class LZKNewsCrawler(NewsCrawler):

    def __init__(self, **params):
        NewsCrawler.__init__(self, **params)
        self.list_pattern = re.compile(
            "title=\"(.*?)\" href=\"(.*?)\">(.|\n)*?created\">(.|\n)*?content\">(.*?)<\/span>")
        self.is_first_page = True
        self.cur_url = ""

    # overwrite to generate new list page url
    def generate_next_list_url(self):
        if self.page_num == 0:
            # self.page_num += 1
            ret_url = self.list_url_tpl
            self.list_url_tpl += "&page_id=%d"
            yield ret_url
        ret_url = self.list_url_tpl % (self.page_num)
        # self.page_num += 1
        yield ret_url

    # overwrite to parse list page
    def parse_list_page(self, content):
        self.logger.debug("start zzw parse list page")
        for title,  url,  _,  _,  pub_date in self.list_pattern.findall(content):
            # if self.last_date is None:
            #     self.last_date = pub_date
            news_info = {}
            news_info["url"] = url
            news_info["title"] = title
            news_info["pub_date"] = datetime.strptime(
                pub_date, "%Y-%m-%d %H:%M:%S")
            self.logger.debug("found news %s (%s)" % (title, pub_date))
            yield news_info
        self.logger.debug("end zzw parse list page")



class LZKNewsContentParser(NewsProcessor):

    def __init__(self, logger=None):
        NewsProcessor.__init__(self, logger)
        pass

    # check if there are multi page in news

    def process(self, news_info):
        '''parse news page
           auther and source pattern:<span><em>(.*?)：<\/em>(.*?)<\/span>
           date pattern : <span class="Ff">(.*?)<\/span>
           content pattern :<div class="artical_c">(.|\n)*?<!-- 附件列表 -->
           page count pattern：var currentPage = (\d+)(.|\n)*?var countPage = (\d+)
        '''
        try:
            page_content = news_info["content"]
            news_pattern = re.compile(
                'encoded\">((.|\n)*?)<\/div>')
            news_data = news_pattern.search(page_content)
            auther = ""
            source = ""
            date = ""
            pure_page = ""
            if news_data:
                self.logger.debug("matched")
                pure_page = news_data.group(1)
            self.logger.debug("auther=>" + auther +
                              " source=>" + source + " date=>" + date+" content=>" + pure_page)
            news_info["author"] = auther
            news_info["source"] = source
            news_info["inner_page_date"] = date
            news_info["content"] = pure_page
        except Exception as e:
            raise NewsProcessor.ProcessorException(
                "Fail to parse url: %s: "%(news_info["url"]) + e.message)
            return None
