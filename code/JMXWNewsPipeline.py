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


class JMXWNewsCrawler(NewsCrawler):

    def __init__(self, **params):
        NewsCrawler.__init__(self, **params)

    # overwrite to parse list page
    def parse_list_page(self, content):
        self.logger.debug("parsing list page %d" % (self.page_num))
        list_patterns = re.compile(r'jQuery\((?P<date>.*)\)', re.DOTALL)
        data = json.loads(list_patterns.search(content).group(1))
        for m in re.compile(r'<a href="(?P<url>.*?)".*?>(?P<title>.*?)<\/a',re.DOTALL).finditer(data["rst"]):
            self.logger.debug("match")
            news_info = {}
            for key, value in m.groupdict().iteritems():
                news_info[key] = value
            yield news_info


