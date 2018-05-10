# -*- coding: utf-8 -*-
from .common import *
from XX_Crawler.Utils import get
import re

website_name = "财经网"
website_short_name = "cjw"
data_path = "../data/"
ckpt_path = "../ckpt/"
log_path = "../log/"
default_ckpt_days = 50
default_log_level = "info"

default_pub_date_format = "%Y-%m-%d %H:%M"

conf = {
    "domain_name": website_name,
    "pipelines": [
        
    ]  # end of pipelines for a website
}  # end of config of a website
pattern_conf = {
    "news":{
        "list_patterns" : [
        ],
        "news_patterns" : [
            r'<div  id="article" class="article">.*?<span id="cont_num1.*?">(?P<comment_cnt>.*?)<\/span>.*?<span id="source_baidu">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>(.*?)<span id="pubtime_baidu">(?P<pub_date>.*?):\d\d<\/span>.*?<div id="the_content" style="font-size:14px;" class="article-content">(?P<content>.*?)<div class="ar_keywords">',
            r'<div class="article">.*?(<span class="news_name">来源：(?P<source>.*?)<\/span>)?<span class="news_time">(?P<pub_date>.*?)<\/span>.*?<div class="article-content">(?P<content>.*?)<div class="news_other">'
        ]
    },
    "it" :{
        "list_patterns" : [
            r'ls_news_r">.*?<a href="(?P<url>.*?)".*?>(?P<title>.*?)<\/',
            r'wzbt">.*?<a href="(?P<url>.*?)".*?>(?P<title>.*?)<\/a'
        ],
        "news_patterns" : [
            r'<div  id="article" class="article">.*?<span id="cont_num1.*?">(?P<comment_cnt>.*?)<\/span>.*?<span id="source_baidu">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>(.*?)<span id="pubtime_baidu">(?P<pub_date>.*?):\d\d<\/span>.*?<div id="the_content" style="font-size:14px;" class="article-content">(?P<content>.*?)<div class="ar_keywords">',
            r'<div class="article">.*?(<span class="news_name">来源：(?P<source>.*?)<\/span>)?<span class="news_time">(?P<pub_date>.*?)<\/span>.*?<div class="article-content">(?P<content>.*?)<div class="news_other">',
            r'news_name">来源：(?P<source>.*?)<\/.*?news_time">(?P<pub_date>.*?)<\/span.*?article-content">(?P<content>.*?)<\/div',
            r'news_time">(?P<pub_date>.*?)<\/span.*?article-content">(?P<content>.*?)<\/div',
        ]
    },
    "itz" :{
        "list_patterns" : [
            r'ls_news_r">.*?<a href="(?P<url>.*?)".*?>(?P<title>.*?)<\/.*?ls_news_time">(?P<pub_date>.*?)<\/',
        ],
        "news_patterns" : [
            r'news_name">来源：(?P<source>.*?)<\/.*?article-content">(?P<content>.*?)<\/div',
            r'news_name">来源：(?P<source>.*?)<\/.*?article-content">(?P<content>.*?)<\/div',
        ]
    },
}

b_class_dict = {
    "新闻": {"url":"http://roll.caijing.com.cn/ajax_lists.php?modelid=0", "short_name":"xw", "pattern_type":"news","crawler_func": "CJWNewsPipeline.CJWNewsCrawler",},
    "科技-移动互联": {"url":"http://tech.caijing.com.cn/internet/index.shtml", "short_name":"ydwl", "pattern_type":"it"},
    "IT业界": {"url":"http://tech.caijing.com.cn/itindustry/", "short_name":"ityj","pub_date_format":"%Y-%m-%d", "pattern_type":"itz"},
    "智能": {"url":"http://tech.caijing.com.cn/intelligence/", "short_name":"zn", "pattern_type":"it"},
    "手机": {"url":"http://tech.caijing.com.cn/mobile/", "short_name":"sj", "pattern_type":"it"},
    "产经": {"url":"http://industry.caijing.com.cn/index.html", "short_name":"cj", "pattern_type":"it"},
    "行业": {"url":"http://www.caijing.com.cn/hangye/", "short_name":"hy", "pattern_type":"it"},
}

def default_generate_next_list_url(crawler):
    for page_num in range(1, 2):
        yield crawler.list_url_tpl

for name, info in b_class_dict.iteritems():
    pipeline_conf = {
        "name": name,
        "log_level": info.get("debug_level",default_log_level),
        "log_filename": "%s/%s_%s.log"%(log_path, website_short_name, info["short_name"]),
        "crawler":
        {
            # "name": info.get("crawler","CJWNewsPipeline.CJWNewsCrawler"),
            "name": info.get("crawler", "XX_Crawler.XXNewsETL.NewsCrawler" if "crawler_func" not in info else info[
                "crawler_func"]),
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
                "start_page_num" : 1,
                #"log_filename": "./test.log"
            }
        },
        "transformers": [
            {
                "name": "XX_Crawler.XXProcessors.DetailNewsContentParser"  if "parser" not in info else info["parser"],
                "params": {
                    "detail_patterns": pattern_conf[info["pattern_type"]]["news_patterns"],
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


