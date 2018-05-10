# -*- coding: utf-8 -*-
from .common import *

website_name = "中新经纬"
website_short_name = "zxjw"
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
            r'<li class="div1">.*?<h3><a href="(?P<url>.*?)">(?P<title>.*?)<\/a>'
        ],
        "news_patterns": [
            r'<div class="time">(?P<pub_date>.*?)  (?P<source>.*?)<\/d.*?<div class="content_zwimg">.*?<\/div>(?P<content>.*?)<div class="editor">\(编辑：(?P<author>.*?)\)<\/di'
        ]
    },
}


def default_generate_next_list_url(crawler):
    yield crawler.list_url_tpl

b_class_dict = {
    "金融": {
        "url": "http://www.jwview.com/jr.html",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.jwview.com",
        "short_name": "jr",
        "pattern_type": "news"
    },
    "股市": {
        "url": "http://www.jwview.com/zq.html",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.jwview.com",
        "short_name": "gs",
        "pattern_type": "news"
    },
    "产经": {
        "url": "http://www.jwview.com/lc.html",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.jwview.com",
        "short_name": "lc",
        "pattern_type": "news"
    },
    "科技": {
        "url": "http://www.jwview.com/kj.html",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.jwview.com",
        "short_name": "kj",
        "pattern_type": "news"
    },
    "汽车": {
        "url": "http://www.jwview.com/qc.html",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.jwview.com",
        "short_name": "qc",
        "pattern_type": "news"
    },
    "V言": {
        "url": "http://www.jwview.com/jwmj.html",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.jwview.com",
        "short_name": "jwmj",
        "pattern_type": "news"
    },
    "原创": {
        "url": "http://www.jwview.com/original.html",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.jwview.com",
        "short_name": "original",
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


