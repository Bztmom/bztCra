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


class ZQWNewsCrawler(NewsCrawler):

    def __init__(self, **params):
        NewsCrawler.__init__(self, **params)
        self.list_pattern = re.compile(
            "<li><font>(.*?)<\/font><a href=\"(.*?)\">(.*?)<\/a><\/li>")
        self.is_first_page = True
        self.cur_url = ""

    # overwrite to generate new list page url
    def generate_next_list_url(self):
        if self.page_num == 0:
            # self.page_num += 1
            self.base_url = self.list_url_tpl
            ret_url = self.list_url_tpl
            self.list_url_tpl += "index_%d.htm"
            yield ret_url
        ret_url = self.list_url_tpl % (self.page_num)
        # self.page_num += 1
        yield ret_url

    # overwrite to parse list page
    def parse_list_page(self, content):
        self.logger.debug("start zzw parse list page")
        for pub_date,url,title, in self.list_pattern.findall(content):
            # if self.last_date is None:
            #     self.last_date = pub_date
            news_info = {}
            self.logger.debug("url:"+url)
            if "http" in url:
                news_info["url"] =url
            else:
                news_info["url"] =self.base_url+url
            news_info["title"] = title.decode("gbk")
            news_info["pub_date"] = datetime.strptime(pub_date,"%Y-%m-%d %H:%M:%S")
            self.logger.debug("found news %s (%s)" % (title, pub_date))
            yield news_info
        self.logger.debug("end zzw parse list page")



