# -*- coding: utf-8 -*-
from .common import *

website_name = "第一财经"
website_short_name = "dycj"
data_path = "../data/"
ckpt_path = "../ckpt/"
log_path = "../log/"
default_ckpt_days = 50
default_log_level = "info"

default_pub_date_format = "%Y-%m-%d %H:%M:%S"
default_header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Host":"www.yicai.com",
    "Referer":"http://www.yicai.com/news/shijie/",
    "X-Requested-With":"XMLHttpRequest"
}

conf = {
    "domain_name": website_name,
    "pipelines": [
        
    ]  # end of pipelines for a website
}  # end of config of a website
pattern_conf = {
    "news":{
        "list_patterns" : [
            r'<dl class="f-cb dl-item">.*?<dd>.*?<h5 class="f-ff1 f-fwn f-fs14">.*?<a href="(?P<b_class_url>.*?)">(?P<b_class>.*?)<\/a>.*?<h3 class="f-ff1 f-fwn f-fs22">.*?<a href="(?P<url>.*?)">(?P<title>.*?)<\/a>.*?<h4 class="f-ff1 f-fwn f-fs14">.*?<span>(?P<author>.*?)<\/span>(?P<pub_date>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'
        ],
        "news_patterns" : [
            r'<div class="m-txt m-txt-mb">.*?<h2 class="f-ff1 f-fwn f-fs14"><i>(?P<source>.*?)<\/i>.*?<a.*?>(?P<b_class>.*?)<\/a><span>(?P<author>.*?)<\/span>.*?<i id="changyan_count_unit">(?P<comment_cnt>.?)<\/i>.*?<div class="m-text">(?P<content>.*?)<\/div>',
            r'<div class="m-txt m-txt-mb">.*?<h2 class="f-ff1 f-fwn f-fs14"><a.*?>(?P<b_class>.*?)<\/a><span>.*?<\/h2>.*?<div class="m-text">(?P<content>.*?)</div>\s*<h3.*?>编辑：<span>(?P<author>.*?)<\/span><\/h3>'
        ]
    },
}

b_class_dict = {
    "新闻": {"url":"http://www.yicai.com/api/ajax/NsList/%d/77", "short_name":"xw", "pattern_type":"news"},
    
}

# def default_generate_next_list_url(crawler):
#     while crawler.page_num < 1:
#         yield crawler.list_url_tpl

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
                "next_list_url_generator":info.get("list_url_gen", None) ,
                "header":info.get("header", default_header),
                "pub_date_format": info.get("pub_date_format",default_pub_date_format),
                "start_page_num" : 1
                #"log_filename": "./test.log"
            }
        },
        "transformers": [
            {
                "name": "XX_Crawler.XXProcessors.DetailNewsContentParser"  if "parser" not in info else info["parser"],
                "params": {
                    "detail_patterns": pattern_conf[info["pattern_type"]]["news_patterns"]
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


