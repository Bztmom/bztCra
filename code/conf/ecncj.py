# -*- coding: utf-8 -*-
from .common import *
from XX_Crawler.Utils import get
import re

website_name = "ECN财经"
website_short_name = "ecncj"
data_path = "../data/"
ckpt_path = "../ckpt/"
log_path = "../log/"
default_ckpt_days = 50
default_log_level = "info"

default_pub_date_format = "%Y-%m-%d %H:%M:%S"

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
            r'<!-- content s -->.*?<p class="article-title">(?P<title>.*?)<\/p>.*?<p class="article-details">.*?<span>来源：(?P<source>.*?)<\/span>.*?<span>(?P<comment_cnt>\d+)条评论<\/span>.*?<span class="article-time">时间：(?P<pub_date>.*?)<\/span>.*?<div class="article-main-content">(?P<content>.*?)<!--div class="article-footer">',
        ]
    },
}

b_class_dict = {
    "新闻": {"url":"http://www.ecnfinance.net/e/class/loadmore.php", "short_name":"xw", "pattern_type":"news"},
}

def default_generate_next_list_url(crawler):
    for page_num in range(1, 2):
        crawler.post_body = {
            "id":'select * from [!db.pre!]ecms_news order by newstime desc limit 0,40;',
            "num":'0,30',
            "len":30,
            "titleshow":0,
            "type":24,
            "mode":2,
            "pic":1,
        }
        yield crawler.list_url_tpl

for name, info in b_class_dict.iteritems():
    pipeline_conf = {
        "name": name,
        "log_level": info.get("debug_level",default_log_level),
        "log_filename": "%s/%s_%s.log"%(log_path, website_short_name, info["short_name"]),
        "crawler":
        {
            "name": info.get("crawler","ECNCJNewsPipeline.ECNCJNewsCrawler"),
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
                "is_post" : True,
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


