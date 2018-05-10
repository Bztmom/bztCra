# -*- coding: utf-8 -*-
from .common import *

website_name = "新华网"
website_short_name = "xhw"
data_path = "../data/"
ckpt_path = "../ckpt/"
log_path = "../log/"
default_ckpt_days = 50
default_log_level = "info"

conf = {
    "domain_name": website_name,
    "pipelines": [

    ]  # end of pipelines for a website
}  # end of config of a website
pattern_conf = {
    "news": {
        "list_patterns": [
            r'lass="clearfix">.*?<h3><a href="(?P<url>.*?)".*?>(?P<title>.*?)<\/'
        ],
        "news_patterns": [
            r'h-time">(?P<pub_date>.*?)<\/sp.*?来源：.*?<em.*?>(?P<source>.*?)<\/.*?<div class="main">.*?swiper-scrollbar.*?<span.*?<\/div>.*?<\/div.*?<\/div>(?P<content>.*?)<div class="zan-wap">'
        ]
    },
}


def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        yield crawler.list_url_tpl


b_class_dict = {
    "科技-滚动新闻": {
        "url": "http://www.xinhuanet.com/tech/qqbb.htm",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "kjgdxw",
        "pattern_type": "news"
    },
    "金融联播": {
        "url": "http://www.xinhuanet.com/tech/qqbb.htm",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "jrlb",
        "pattern_type": "news"
    },
    "滚动新闻": {
        "url": "http://www.xinhuanet.com/fortune/gd.htm",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "gdxw",
        "pattern_type": "news"
    },
}

for name, info in b_class_dict.iteritems():
    pipeline_conf = {
        "name": name,
        "log_level": info.get("debug_level", default_log_level),
        "log_filename": "%s/%s_%s.log" % (log_path, website_short_name, info["short_name"]),
        "crawler":
            {
                "name": info.get("crawler", "XX_Crawler.XXNewsETL.NewsCrawler"),
                "params":
                    {
                        "list_url_tpl": info["url"],
                        "data_path": "%s/%s/" % (data_path, website_short_name),
                        "base_url": info["base_url"],
                        "website_name": website_name,
                        "b_class": name,
                        "checkpoint_filename": "%s/%s_%s.ckpt" % (ckpt_path, website_short_name, info["short_name"]),
                        "checkpoint_saved_days": info.get("ckpt_days", default_ckpt_days),
                        "list_patterns": pattern_conf[info["pattern_type"]]["list_patterns"],
                        "pub_date_format": info["pub_date_format"],
                        "next_list_url_generator": info.get("list_url_gen", info["next_list_url_generator"]),
                        "header": info.get("header", None)
                        # "log_filename": "./test.log"
                    }
            },
        "transformers": [
            {
                "name": "XX_Crawler.XXProcessors.DetailNewsContentParser" if "parser" not in info else info["parser"],
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
    # print pipeline_conf
    conf["pipelines"].append(pipeline_conf)


