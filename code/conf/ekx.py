# -*- coding: utf-8 -*-
from .common import *

website_name = "e公司"
website_short_name = "ekx"
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
            r'栏目链接.*?a.*?title="(?P<title>.*?) href="(?P<url>.*?)"'
        ],
        "news_patterns": [
            r'author">(?P<author>.*?)<span class="time">(?P<pub_date>.*?)<\/span>.*?source">(?P<source>.*?)<\/span.*?content">(?P<content>.*?)<\/div'
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
    "快讯": {
        "url": "http://www.egsea.com/index.php?app=Company&mod=Index&act=flash&ajax=true&p=%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url": None,
        "short_name": "kx",
        "pattern_type": "news"
    },
    "首页": {
        "url": "http://www.egsea.com/index.php?app=Company&mod=Index&act=index&ajax=true&p=%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url": None,
        "short_name": "sy",
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
                "name": info.get("crawler", "EKXNewsPipline.EKXNewsCrawler"),
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