class ZQWNewsContentParser(NewsProcessor):

    def __init__(self, logger=None):
        NewsProcessor.__init__(self, logger)
        pass

    # check if there are multi page in news
    def multi_news_page(self, news_info, content):
        '''check if there are multi page in news
        if yes, yield next url, otherwise nothing
        '''
        page_info_pattern = re.compile('var currentPage = (\d+)(.|\n)*?var countPage = (\d+)')
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
            news_pattern = re.compile(
                '<div class=\"l_tit\">(.*?)<\/div>(.|\n)*?pubtime_baidu\">(.*?)<\/span>(.|\n)*?source_baidu\">(.|\n)*?来源：((.|\n)*?)view_num\"><\/span>(.|\n)*?container>((.|\n)*?)<\/div>(.|\n)*?editor_baidu\">责任编辑：(.*?)<\/span')
            news_data = news_pattern.search(page_content)
            news_otherpattern = re.compile(
                '<h1>(.*?)<\/h1>(.|\n)*?date\">(.*?)<\/span>(.|\n)*?soure1\">((.|\n)*?)<\/span>(.|\n)*?content\">((.|\n)*?)<\/div>(.|\n)*?editor\">责任编辑：(.*?)<\/')
            news_otherdata = news_otherpattern.search(page_content)
            news_anotherpattern = re.compile(
                'articleText\">((.|\n)*?)<\/div>(.|\n)*?editor_baidu\">(.*?)<\/span>(.|\n)*?source_baidu\">((.|\n)*?)<\/span>(.|\n)*?pubtime_baidu\">(.*?)<\/span>')
            news_anotherdata = news_anotherpattern.search(page_content)
            news_anotherpattern1 = re.compile(
                'pubtime_baidu\">(.*?)<\/span>(.|\n)*?source_baidu\">((.|\n)*?)<\/div>(.|\n)*?article\">((.|\n)*?)<\/div>(.|\n)*?editor_baidu\">责任编辑：(.*?)<\/span>')
            news_anotherdata1 = news_anotherpattern1.search(page_content)
            author = ""
            source = ""
            date = ""
            content=""
            if news_data:
                author = news_data.group(12)
                source = news_data.group(6).strip()
                if 'HREF' in source and 'href' in source:
                    source_pattern=re.compile('\"_BLANK\">((.|\n)*?)<\/A>(.|\n)*?\">(.*?)<\/a>')
                    source_data=source_pattern.search(source)
                    source=source_data.group(1).strip()+" "+source_data.group(4).strip()
                elif 'HREF' not in source and 'href' in source:
                    source=source
                    source_otherpattern=re.compile('((.|\n)*?)<\/span>(.|\n)*?\">(.*?)<\/a>')
                    source_otherdata=source_otherpattern.search(source)
                    source=source_otherdata.group(1).strip()+" "+source_otherdata.group(4).strip()
                elif 'HREF' in source and 'href' not in source:
                    source=source
                    source_other1pattern=re.compile('(.|\n)*?BLANK\">((.|\n)*?)<\/A>')
                    source_other1data=source_other1pattern.search(source)
                    source=source_other1data.group(2).strip()
                else:
                    source=news_data.group(5).strip()
                date = news_data.group(3)[5:]
                content =news_data.group(9)
                for next_page in self.multi_news_page(news_info, page_content):
                    content += news_data.search(next_page).group(8)
            elif news_anotherdata:
                author = news_anotherdata.group(4)
                source = news_anotherdata.group(6).strip()
                if 'HREF' in source and 'href' in source:
                    source_pattern2=re.compile('\"_BLANK\">((.|\n)*?)<\/A>(.|\n)*?\">(.*?)<\/a>')
                    source_data2=source_pattern2.search(source)
                    source=source_data2.group(1).strip()+" "+source_data2.group(4).strip()
                elif 'HREF' not in source and 'href' in source:
                    source=source[3:]
                    source_otherpattern3=re.compile('((.|\n)*?)<\/span>(.|\n)*?\">(.*?)<\/a>')
                    source_otherdata3=source_otherpattern3.search(source)
                    source=source_otherdata3.group(1).strip()+" "+source_otherdata3.group(4).strip()
                elif 'HREF' in source and 'href' not in source:
                    source=source[3:]
                    source_other2pattern3=re.compile('(.|\n)*?BLANK\">((.|\n)*?)<\/A>')
                    source_other2data3=source_other2pattern3.search(source)
                    source=source_other2data3.group(2).strip()
                else:
                    source=news_anotherdata.group(5).strip()
                date = news_anotherdata.group(9)[5:]
                content =news_anotherdata.group(1)
                for next_page in self.multi_news_page(news_info, page_content):
                    content += news_anotherdata.search(next_page).group(1)
            elif news_anotherdata1:
                source = news_anotherdata1.group(3).strip()
                source_pattern4=re.compile("(.|\n)*?\'>(.*?)<\/a>(.|\n)*?cn\">(.*?)<\/a")
                source_data4=source_pattern4.search(source)
                source=source_data4.group(2)+source_data4.group(4)
                date = news_anotherdata1.group(1)[5:]
                author =news_anotherdata1.group(8)
                content =news_anotherdata1.group(5)
                for next_page in self.multi_news_page(news_info, page_content):
                    content += news_anotherdata1.search(next_page).group(5)
            else:
                author = news_otherdata.group(11)
                source = news_otherdata.group(5).strip()
                if 'HREF' in source and 'href' in source:
                    source_pattern1=re.compile('\"_BLANK\">((.|\n)*?)<\/A>(.|\n)*?\">(.*?)<\/a>')
                    source_data1=source_pattern1.search(source)
                    source=source_data1.group(1).strip()+" "+source_data1.group(4).strip()
                elif 'HREF' not in source and 'href' in source:
                    source=source[3:]
                    source_otherpattern2=re.compile('((.|\n)*?)<\/span>(.|\n)*?\">(.*?)<\/a>')
                    source_otherdata2=source_otherpattern2.search(source)
                    source=source_otherdata2.group(1).strip()+" "+source_otherdata2.group(4).strip()
                elif 'HREF' in source and 'href' not in source:
                    source=source[3:]
                    source_other1pattern3=re.compile('(.|\n)*?BLANK\">((.|\n)*?)<\/A>')
                    source_other1data3=source_other1pattern3.search(source)
                    source=source_other1data3.group(2).strip()
                else:
                    source=news_otherdata.group(5).strip()
                date = news_otherdata.group(3)[5:]
                content =news_otherdata.group(8)
                for next_page in self.multi_news_page(news_info, page_content):
                    content += news_otherdata.search(next_page).group(8)

            news_info["author"] = author
            news_info["source"] = source
            news_info["inner_page_date"] = date
            news_info["content"] = content
        except Exception as e:
            raise NewsProcessor.ProcessorException(
                "Fail to parse url: %s: "%(news_info["url"]) + e.message)
            return None
