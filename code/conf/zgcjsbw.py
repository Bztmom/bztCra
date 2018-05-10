# -*- coding: utf-8 -*-
from .common import *
import re
from XX_Crawler.Utils import get

website_name = "中国财经时报网"
website_short_name = "zgcjsbw"
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
            r'<h2 class="title"><a href="(?P<url>.*?)".*?title="(?P<title>.*?)"'
        ],
        "news_patterns": [
            r'来源：<ins>(?P<source>.*?)<\/ins>.*?发布时间：(?P<pub_date>.*?)<\/span.*?class="text">(?P<content>.*?)<\/div'
        ]
    },
}


def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num != 0:
            ret_url = crawler.list_url_tpl+"%d.html" % (crawler.page_num)
        else:
            ret_url = crawler.list_url_tpl+"index.html"
        yield ret_url


b_class_dict = {
    "财经要闻": {
        "url": "http://focus.3news.cn/cjyw/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "cjyw",
        "pattern_type": "news"
    },
    "行业要闻": {
        "url": "http://focus.3news.cn/hyxw/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "hyxw",
        "pattern_type": "news"
    },
    "市场评论": {
        "url": "http://focus.3news.cn/scpl/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "scpl",
        "pattern_type": "news"
    },
    "曝光台": {
        "url": "http://focus.3news.cn/bgt/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "bgt",
        "pattern_type": "news"
    },
    "时事": {
        "url": "http://focus.3news.cn/jdht/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "ss",
        "pattern_type": "news"
    },
    "宏观": {
        "url": "http://finance.3news.cn/fx/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "fx",
        "pattern_type": "news"
    },
    "金融": {
        "url": "http://finance.3news.cn/jr/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "jr",
        "pattern_type": "news"
    },
    "国内": {
        "url": "http://finance.3news.cn/gn/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "gn",
        "pattern_type": "news"
    },
    "国际": {
        "url": "http://finance.3news.cn/gj/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "gj",
        "pattern_type": "news"
    },
    "公司": {
        "url": "http://finance.3news.cn/gs/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "gs",
        "pattern_type": "news"
    },
    "大数据": {
        "url": "http://focus.3news.cn/dsj/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "dsj",
        "pattern_type": "news"
    },
    "原创": {
        "url": "http://www.3news.cn/yc/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "yc",
        "pattern_type": "news"
    },
    "股票-24小时直播": {
        "url": "http://stock.3news.cn/24xszb/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "24xszb",
        "pattern_type": "news"
    },
    "外汇": {
        "url": "http://forex.3news.cn/rdzz/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "rdzz",
        "pattern_type": "news"
    },
    "期市": {
        "url": "http://futures.3news.cn/qsyw/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "qsyw",
        "pattern_type": "news"
    },
    "支付": {
        "url": "http://wangdai.3news.cn/zf/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "zf",
        "pattern_type": "news"
    },
    "网贷": {
        "url": "http://wangdai.3news.cn/wd/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "wd",
        "pattern_type": "news"
    },
    "行业": {
        "url": "http://wangdai.3news.cn/hy/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "hy",
        "pattern_type": "news"
    },
    "科技热点": {
        "url": "http://tech.3news.cn/kjrd/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "kjrd",
        "pattern_type": "news"
    },
    "热点24小时": {
        "url": "http://www.3news.cn/24hot/",
        "base_url": None,
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "24hot",
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
                        "base_url": info["base_url"],
                        "data_path": "%s/%s/" % (data_path, website_short_name),
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
                    "detail_patterns": pattern_conf[info["pattern_type"]]["news_patterns"],
                }
            },
            # {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },

        ],
        "uploader": online_mysql_uploader_conf
    }
    # print pipeline_conf
    conf["pipelines"].append(pipeline_conf)


