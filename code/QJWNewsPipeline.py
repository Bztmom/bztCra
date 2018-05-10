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
from datetime import datetime



####we言堂
class QJW_WYTNewsCrawler(NewsCrawler):

    def __init__(self, **params):
        NewsCrawler.__init__(self, **params)
        self.list_pattern = re.compile(
            r'<div class="toux">.*?<i>(?P<author>.*?)<\/i>.*?<h2 class="bshare-title">.*?<a href="(?P<url>.*?)".*?>(?P<title>.*?)<\/a>.*?<span class="newsdetail_left">.*?<i>(?P<pub_date>.*?)<\/i>', re.DOTALL)

        self.headers = {
            "Referer":"http://weyt.p5w.net/",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest",
            "Host":"weyt.p5w.net"
        }
    # overwrite to generate new list page url
    # def generate_next_list_url(self):
    #     #url_tpl:http://weyt.p5w.net/ajaxGetArticleList?page=%d&search=&size=10
    #     def _gen(self):
    #         self.page_num += 1
    #         ret_url = self.list_url_tpl % (self.page_num)
    #         return ret_url
    #     return _gen

    # overwrite to parse list page
    def parse_list_page(self, content):
        self.logger.debug("parsing list page %d"%(self.page_num))
        encoding = chardet.detect(content)['encoding']
        if encoding.lower() == "gb2312":
            encoding="gbk"
        content = content.decode(encoding).encode("utf-8")
        json_obj = json.loads(content)
        if "html" not in json_obj:
            self.logger.warning("not html field in response")
        content = json_obj["html"]#.decode("string_escape")
        #print self.list_pattern.findall(content)[0]
        #print >> sys.stderr ,content
        for author, url, title, pub_date in self.list_pattern.findall(content):
            # if self.last_date is None:
            #     self.last_date = pub_date
            news_info = {}
            news_info["author"] = author
            news_info["url"] = url
            news_info["title"] = title
            news_info["pub_date"] = datetime.strptime(
                pub_date, "%Y-%m-%d %H:%M:%S")
            #print >> sys.stderr, author, url, title
            self.logger.debug("found news %s (%s)" % (title, pub_date))
            yield news_info



class QJW_WYTNewsContentParser(NewsProcessor):

    def __init__(self, logger=None):
        NewsProcessor.__init__(self, logger)
        pass

    # check if there are multi page in news
    def multi_news_page(self, news_info, content):
        '''check if there are multi page in news
        if yes, yield next url, otherwise nothing
        '''
        page_info_pattern = re.compile(
            'var currentPage = (\d+)(.|\n)*?var countPage = (\d+)')
        page_info_data = page_info_pattern.search(content)
        if page_info_data:
            # print page_info_data.group(1)
            page_count = int(page_info_data.group(3))
            self.logger.debug(
                "there are %d pages for this news" % (page_count))
            cur_url = news_info["url"]
            for page_num in xrange(1, page_count):
                # next page url is t2017-10-09_32432432.html =>t2017-10-09_32432432_1.html
                page_content = get(cur_url[:-5] + "_%d" %
                                   (page_num) + cur_url[-5:])
                if page_content is not None:
                    yield page_content

    def process(self, news_info):
        '''parse news page
           auther and source pattern:<span><em>(.*?)：<\/em>(.*?)<\/span>
           date pattern : <span class="Ff">(.*?)<\/span>
           content pattern :<div class="artical_c">(.|\n)*?<!-- 附件列表 -->
           page count pattern：var currentPage = (\d+)(.|\n)*?var countPage = (\d+)
        '''
        try:
            page_content = news_info["content"]
            news_page_pattern = re.compile(
                r'<div class="article_content">(?P<content>.*?)<div class="copyright">',re.DOTALL)
            pure_page_data = news_page_pattern.search(page_content)
            if pure_page_data:
                pure_page = pure_page_data.group("content")
            else:
                raise Exception("not found content")
            return pure_page
        except Exception as e:
            raise NewsProcessor.ProcessorException(
                "Fail to parse url: %s: "%(news_info["url"]) + e.message)
            return None


###
##舆情部分
#http://www.p5w.net/yuqing/kuaixun/
####we言堂
class QJW_YQNewsCrawler(NewsCrawler):

    def __init__(self, **params):
        NewsCrawler.__init__(self, **params)
        self.list_pattern = re.compile(
            r'<h2 class="title"><a href="(?P<url>.*?)".*?>(?P<title>.*?)<\/a>.*?<span class="time">(?P<pub_date>.*?)<\/span>', re.DOTALL)
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        }


    # overwrite to parse list page
    def parse_list_page(self, content):
        #print self.list_pattern.findall(content)[0]
        for url, title, pub_date in self.list_pattern.findall(content):
            # if self.last_date is None:
            #     self.last_date = pub_date
            try:
                news_info = {}
                news_info["url"] = self.base_url+url
                news_info["title"] = title.decode("gbk")
                news_info["pub_date"] = datetime.strptime(
                    pub_date.decode("gbk").encode("utf-8"), "%m月%d日 %H:%M")
                news_info["pub_date"] = news_info["pub_date"].replace(year = datetime.now().year)
                self.logger.debug("found news %s (%s)" % (title, pub_date))
                yield news_info
            except Exception as e:
                import traceback
                traceback.print_exc()
                print url, title, pub_date
                print e.message
                continue
