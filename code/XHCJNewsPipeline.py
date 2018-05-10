# -*- coding: utf-8 -*-

'''crawl forture(xinhuacaijing)
'''


import re
from XX_Crawler.XXNewsETL import *
from XX_Crawler.Utils import *
import logging
import json
import time
from datetime import datetime


class XHCJNewsCrawler(NewsCrawler):

    def __init__(self, list_url_tpl, data_path, website_name, b_class, checkpoint_filename, logger,checkpoint_saved_days):
        NewsCrawler.__init__(self, list_url_tpl, data_path, website_name,
                             b_class, logger=logger, checkpoint_filename=checkpoint_filename, checkpoint_saved_days=checkpoint_saved_days)
        self.list_pattern = re.compile("<dl>(.|\n)*?<dt><a href=\"(.*)\">(.*)<\/a><\/dt>(.|\n)*?<span(.|\n)*?>(.*)<\/span>(.|\n)*?<\/dl>")
        self.base_url = list_url_tpl #"http://www.cs.com.cn/gppd/"
        self.is_first_page = True
        self.cur_url = ""
        self.b_class = b_class
        self.logger = logger

    ##overwrite to generate news page filename
    def generate_news_filename(self, news_info):
        #filename = self.data_path + news_info["title"] + ".news"
        class_name = self.base_url.split("/")[-2]
        date_no = news_info["url"].split("/")[-1].split(".")[0]
        filename = "%s/%s_%s.news" % (self.data_path, class_name, date_no)
        logging.debug("generate news filename "+ filename)
        return filename

    ##overwrite to generate list page filename
    def generate_list_filename(self):
        filename = self.data_path + self.website_name+"_"+self.b_class+"_"+str(int(time.time()))+".list"
        logging.debug("generate list filename "+ filename)
        return filename

    ##overwrite to generate new list page url
    def generate_next_list_url(self):
        if self.page_num == 0:
            self.page_num += 1
            self.base_url = self.list_url_tpl
            ret_url = self.list_url_tpl % (self.page_num)
            self.list_url_tpl = self.base_url
            return ret_url
        self.page_num += 1
        ret_url = self.list_url_tpl % (self.page_num)
        return ret_url

    ##overwrite to parse list page
    def parse_list_page(self, content):
        content = content.decode("utf-8")
        self.logger.debug(content)
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
                #break


class XHCJNewsContentParser(NewsProcessor):

    def __init__(self, logger=None):
        NewsProcessor.__init__(self, logger)
        pass

    def process(self, news_info, doc):
        try:
            page_content = doc.decode("utf-8")
            page_content_pattern = re.compile(u"作者：((.|\n)*?)<\/span>(.|\n)*?important\">(.|n)*?<\/div>((.|\n)*?)<!--")
            other_page_content_pattern = re.compile(u"time\">(.*?)<\/span>(.|\n)*?来源：((.|\n)*?)<\/span>(.|\n)*?<\/div>(.|\n)*?(<p(.|\n)*?)<div(.|\n)*?编辑：((.|\n)*?)<")
            date_str = ""
            author = ""
            pure_page = ""
            content_data = page_content_pattern.search(page_content)
            other_content_data = other_page_content_pattern.search(page_content)
            if content_data:
                pure_page = content_data.group(5)
                news_info["author"] = content_data.group(1)
                return pure_page
            elif other_content_data:
                pure_page = other_content_data.group(7)
                news_info["author"] = other_content_data.group(10)
                news_info["source"] = other_content_data.group(3)
                news_info["inner_page_date"] = other_content_data.group(1)
                return pure_page
            else:
                raise Exception("exists pattern not matched")
        except Exception as e:
            import traceback
            traceback.print_exc()
            raise NewsProcessor.ProcessorException(
                "Fail to parse url: %s: "%(news_info["url"]) + e.message)
        return None
