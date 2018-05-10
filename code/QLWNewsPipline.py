# -*- coding: utf-8 -*-

import re
import sys
from XX_Crawler.XXNewsETL import *
from XX_Crawler.Utils import *
import logging
import time
from datetime import datetime

class QLWNewsCrawler(NewsCrawler):

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
        content = content.decode(encoding, "ignore").encode("utf-8")
        content = re.compile(r'<ul class="list6">(.*?)<\/ul>',re.DOTALL).findall(content)
        for m in re.compile(r'<li><a href="(?P<url>.*?)".*?>(?P<title>.*?)<\/',re.DOTALL).finditer(content[0]):
            self.logger.debug("match")
            news_info = {}
            for key, value in m.groupdict().iteritems():
                news_info[key] = value
            yield news_info

