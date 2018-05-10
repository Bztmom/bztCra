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



class ECNCJNewsCrawler(NewsCrawler):

    def __init__(self, **params):
        NewsCrawler.__init__(self, **params)

    # overwrite to parse list page
    def parse_list_page(self, content):
        json_data = json.loads(content)
        if "data" not in json_data:
            self.logger.warning("not html field in response")
            raise Exception("not required field in response json")
        data = json_data['data'].encode("utf-8")
        list_pattern = re.compile(r'<li class="news"><a href="(?P<url>.*?)" target="_blank" title="(?P<title>.*?)"', re.DOTALL)
        self.logger.debug("parsing list page %d"%(self.page_num))
        for m in list_pattern.finditer(data):
            self.logger.debug("match")
            news_info = {}
            news_info["url"] = m.group("url")
            news_info["title"] = m.group("title")
            self.logger.debug("found news %s"%(news_info["title"]))
            yield news_info

