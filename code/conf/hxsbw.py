# -*- coding: utf-8 -*-
from .common import *

website_name = "华夏时报网"
website_short_name = "hxsbw"
data_path = "../data/"
ckpt_path = "../ckpt/"
log_path = "../log/"
default_ckpt_days = 50
default_log_level = "debug"

conf = {
    "domain_name": website_name,
    "pipelines": [

    ]  # end of pipelines for a website
}  # end of config of a website
pattern_conf = {
    "news": {
        "list_patterns": [
            r'class="item">.*?<h2.*?href="(?P<url>.*?)">(?P<title>.*?)<\/a><\/h2',
        ],
        "news_patterns": [
            r'class="title">.*?作者：<a.*?>(?P<author>.*?)<\/a>.*来源：(?P<source>.*?)<\/p.*发布时间：(?P<pub_date>.*?)<\/p>.*?infoMain">(?P<content>.*?)<div',
        ]
    },
}


def default_generate_next_list_url(crawler):
    while crawler.page_num < 4:
        if crawler.page_num == 0:
            crawler.page_num += 1
        ret_url = crawler.list_url_tpl % (crawler.page_num)
        yield ret_url

b_class_dict = {
    "财经": {
        "url": "http://www.chinatimes.cc/finance?page=%d",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.chinatimes.cc",
        "short_name": "cj",
        "pattern_type": "news"
    },
    "金融": {
        "url": "http://www.chinatimes.cc/finance/jinrong?page=%d",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.chinatimes.cc",
        "short_name": "jr",
        "pattern_type": "news"
    },
    "政策": {
        "url": "http://www.chinatimes.cc/finance/zhengce?page=%d",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.chinatimes.cc",
        "short_name": "zc",
        "pattern_type": "news"
    },
    "观点": {
        "url": "http://www.chinatimes.cc/finance/guandian?page=%d",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.chinatimes.cc",
        "short_name": "gd",
        "pattern_type": "news"
    },
    "调查": {
        "url": "http://www.chinatimes.cc/finance/diaocha?page=%d",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.chinatimes.cc",
        "short_name": "dc",
        "pattern_type": "news"
    },
    "地产": {
        "url": "http://www.chinatimes.cc/finance/dichan?page=%d",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.chinatimes.cc",
        "short_name": "dichan",
        "pattern_type": "news"
    },
    "公司": {
        "url": "http://www.chinatimes.cc/finance/gongsi?page=%d",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.chinatimes.cc",
        "short_name": "gs",
        "pattern_type": "news"
    },
    "人物": {
        "url": "http://www.chinatimes.cc/finance/renwu?page=%d",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.chinatimes.cc",
        "short_name": "rw",
        "pattern_type": "news"
    },
    "汽车": {
        "url": "http://www.chinatimes.cc/finance/qiche?page=%d",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.chinatimes.cc",
        "short_name": "qc",
        "pattern_type": "news"
    },
    "天下": {
        "url": "http://www.chinatimes.cc/finance/tianxia?page=%d",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.chinatimes.cc",
        "short_name": "tx",
        "pattern_type": "news"
    },
    "视点": {
        "url": "http://www.chinatimes.cc/category/25.html?page=%d",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.chinatimes.cc",
        "short_name": "sd",
        "pattern_type": "news"
    },
    "财经大V": {
        "url": "http://www.chinatimes.cc/dav?page=%d",
        "pub_date_format": "%Y-%m-%d %H:%M:%S",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.chinatimes.cc",
        "short_name": "cjdv",
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


