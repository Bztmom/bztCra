# -*- coding: utf-8 -*-
from .common import *
from XX_Crawler.Utils import get
import re

website_name = "21经济网"
website_short_name = "21jjw"
data_path = "../data/"
ckpt_path = "../ckpt/"
log_path = "../log/"
default_ckpt_days = 50
default_log_level = "info"

default_pub_date_format = "%Y年%m月%d日%H:%M"


def multi_news_page(self, news_info, content):
    self.logger.debug("multi page process")
    page_info_pattern = re.compile(
        r'<div id="pages" class="text-c">(?P<page_div>.*?)<\/div>', re.DOTALL)
    page_pattern = re.compile(r'<a href="(?P<url>.*?)">(?P<page_num>\d{1,2})<\/a>', re.DOTALL)
    content_pattern = re.compile(r'<div class="detailCont">(?P<content>.*?)<div id="pages" class="text-c">', re.DOTALL)
    page_info_data = page_info_pattern.search(content)
    if page_info_data:
        # print page_info_data.group(1)
        page_div = page_info_data.group("page_div")
        max_page_num = 1
        for m in page_pattern.finditer(page_div):
            cur_page_num = int(m.group("page_num"))
            if cur_page_num > max_page_num:
                max_page_num = cur_page_num
        self.logger.debug(
            "there are %d pages for this news" % (max_page_num))
        cur_url = news_info["url"]
        for page_num in xrange(2, max_page_num+1):
            # next page url is t2017-10-09_32432432.html =>t2017-10-09_32432432_1.html
            next_url = cur_url[:-5] + "_%d" %(page_num) + cur_url[-5:]
            page_content = get(next_url)
            self.logger.debug("got next page %s"%next_url)
            if page_content is not None:
                m = content_pattern.search(page_content)
                if m:
                    self.logger.debug("yield next_page content")
                    yield m.group("content")
    pass

conf = {
    "domain_name": website_name,
    "pipelines": [
        
    ]  # end of pipelines for a website
}  # end of config of a website
pattern_conf = {
    "news":{
        "list_patterns" : [
            r'<div class="Tlist">.*?<a href="(?P<url>.*?)".*?>(?P<title>.*?)<\/a>.*?<p class="shuoming">.*?<span.*?>.*?<span.*?>(?P<source>.*?)<\/span><span.*?>(?P<author>.*?)<\/span>'
        ],
        "news_patterns" : [
            r'<div class="content">.*?<p class="Wh">.*?<span class="">(?P<part_1_pub_date>.*?)<\/span>.*?<span class="hour">(?P<part_2_pub_date>.*?)<\/span>.*?<div class="detailCont">(?P<content>.*?)<div id="pages" class="text-c">',
            r'<div class="newsInfo">(?P<source>.*?)<a.*?<div class="newsDate">(?P<pub_date>.*?)<\/div.*?txtContent.*?>(?P<content>.*?)<div'
        ]
    },
}

b_class_dict = {
    "财经": {"url":"http://www.21jingji.com/channel/money/", "short_name":"cj", "pattern_type":"news"},
    "政经": {"url":"http://www.21jingji.com/channel/politics/", "short_name":"zj", "pattern_type":"news"},
    "金融": {"url":"http://www.21jingji.com/channel/finance/", "short_name":"jr", "pattern_type":"news"},
    "商业": {"url":"http://www.21jingji.com/channel/business/", "short_name":"sy", "pattern_type":"news"},
    "数读": {"url":"http://www.21jingji.com/channel/readnumber/", "short_name":"sd", "pattern_type":"news" ,"pub_date_format" :"%Y-%m-%d %H:%M"},
    "宏观": {"url":"http://www.21jingji.com/channel/politics/", "short_name":"hg", "pattern_type":"news" },
    "一带一路": {"url":"http://www.21jingji.com/channel/BandR/", "short_name":"ydyl", "pattern_type":"news","pub_date_format" :"%Y-%m-%d %H:%M"},
    "自贸": {"url":"http://www.21jingji.com/channel/ftz/", "short_name":"zm", "pattern_type":"news","pub_date_format" :"%Y-%m-%d %H:%M"},
    "大湾区": {"url":"http://www.21jingji.com/channel/GHM_GreaterBay/", "short_name":"dwq", "pattern_type":"news","pub_date_format" :"%Y-%m-%d %H:%M"},
}

def default_generate_next_list_url(crawler):
    for page_num in range(1, 2):
        if page_num == 1:
            yield crawler.list_url_tpl
        else:
            yield "%s/%d.html"%(crawler.list_url_tpl, page_num)

for name, info in b_class_dict.iteritems():
    pipeline_conf = {
        "name": name,
        "log_level": info.get("debug_level",default_log_level),
        "log_filename": "%s/%s_%s.log"%(log_path, website_short_name, info["short_name"]),
        "crawler":
        {
            "name": info.get("crawler","XX_Crawler.XXNewsETL.NewsCrawler"),
            "params":
            {
                "list_url_tpl": info["url"],
                "data_path": "%s/%s/"%(data_path, website_short_name),
                "website_name": website_name,
                "b_class": name,
                "checkpoint_filename": "%s/%s_%s.ckpt"%(ckpt_path, website_short_name, info["short_name"]),
                "checkpoint_saved_days": info.get("ckpt_days",default_ckpt_days) ,
                "list_patterns": pattern_conf[info["pattern_type"]]["list_patterns"],
                "next_list_url_generator":info.get("list_url_gen", default_generate_next_list_url) ,
                "header":info.get("header", None),
                "pub_date_format": info.get("pub_date_format",default_pub_date_format),
                "start_page_num" : 1
                #"log_filename": "./test.log"
            }
        },
        "transformers": [
            {
                "name": "XX_Crawler.XXProcessors.DetailNewsContentParser"  if "parser" not in info else info["parser"],
                "params": {
                    "detail_patterns": pattern_conf[info["pattern_type"]]["news_patterns"],
                    "multi_news_page_func": multi_news_page,
                }
            },
            {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },

        ],
        "uploader": online_mysql_uploader_conf
    }
    #print pipeline_conf
    conf["pipelines"].append(pipeline_conf)


