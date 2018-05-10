# -*- coding: utf-8 -*-
from .common import *

website_name = "号外财经网"
website_short_name = "hwcjw"
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
            r'<h5><a href="(?P<url>.*?)".*?>(?P<title>.*?)<\/a><\/h5>',
            r'<li>\s*<a href="(?P<url>.*?)".*?h5>(?P<title>.*?)<\/h5',
        ],
        "news_patterns": [
            r'时间：(?P<pub_date>.*?)作者：(?P<author>.*?)编辑：(?P<source>.*?)来源.*?Article">(?P<content>.*?)<\/div>\s?\S?<div class="article-page'
        ]
    },
}


def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url = crawler.list_url_tpl
        else:
            crawler.page_num += 1
            ret_url = crawler.list_url_tpl +str(crawler.page_num) +".html"
        yield ret_url

b_class_dict = {
    "号外": {
        "url": "http://www.haowaicaijing.com/htm/",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "hy",
        "pattern_type": "news"
    },
    "要闻": {
        "url": "http://www.haowaicaijing.com/html/yaowen/",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "yw",
        "pattern_type": "news"
    },
    "上市公司": {
        "url": "http://www.haowaicaijing.com/html/ssgs/",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "ssgs",
        "pattern_type": "news"
    },
    "基金": {
        "url": "http://www.haowaicaijing.com/html/jijing/",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "jj",
        "pattern_type": "news"
    },
    "证券": {
        "url": "http://www.haowaicaijing.com/html/gupiao/",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "zq",
        "pattern_type": "news"
    },
    "银行": {
        "url": "http://www.haowaicaijing.com/html/yinhan/",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "yh",
        "pattern_type": "news"
    },
    "保险": {
        "url": "http://www.haowaicaijing.com/html/gp/",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "bx",
        "pattern_type": "news"
    },
    "互金": {
        "url": "http://www.haowaicaijing.com/html/hlwjr/",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "hj",
        "pattern_type": "news"
    },
    "新三板": {
        "url": "http://www.haowaicaijing.com/html/x3b/",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "x3b",
        "pattern_type": "news"
    },
    "地产": {
        "url": "http://www.haowaicaijing.com/html/dichan/",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "dc",
        "pattern_type": "news"
    },
    "汽车": {
        "url": "http://www.haowaicaijing.com/html/qiche/",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "dc",
        "pattern_type": "news"
    },
    "快报": {
        "url": "http://www.haowaicaijing.com/html/zmtl/",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "dc",
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


