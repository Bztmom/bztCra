# -*- coding: utf-8 -*-

############################################
##
# defination of new crawler framework
##
##
#############################################

import re
import traceback
import cPickle as pickle
from datetime import datetime
from datetime import timedelta
import json
import chardet
from types import MethodType
import os
import requests
import time
import logging
import HTMLParser
# from XX_ES.XX_ESExporter.ESExporter import ESExporter

# class ESCrawler():

#     def __init__(self, server_list, index_name, doc_type, query):
#         self.exporter = ESExporter(server_list, index_name, doc_type, query)

#     def run(self):
#         for doc in self.exporter.fetch_data():
#             yield doc
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def default_list_url_gen(crawler):
    for crawler.page_num in range(1, 3):
        yield crawler.list_url_tpl % (crawler.page_num)


class NewsCrawler:
    '''Crawler base class
    '''

    debug = False

    def __init__(self,
                 list_url_tpl,
                 data_path,
                 website_name,
                 b_class,
                 list_patterns=[],
                 requests_interval=1,
                 banned_interval=5,
                 max_request_retry=5,
                 logger=None,
                 checkpoint_filename=None,
                 checkpoint_saved_days=50,
                 encoding="utf-8",
                 pub_date_format=None,
                 next_list_url_generator=None,
                 base_url=None,
                 header=None,
                 news_header=None,
                 start_page_num=None,
                 allow_redirect=True,
                 is_post=False,
                 post_body={},
                 proxies=None,
                 max_itered_page_num=3
                 ):
        self.requests_interval = requests_interval
        self.exception_interval = requests_interval
        self.banned_interval = banned_interval
        self.max_request_retry = max_request_retry
        self.list_url_tpl = list_url_tpl
        self.page_num = start_page_num if start_page_num is not None else 0
        self.data_path = data_path
        self.allow_redirect = allow_redirect
        # check if the data path exists
        if not os.path.exists(data_path):
            os.mkdir(data_path)
        self.doc_counter = 0
        self.website_name = website_name
        self.b_class = b_class
        if logger is None:
            self.logger = logging.getLogger()
        else:
            self.logger = logger
        self.checkpoint_filename = checkpoint_filename
        # load check point
        self.check_point = self.load_checkpoint()
        self.no_check_point = True if self.check_point is None else False
        self.checkpoint_saved_days = checkpoint_saved_days
        if header is None:
            self.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
        else:
            self.headers = header
        if news_header is None:
            self.news_header = self.headers
        else:
            self.news_header = news_header

        self.list_patterns = [re.compile(
            list_pattern, re.DOTALL) for list_pattern in list_patterns]
        self.encoding = encoding
        if pub_date_format is not None:
            self.pub_date_format = pub_date_format
        else:
            self.pub_date_format = u"%Y-%m-%d %H:%M"
        if base_url is not None:
            self.base_url = base_url
        else:
            self.base_url = list_url_tpl  # "http://www.cs.com.cn/gppd/"

        # self.next_list_url_generator = next_list_url_generator
        if next_list_url_generator is not None:
            self.generate_next_list_url = MethodType(
                next_list_url_generator, self)
        # if next_list_url_generator is None:
        #     self.next_list_url_generator = default_list_url_gen

        self.is_post = is_post
        self.post_body = post_body
        self.html_parser = HTMLParser.HTMLParser()
        # proxy
        self.proxy = proxies

        self.max_itered_page_num = max_itered_page_num

    def __del__(self):
        # dump check point
        # self.dump_checkpoint()
        pass

    class CrawlerException(Exception):
        '''Exception for News Crawler
        '''

        def __init__(self, err='Crawler error'):
            Exception.__init__(self, err)

    # load checkpoin from file system
    def load_checkpoint(self):
        try:
            if self.checkpoint_filename is None:
                self.checkpoint_filename = self.__class__.__name__ + ".ckpt"
            with open(self.checkpoint_filename, "r") as fd:
                return pickle.loads(fd.read())
        except:
            return None

    # dump checkpoint to filesystem
    def dump_checkpoint(self):
        if self.check_point is not None:
            ##temp strategy
            if self.checkpoint_saved_days < 300:
                self.checkpoint_saved_days = 300
            savedDay = timedelta(days=self.checkpoint_saved_days)
            now = datetime.now()
            if len(self.check_point) > 500:
                self.check_point = dict(filter(lambda items: items[1] > (
                        now - savedDay), self.check_point.items()))
            with open(self.checkpoint_filename, "w") as fd:
                fd.write(pickle.dumps(self.check_point))
            self.logger.debug("finished dumping checkpoint")

    # run crawler yield news_info structur for every news
    def run(self):
        # if self.next_list_url_generator is None:
        #     list_url_gen = self.generate_next_list_url
        # else:
        #     list_usr_gen = self.next_list_url_generator
        for list_url in self.generate_next_list_url():
            self.page_num += 1
            # generate list page url
            self.logger.debug("start to download %s" % (list_url))
            # fetching list page content
            try:
                content = self.get(
                    list_url, header=self.headers, is_post=self.is_post)
            except NewsCrawler.CrawlerException as ce:
                if self.page_num <= 1:
                    raise NewsCrawler.CrawlerException(str(ce) +
                                                       "when crawling news list url: %s" % (list_url))
                content = None
                self.logger.error("stat:download:start:failed:%s" % list_url)
                continue
            # generate list page filename
            filename = self.generate_list_filename(list_url)
            if content is not None:
                # write list page to local fs
                self.write_to_file(filename, content)
                # iterate all news in the list page
                update_finished = False
                for news_info in self.generate_url_from_list(content):
                    if news_info is not None:
                        news_url = news_info["url"]
                        # fetching news page
                        self.logger.info("stat:download:start:%s" % (news_url))
                        try:
                            content = self.get(news_url, header=self.news_header)
                        except NewsCrawler.CrawlerException as ce:
                            self.logger.info(
                                "stat:download:end:failed:" + str(ce))
                            # logging.warning("Failed to download %s with content is None"%(news_url))
                            continue
                        # processing news page
                        filename = self.generate_news_filename(news_info)
                        if filename is None:
                            self.logger.warning(
                                "generate news filename falsed for url:%s" % (news_info["url"]))
                            # return False
                            continue
                        news_info["filename"] = filename
                        news_info["website_name"] = self.website_name
                        if "b_class" not in news_info:
                            news_info["b_class"] = self.b_class
                        encoding = chardet.detect(content)['encoding']
                        if encoding is None:
                            encoding = self.encoding  # "utf-8"
                        if encoding.lower() == "gb2312":
                            encoding = "gbk"
                        if (encoding != "utf-8" and encoding != "gb2312" and encoding != "gbk"):
                            encoding = self.encoding
                        news_info["content"] = content.decode(
                            encoding, "ignore")  # .encode("utf-8").replace("&nbsp;"," ")
                        news_info["content"] = self.html_parser.unescape(
                            news_info["content"]).encode("utf-8").replace("\xc2\xa0", " ")
                        self.write_to_file(
                            filename + ".news_info", pickle.dumps(news_info))
                        # self.write_to_file(filename, content)
                        # add crawler in news_info
                        news_info["crawler"] = self
                        yield news_info
                        # self.process_news_page(news_info, content)
                    else:
                        # if news_info is None
                        #
                        update_finished = True
                        break
                if update_finished:
                    break
                continue
            else:
                self.logger.info(
                    "stat:download:end:failed:" + str(list_url) + "")
            # If it fails when crawling first page of news list
            break
        self.task_finished()
        self.dump_checkpoint()

    # requests get wrapper
    def get(self, url, timeout=30, header={}, is_post=False):
        retry_count = 0
        while retry_count < self.max_request_retry:
            try:
                retry_count += 1
                self.logger.debug("getting " + url)
                if not is_post:
                    page = requests.get(
                        url, timeout=timeout, headers=header, allow_redirects=self.allow_redirect, proxies=self.proxy)
                else:
                    page = requests.post(url, timeout=timeout, headers=header,
                                         allow_redirects=self.allow_redirect, data=self.post_body, proxies=self.proxy)
                if page.status_code != 200:
                    self.logger.debug("url:%s return %d" %
                                      (url, page.status_code))
                    raise NewsCrawler.CrawlerException(
                        "requests return %d" % (page.status_code))
                    return None
                if not self.is_page_banned(page.content):
                    time.sleep(self.requests_interval)
                    self.doc_counter += 1
                    return page.content
                else:
                    time.sleep(self.banned_interval)
            except Exception as e:
                self.logger.debug("get exception : " + str(e.message))
                time.sleep(self.exception_interval)
        raise NewsCrawler.CrawlerException(e.message)
        return None

    def write_to_file(self, filename, content):
        with open(filename, "w") as fd:
            fd.write(content)
        self.logger.debug("finished writing file " + filename)

    # overwrite function
    def task_finished(self):
        pass

    # overwrite to generate news page filename
    def generate_news_filename(self, news_info):
        filename = "_".join(news_info['url'].split("/")[3:])
        filename = filename.replace("?", "_QM_")
        self.logger.debug("generate news filename " + filename)
        return self.data_path + filename

    # overwrite to generate list page filename
    def generate_list_filename(self, url):
        filename = "_".join(url.split("/")[3:]) + "_" + str(int(time.time()))
        filename = filename.replace("?", "_QM_")
        self.logger.debug("generate list filename " + filename)
        return self.data_path + filename

    # overwrite to generate new list page url
    def generate_next_list_url(self):
        for page_num in range(self.max_itered_page_num):
            # self.page_num += 1
            yield self.list_url_tpl % (self.page_num)

    # overwrite to parse list page
    def parse_list_page(self, content):
        self.logger.debug("start to parse page %d" % self.page_num)
        encoding = chardet.detect(content)['encoding']
        if encoding is None:
            encoding = self.encoding  # "utf-8"
        if encoding.lower() == "gb2312" or encoding.lower() == "gbk":
            encoding = "gbk"
        if (encoding != "utf-8" and encoding != "gb2312" and encoding != "gbk"):
            encoding = self.encoding
        for list_pattern in self.list_patterns:
            matched = False
            for m in list_pattern.finditer(content.decode(encoding, "ignore").encode("utf-8")):
                # print >>sys.stderr,m.groupdict()
                news_info = {}
                for key, value in m.groupdict().iteritems():
                    # print key
                    if key == "url" and not value.startswith("http"):
                        value = self.base_url + value
                    if key == "pub_date":
                        value = value.replace("&nbsp;", " ")
                        value = value.replace("\xc2\xa0", "")
                        value = value.replace("\n", " ")
                        value = value.strip(" ")
                        if isinstance(self.pub_date_format, list):
                            for val in self.pub_date_format:
                                try:
                                    value = datetime.strptime(value, val)
                                except:
                                    self.logger.debug("pub_date re abnormal")
                        else:
                            value = datetime.strptime(value, self.pub_date_format)
                        # value = value.replace(year = datetime.now().year)
                    news_info[key] = value
                    # if isinstance(value, basestring) or isinstance(value, unicode):
                    # print >>sys.stderr,key,value
                    # if key==u"title":
                    #     print value.decode("utf-8")
                    # print >>sys.stderr, news_info
                # deal with the pub time with out year
                if "pub_date" in news_info:
                    if news_info["pub_date"].year == 1900:
                        # year is not set
                        self.logger.debug("year not found")
                        m = re.search(r"\/(?P<year>201\d).*?\/.*",
                                      news_info["url"])
                        cur_year = datetime.now().year
                        if m:
                            cur_year = int(m.group("year"))
                        self.logger.debug("set year to %d" % (cur_year))
                        news_info["pub_date"] = news_info["pub_date"].replace(
                            year=cur_year)
                if "url" in news_info:
                    # unscape
                    news_info["url"] = news_info["url"].replace("\/", "/")

                # , news_info["pub_date"]))
                self.logger.debug("found news %s \n %s" %
                                  (news_info["title"], news_info["url"]))
                # print >>sys.stderr, news_info

                yield news_info
                matched = True
            if matched:
                break

    # overwrite to check if the news needs to be updated
    def news_need_update(self, news_info):
        return False

    # overwrite to check if ip is banned
    def is_page_banned(self, content):
        return False

    def generate_url_from_list_ex(self, content):
        '''this function generate news_info by parsing the list page
           when the old news are meet return None to end the whole process
           return :
               this function yield news_info which is a dict whoes keys
               are url, title,
        '''
        for news_info in self.parse_list_page(content):
            if not self.news_need_update(news_info):
                yield None
                break
            yield news_info
        pass

    def generate_url_from_list(self, content):
        news_info_list = [
            news_info for news_info in self.parse_list_page(content)]
        if len(news_info_list) == 0:
            yield None
        news_start_flag = False
        old_news_count = 0
        if self.check_point is None:
            self.check_point = {}
        for news_info in reversed(news_info_list):
            news_title = news_info["title"]
            if news_title in self.check_point:
                old_news_count += 1
                self.logger.debug("%s in check_point, continue" % news_title)
                continue
            # print >>sys.stderr, news_info
            if "pub_date" in news_info:
                self.check_point[news_title] = news_info["pub_date"]
            else:
                self.check_point[news_title] = datetime.now()
            self.logger.debug("add %s to check_point" % news_title)
            yield news_info
            # break
        self.logger.debug("finish parse list page %d" % (self.page_num))
        if old_news_count > 3:
            self.logger.debug(
                "this page has more than 3 old news stop crawling")
            yield None
        if self.no_check_point and self.page_num > 3:
            self.logger.debug("no last check point info. one page finished")
            yield None
