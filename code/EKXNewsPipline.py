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
import json
from datetime import datetime


class EKXNewsCrawler(NewsCrawler):

    def __init__(self, **params):
        NewsCrawler.__init__(self, **params)

    # overwrite to generate new list page url
    def generate_next_list_url(self):
        if self.page_num == 0:
            self.page_num += 1
            ret_url = self.list_url_tpl
            self.list_url_tpl += "index_%d.shtml"
            yield ret_url
        ret_url = self.list_url_tpl % (self.page_num)
        self.page_num += 1
        yield ret_url

    # overwrite to parse list page
    def parse_list_page(self, content):

        self.logger.debug("parsing list page %d" % (self.page_num))
        data = json.loads(content)['data']
        for val in data:
            self.logger.debug("match")
            news_info = {}
            news_info["url"] = val['url']
            news_info["title"] = val['title']
            yield news_info


