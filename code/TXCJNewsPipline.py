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


class TXCJNewsCrawler(NewsCrawler):

    def __init__(self, **params):
        NewsCrawler.__init__(self, **params)

    # overwrite to parse list page
    def parse_list_page(self, content):

        self.logger.debug("parsing list page %d" % (self.page_num))

        encoding = chardet.detect(content)['encoding']
        if encoding is None:
            encoding = self.encoding  # "utf-8"
        if encoding.lower() == "gb2312" or encoding.lower() == "gbk":
            encoding = "gbk"
        if (encoding != "utf-8" and encoding != "gb2312" and encoding != "gbk"):
            encoding = self.encoding
        content = json.loads(content.decode(encoding, "ignore").encode("utf-8"))['data']
        for m in re.compile(r'<a.*?href="(?P<url>.*?)">(?P<title>.*?)<\/a',re.DOTALL).finditer(content['article_info']):
            news_info = {}
            for key, value in m.groupdict().iteritems():
                news_info[key] = value.replace("http://","https://")

            yield news_info


