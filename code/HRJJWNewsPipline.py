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


class HRJJWNewsCrawler(NewsCrawler):

    def __init__(self, **params):
        NewsCrawler.__init__(self, **params)

    # overwrite to parse list page
    def parse_list_page(self, content):
        self.logger.debug("parsing list page %d" % (self.page_num))
        data = json.loads(content)['data']['items']
        for val in data:
            if len(val['related_topics']) == 0:
                self.logger.debug("match")
                news_info = {}
                if (val['source_uri']):
                    news_info["url"] = val['source_uri']
                else:
                    news_info["url"] = val['uri']
                news_info["pub_date"] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(val['display_time']))
                news_info["title"] = val['title']
                yield news_info



