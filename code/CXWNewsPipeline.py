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



class CXWNewsCrawler(NewsCrawler):

    def __init__(self, **params):
        NewsCrawler.__init__(self, **params)

    # overwrite to parse list page
    def parse_list_page(self, content):
        content = content[content.index("{"): content.rindex("}")+1]
        json_data = json.loads(content)
        json_data = json_data['datas']
        self.logger.debug("parsing list page %d"%(self.page_num))
        self.logger.debug("there are %d news in list"%(len(json_data)))
        for data in json_data:
            try:
                news_info = {}
                news_info["b_class"] = data["channelDesc"].encode("utf-8")
                news_info["url"] = data["link"]
                news_info["title"] = data["desc"].encode("utf-8")
                news_info["author"] = data["edit"]["name"]
                news_info["pub_date"] = data["time"]
                self.logger.debug("found news %s"%(news_info["title"]))
                yield news_info
            except:
                self.logger.debug("response json format error")
                continue

