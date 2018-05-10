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


class HQCJNewsCrawler(NewsCrawler):

    def __init__(self, **params):
        NewsCrawler.__init__(self, **params)
        self.list_pattern = re.compile(
            "<l.*?><a href=\"(.*?)\">((.|\n)*?)<\/a><\/li>")
        self.is_first_page = True
        self.cur_url = ""

    # overwrite to generate new list page url
    def generate_next_list_url(self):
        if self.page_num == 0:
            self.page_num += 1
            self.base_url = self.list_url_tpl
            ret_url = self.list_url_tpl
            self.list_url_tpl += "%d.html"
            yield ret_url
        ret_url = self.list_url_tpl % (self.page_num)
        # self.page_num += 1
        yield ret_url

    # overwrite to parse list page
    def parse_list_page(self, content):
        self.logger.debug("start zzw parse list page")
        for url,title,_, in self.list_pattern.findall(content):
            # if self.last_date is None:
            #     self.last_date = pub_date
            news_info = {}
            if "http" in url:
                news_info["url"] =url
            else:
                news_info["url"] =self.base_url+url
            news_info["title"] = title.decode("utf-8")
            # news_info["pub_date"] = ""
            # news_info["pub_date"] = datetime.strptime(
            #     pub_date, "%Y-%m-%d %H:%M")
            # self.logger.debug("found news %s (%s)" % (title, pub_date))
            yield news_info
        self.logger.debug("end zzw parse list page")



