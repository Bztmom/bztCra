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


class HZKNewsCrawler(NewsCrawler):

    def __init__(self, **params):
        NewsCrawler.__init__(self, **params)
        self.list_pattern = re.compile(
            "<li ><a href=\"(ht(.*?)ml)\".*?>(.*?)<\/a><span>(20(.*?))<\/span><\/li>")
        self.is_first_page = True
        self.cur_url = ""

    # overwrite to generate new list page url
    def generate_next_list_url(self):
        if self.page_num == 0:
            # self.page_num += 1
            ret_url = self.list_url_tpl
            self.list_url_tpl += "&page_id=%d"
            yield ret_url
        ret_url = self.list_url_tpl % (self.page_num)
        # self.page_num += 1
        yield ret_url

    # overwrite to parse list page
    def parse_list_page(self, content):
        self.logger.debug("start zzw parse list page")
        for url,_, title, pub_date, _,in self.list_pattern.findall(content):
            # if self.last_date is None:
            #     self.last_date = pub_date
            news_info = {}
            news_info["url"] = url
            news_info["title"] = title
            news_info["pub_date"] = datetime.strptime(
                pub_date, "%Y-%m-%d %H:%M")
            self.logger.debug("found news %s (%s)" % (title, pub_date))
            yield news_info
        self.logger.debug("end zzw parse list page")



class HZKNewsContentParser(NewsProcessor):

    def __init__(self, logger=None):
        NewsProcessor.__init__(self, logger)
        pass

    # check if there are multi page in news

    def process(self, news_info):
        '''parse news page
           auther and source pattern:<span><em>(.*?)：<\/em>(.*?)<\/span>
           date pattern : <span class="Ff">(.*?)<\/span>
           content pattern :<div class="artical_c">(.|\n)*?<!-- 附件列表 -->
           page count pattern：var currentPage = (\d+)(.|\n)*?var countPage = (\d+)
        '''
        try:
            page_content = news_info["content"]
            news_pattern = re.compile(
                '<div class="article">(.|\n)*?<h1>(.*?)<\/h1>(.|\n)*?<h2><span>(.*?)<\/span><span>来源：(.*?)<\/span><span><\/span><\/h2>(.|\n)*?<p>(.*?)<\/p>(.|\n)*?<p(.|\n)*?责编:(.*?)\]<\/p>')
            news_data = news_pattern.search(page_content)
            news_pattern1 = re.compile(
                '来源：((.|\n)*?)<!--(.|\n)*?<div class="newsc_dcontent">((.|\n)*?)<div class="newsc_dyema">(.|\n)*?责任编辑：(.*?)(\])? <\/div>')
            news_data1 = news_pattern1.search(page_content)
            news_pattern2 = re.compile(
                '<div class="article">(.|\n)*?<h1>(.*)<\/h1>(.|\n)*?<h2><span>(.*)<\/span><span>(来源：)?(.*)<\/span><span>(作者：)?(.*?)<\/span><\/h2>(.|\n)*?<p>((.|\n)*?)<p class="sp">')
            news_data2 = news_pattern2.search(page_content)
            news_pattern3 = re.compile(
                '<div class="newsc_dcontent">((.|\n)*?)<div class="newsc_dyema">(.|\n)*?责任编辑：(.*?)(\])? <\/div>')
            news_data3 = news_pattern3.search(page_content)
            news_pattern4 = re.compile(
                '<div id="news_aritcal".*?">(.|\n)*?<P>((.|\n)*?)<\/P>')
            news_data4 = news_pattern4.search(page_content)
            auther = ""
            source = ""
            date = ""
            pure_page = ""
            if news_data:
                self.logger.debug("matched")
                # print meta_data.groupdict()
                auther = news_data.group(10)
                source = news_data.group(5)
                date = news_data.group(4)
                pure_page = news_data.group(7)
            elif news_data1:
                self.logger.debug("matched 1")
                # print meta_data.groupdict()
                auther = news_data1.group(7)
                source = news_data1.group(1)
                pure_page = news_data1.group(4)
            elif news_data2:
                self.logger.debug("matched 2")
                # print meta_data.groupdict()
                auther = news_data2.group(8)
                source = news_data2.group(6)
                pure_page = news_data2.group(10) 
            elif news_data3:
                self.logger.debug("matched 1")
                # print meta_data.groupdict()
                auther = news_data3.group(4)
                pure_page = news_data3.group(1)
            elif news_data4:
                self.logger.debug("matched 1")
                # print meta_data.groupdict()
                pure_page = news_data4.group(2)   
            news_info["author"] = auther
            news_info["source"] = source
            news_info["inner_page_date"] = date
            #news_info["website_name"] = self.website_name
            #news_info["b_class"] = self.b_class
            news_info["content"] = pure_page
        except Exception as e:
            raise NewsProcessor.ProcessorException(
                "Fail to parse url: %s: "%(news_info["url"]) + e.message)
            return None
