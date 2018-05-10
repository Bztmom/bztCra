# -*- coding: utf-8 -*-

############################################
##
# defination of new crawler framework
##
##
#############################################


import re
import sys
from XX_Crawler.XXNewsETL import *
from XX_Crawler.Utils import *
import logging
import time
import json
from datetime import datetime


class WYWNewsCrawler(NewsCrawler):

    def __init__(self, **params):
        NewsCrawler.__init__(self, **params)

    # overwrite to parse list page
    def parse_list_page(self, content):

        pattern_conf = [
            r'category-post-node".*?href="(?P<url>.*?)".*?h2.*?>(?P<title>.*?)<\/h2'
        ]
        list_patterns = [re.compile(list_pattern, re.DOTALL) for list_pattern in pattern_conf]
        encoding = "utf-8"
        self.logger.debug("parsing list page %d" % (self.page_num))
        news_info = []
        for list_pattern in list_patterns:
            for m in list_pattern.finditer(content.decode(encoding, "ignore").encode("utf-8")):
                self.logger.debug("match")
                news_info = {}
                news_info["url"] = m.group("url")
                news_info["title"] = m.group("title")
                news_info["pub_date"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                self.logger.debug("found news %s" % (news_info["title"]))
                yield news_info