class   HQCJNewsContentParser(NewsProcessor):

    def __init__(self, logger=None):
        NewsProcessor.__init__(self, logger)
        pass

    # check if there are multi page in news
    def multi_news_page(self, news_info, content):
        '''check if there are multi page in news
        if yes, yield next url, otherwise nothing
        '''
        page_info_pattern = re.compile(
            '<div id=\"pages\"(.|\n)*?<a href(.*)\">(.*?)<\/a> <a class=\"a1\"')
        page_info_data = page_info_pattern.search(content)
        page_info_pattern1 = re.compile(
            '<div id=\"pages\"(.|\n)*?<a href(.*)\">(.*?)<span>(.*?)<\/span> <a class=\"a1\"')
        page_info_data1 = page_info_pattern1.search(content)
        if page_info_data:
            # print page_info_data.group(1)
            page_count = int(page_info_data.group(3))
            self.logger.debug(
                "there are %d pages for this news" % (page_count))
            cur_url = news_info["url"]
            for page_num in xrange(2, page_count):
                # next page url is t2017-10-09_32432432.html =>t2017-10-09_32432432_2.html
                page_content = get(cur_url[:-5] + "_%d" %
                                   (page_num) + cur_url[-5:])
                if page_content is not None:
                    yield page_content
        elif page_info_data1:
            page_count = int(page_info_data1.group(4))
            self.logger.debug(
                "there are %d pages for this news" % (page_count))
            cur_url = news_info["url"]
            for page_num in xrange(2, page_count):
                # next page url is t2017-10-09_32432432.html =>t2017-10-09_32432432_2.html
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
                '<div class=\"text\" id=\"text\">((.|\n)*?)<!-- 翻页按钮 begin')#内容
            pure_page = news_page_pattern.search(page_content)
            news_page_otherpattern = re.compile(
                '<div class=\"text\" id=\"text\">((.|\n)*?)<div class=\"editorSign')#内容
            pure_otherpage = news_page_otherpattern.search(page_content)
            news_page_otherpattern1 = re.compile(
                '<div class=\"text\" id=\"text\">((.|\n)*?)<!--相关新闻上方合作 begain')#内容
            pure_otherpage1 = news_page_otherpattern1.search(page_content)
            news_page_otherpattern2 = re.compile(
                '<div class=\"summary\">((.|\n)*?)<div class=\"summary infoArea\">')#内容
            pure_otherpage2 = news_page_otherpattern2.search(page_content)
            news_meta_pattern = re.compile(
                '<div class=\"summaryNew\">(.|\n)*?pubtime_baidu\">(.*?)<\/strong>(.|\n)*?source_baidu\">(<a.*?>)?(来源：)?(<a.*?>)?(.*?)(<\/a>)?(<\/span>)?<\/strong>')#时间+来源
            meta_data = news_meta_pattern.search(page_content)
            news_meta_pattern1 = re.compile(
                '<div class=\"summary\">(.|\n)*?strong>(.*?)<\/strong>(.|\n)*?<strong>(<a.*?>)?(.*?)(<\/a>)?<\/strong>')#时间+来源
            meta_data1 = news_meta_pattern1.search(page_content)
            news_meta_pattern2 = re.compile(
                '<div class=\"summaryNew\">(.|\n)*?strong>(.*?)<\/strong>(.|\n)*?strong>(<span.*?>)?(来源：)?(<a.*?>)?(<a.*?>)?(.*?)(<\/a>)?(<\/a>)?(<\/span>)?<\/strong>')#时间+来源
            meta_data2 = news_meta_pattern2.search(page_content)
            news_author_pattern = re.compile(
                'editor_baidu\">责任编辑：(.*?)<\/span>')#作者
            author_data = news_author_pattern.search(page_content)
            news_author_pattern1 = re.compile(
                'editorSign\">责任编辑：(.*?)<\/p>')#作者
            author_data1 = news_author_pattern1.search(page_content)
            news_author_pattern2 = re.compile(
                'editor\">责任编辑：(.*?)<\/span>')#作者
            author_data2 = news_author_pattern2.search(page_content)
            news_author_pattern3 = re.compile(
                'author_baidu\"(.|\n)*?>责任编辑：((.|\n)*?)<\/span>')#作者
            author_data3 = news_author_pattern3.search(page_content)
            news_author_pattern4= re.compile(
                'editor_baidu\".*?\">责任编辑：(.*?)<\/span>')#作者
            author_data4 = news_author_pattern4.search(page_content)
            news_author_pattern5= re.compile(
                '<\/a><\/strong>(.|\n)*?<strong>责任编辑：(.*?)<\/strong>(.|\n)*?<em')#作者
            author_data5 = news_author_pattern5.search(page_content)
            news_author_pattern6= re.compile(
                'editor_baidu\">(<span>)?责编：(.*?)<\/span>')#作者
            author_data6 = news_author_pattern6.search(page_content)
            author = ""
            source = ""
            date = ""
            content=""
            if meta_data:
                source = meta_data.group(7)
                date = meta_data.group(2)
            elif meta_data1:
                source = meta_data1.group(5)
                date = meta_data1.group(2)
            elif meta_data2:
                source = meta_data2.group(8)
                date = meta_data2.group(2)
            else:
                source=source
                date=date
            if author_data:
                author=author_data.group(1)
            elif author_data1:
                author=author_data1.group(1)
            elif author_data2:
                author=author_data2.group(1)
            elif author_data3:
                author=author_data3.group(2)
            elif author_data4:
                author=author_data4.group(1)
            elif author_data5:
                # if u"字号" in author_data5.group(2)
                #     author=""
                # else :
                author=author_data5.group(2)
            elif author_data6:
                author=author_data6.group(2)
            else:
                author=author
            if pure_page:
                content=pure_page.group(1)
                for next_page in self.multi_news_page(news_info, page_content):
                #     # next_page = next_page.decode("utf-8")
                #     # next_page = next_page.decode(charset)
                    content += news_page_pattern.search(next_page).group(1)
            elif pure_otherpage:
                content=pure_otherpage.group(1)
                for next_page in self.multi_news_page(news_info, page_content):
                #     # next_page = next_page.decode("utf-8")
                #     # next_page = next_page.decode(charset)
                    content += news_page_otherpattern.search(next_page).group(1)
            elif pure_otherpage1:
                content=pure_otherpage1.group(1)
                for next_page in self.multi_news_page(news_info, page_content):
                #     # next_page = next_page.decode("utf-8")
                #     # next_page = next_page.decode(charset)
                    content += news_page_otherpattern1.search(next_page).group(1)
            elif pure_otherpage2:
                content=pure_otherpage2.group(1)
                for next_page in self.multi_news_page(news_info, page_content):
                #     # next_page = next_page.decode("utf-8")
                #     # next_page = next_page.decode(charset)
                    content += news_page_otherpattern2.search(next_page).group(1)
            # self.logger.debug("auther=>" + auther +
            #                   " source=>" + source + " date=>" + date)
            else:
                content=content
            news_info["author"] = author
            news_info["source"] = source
            news_info["inner_page_date"] = date
            news_info["content"] = content
        except Exception as e:
            raise NewsProcessor.ProcessorException(
                "Fail to parse url: %s: "%(news_info["url"]) + e.message)
            return None
