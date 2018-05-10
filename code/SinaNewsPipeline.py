# -*- coding: utf-8 -*-

'''crawl sina
'''


import re
from XX_Crawler.XXNewsETL import *
from XX_Crawler.Utils import *
import logging
import json
import time
from datetime import datetime


class SinaNewsCrawler(NewsCrawler):

    def __init__(self, **params):
        NewsCrawler.__init__(self, **params)
        self.list_pattern = re.compile("<dl>(.|\n)*?<dt><a href=\"(.*)\">(.*)<\/a><\/dt>(.|\n)*?<span(.|\n)*?>(.*)<\/span>(.|\n)*?<\/dl>")
        self.cur_news_list = []

    ##overwrite to parse list page
    def parse_list_page(self, content):
        for news_info in NewsCrawler.parse_list_page(self, content):
            if news_info["url"] not in self.cur_news_list:
                self.cur_news_list.append(news_info["url"])
                yield news_info
