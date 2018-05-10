# -*- coding: utf-8 -*-
import chardet
import re

from .common import *
import json

website_name = "中国新闻网"
website_short_name = "zgxww"
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
            r'<div class="dd_bt"><a href="/cj(?P<url>.*?)">(?P<title>.*?)<\/a',
            r'<div class="dd_bt"><a href="/business(?P<url>.*?)">(?P<title>.*?)<\/a',
            r'class="color065590">.*?<a href=\'(?P<url>.*?)\n\'.*?>(?P<title>.*?)<\/a'
        ],
        "news_patterns": [
            r'"pubtime_baidu">(?P<pub_date>.*?)<\/span>.*?source_baidu">来源：<a.*?>(?P<source>.*?)<\/a.*?<!--正文start-->.*?<div.*?>(?P<content>.*?)<!--正文start-->',
            r'"pubtime_baidu">(?P<pub_date>.*?)<\/span>.*?source_baidu">来源：(?P<source>.*?)<\/span.*?<!--正文start-->.*?<div.*?>(?P<content>.*?)<!--正文start-->',
        ]
    },
}

headers = {
    "newsPageHeaders": {
        'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'Keep-Alive',
        'Host': 'finance.chinanews.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    },
    "CjPageHeaders": {
        'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'Keep-Alive',
        'Host': 'www.chinanews.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    },
}


def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        print crawler.page_num
        if crawler.page_num == 0:
            ret_url = crawler.list_url_tpl
        else:
            ret_url = crawler.list_url_tpl+"pager=%d" % (crawler.page_num)
        yield ret_url


def gd_list_url(crawler):
    yield crawler.list_url_tpl



b_class_dict = {
    "财经-滚动": {
        "url": "http://finance.chinanews.com/cj/gd.shtml",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": gd_list_url,
        "base_url": "http://finance.chinanews.com/cj",
        "short_name": "cjgd",
        "pattern_type": "news",
        "header": headers['newsPageHeaders']
    },
    "产经-滚动": {
        "url": "http://www.chinanews.com/business/gd.shtml",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": gd_list_url,
        "base_url": "http://www.chinanews.com/business",
        "short_name": "chanjgd",
        "pattern_type": "news",
        "header": headers['CjPageHeaders'],
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
