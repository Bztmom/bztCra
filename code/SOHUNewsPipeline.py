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



class SOHUNewsCrawler(NewsCrawler):

    def __init__(self, **params):
        NewsCrawler.__init__(self, **params)

    # overwrite to parse list page
    def parse_list_page(self, content):
        content = content[content.index("["): content.rindex("]")+1]
        json_data = json.loads(content)
        #data = json_data['data'].encode("utf-8")
        self.logger.debug("parsing list page %d"%(self.page_num))
        self.logger.debug("there are %d news in list"%(len(json_data)))
        for data in json_data:
            try:
                news_info = {}
                news_info["author"] = data["authorName"].encode("utf-8")
                news_info["url"] = "http://www.sohu.com/a/%d_%d"%(data["id"], data["authorId"])
                news_info["title"] = data["title"].encode("utf-8")
                news_info["pub_date"] =  datetime.fromtimestamp(data["publicTime"] / 1000)
                self.logger.debug("found news %s"%(news_info["title"]))
                yield news_info
            except:
                self.logger.debug("response json format error")
                continue

