# -*- coding: utf-8 -*-
from .common import *

website_name = "北京晨报"
website_short_name = "bjcb"
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
            r'(<div class="main-nr">|<div class="lb-nt">)+.*?href="(?P<url>.*?)"\s*title="(?P<title>.*?)"\sclass'
        ],
        "news_patterns": [
            r'<!-- 文章相关信息.*?"date">(?P<pub_date>.*?)<\/span.*文章来源：\s*(?P<source>.*?)\s*<\/s.*<!-- 描述 -->(?P<content>.*?)<!-- @end 文章内容 -->'
        ]
    },
}


def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            crawler.page_num += 1
        ret_url = crawler.list_url_tpl % (crawler.page_num)
        yield ret_url

b_class_dict = {
    "经济": {
        "url": "http://www.morningpost.com.cn/Finance/jingji/%d.shtml",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "cjjj",
        "pattern_type": "news"
    },
    "投资": {
        "url": "http://www.morningpost.com.cn/Finance/tz/%d.shtml",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "cjtz",
        "pattern_type": "news"
    },
    "金融": {
        "url": "http://www.morningpost.com.cn/Finance/jinrong/%d.shtml",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "cjjr",
        "pattern_type": "news"
    },
    "科技": {
        "url": "http://www.morningpost.com.cn/newly/keji/%d.shtml",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "xzkj",
        "pattern_type": "news"
    },
    "军事": {
        "url": "http://www.morningpost.com.cn/newly/mil/%d.shtml",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "xzjs",
        "pattern_type": "news"
    },
    "互联网": {
        "url": "http://www.morningpost.com.cn/newly/Internet/%d.shtml",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "xzhlw",
        "pattern_type": "news"
    },
    "汽车": {
        "url": "http://www.morningpost.com.cn/life/auto/%d.shtml",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "qc",
        "pattern_type": "news"
    },
    "房产": {
        "url": "http://www.morningpost.com.cn/life/fangchan/%d.shtml",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "fc",
        "pattern_type": "news"
    },
    "娱乐": {
        "url": "http://www.morningpost.com.cn/life/fangchan/%d.shtml",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "yl",
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


