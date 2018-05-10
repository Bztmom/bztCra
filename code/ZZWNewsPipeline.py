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


class ZZWNewsCrawler(NewsCrawler):

    def __init__(self, **params):
        NewsCrawler.__init__(self, **params)
        self.list_pattern = re.compile(
            "<dl>(.|\n)*?<dt><a href=\"(.*)\">(.*)<\/a><\/dt>(.|\n)*?<span(.|\n)*?>(.*)<\/span>(.|\n)*?<\/dl>")
        self.is_first_page = True
        self.cur_url = ""

    # overwrite to generate new list page url
    def generate_next_list_url(self):
        if self.page_num == 0:
            self.page_num += 1
            ret_url = self.list_url_tpl
            self.list_url_tpl += "index_%d.shtml"
            yield ret_url
        ret_url = self.list_url_tpl % (self.page_num)
        self.page_num += 1
        yield ret_url

    # overwrite to parse list page
    def parse_list_page(self, content):
        self.logger.debug("start zzw parse list page")
        for _, url, title, _, _, pub_date, _ in self.list_pattern.findall(content):
            # if self.last_date is None:
            #     self.last_date = pub_date
            news_info = {}
            news_info["url"] = self.base_url + url
            news_info["title"] = title.decode("gbk")
            news_info["pub_date"] = datetime.strptime(
                pub_date, "%y-%m-%d %H:%M")
            self.logger.debug("found news %s (%s)" % (title, pub_date))
            yield news_info
        self.logger.debug("end zzw parse list page")



class ZZWNewsContentParser(NewsProcessor):

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
                r'<div class=\"artical_c\">((.|\n)*?)<!--')
            news_meta_pattern = re.compile(
                '<span><em>作者：</em>(.*?)</span><span><em>来源：<\/em>(.*?)<\/span>')
            news_date_pattern = re.compile('<span class="Ff">(.*?)<\/span>')
            meta_data = news_meta_pattern.search(page_content)
            auther = ""
            source = ""
            date = ""
            if meta_data:
                # print meta_data.groupdict()
                auther = meta_data.group(1)
                source = meta_data.group(2)
            date_data = news_date_pattern.search(page_content)
            if date_data:
                date = date_data.group(1)
            pure_page = news_page_pattern.search(page_content).group(1)
            for next_page in self.multi_news_page(news_info, page_content):
                next_page = next_page.decode("gbk")
                pure_page += news_page_pattern.search(next_page).group(1)
            self.logger.debug("auther=>" + auther +
                              " source=>" + source + " date=>" + date)
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
