# -*- coding: utf-8 -*-
from .common import *
from XX_Crawler.Utils import get
import re

website_name = "财新网"
website_short_name = "cxw"
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
        ],
        "news_patterns" : [
            r'<span class="bd_block" id="source_baidu">来源：\s?<a.*?>(?P<source>.*?)<\/a><\/span>(<span class="bd_block" id="author_baidu">作者：(?P<author>.*?)<\/span>)?.*?<div id="Main_Content_Val" class="text">(?P<content>.*?)<\/div>',
        ]
    },
}

b_class_dict = {
    "金融": {"url":"http://tag.caixin.com/news/homeInterface.jsp?channel=125&start=0&count=20&picdim=_145_97&callback=jQuery172024195236779624762_1514002859886", "short_name":"jr", "pattern_type":"news"},
    # "公司": {"url":"http://tag.caixin.com/news/homeInterface.jsp?channel=130&start=0&count=20&picdim=_145_97&callback=jQuery172024195236779624762_1514002859886", "short_name":"gs", "pattern_type":"news"},
    # "经济": {"url":"http://tag.caixin.com/news/homeInterface.jsp?channel=129&start=0&count=20&picdim=_145_97&callback=jQuery172024195236779624762_1514002859886", "short_name":"jj", "pattern_type":"news"},
    # "政经": {"url":"http://tag.caixin.com/news/homeInterface.jsp?channel=131&start=0&count=20&picdim=_145_97&callback=jQuery172024195236779624762_1514002859886", "short_name":"zj", "pattern_type":"news"},
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
            "name": info.get("crawler","CXWNewsPipeline.CXWNewsCrawler"),
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


