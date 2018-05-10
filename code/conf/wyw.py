# -*- coding: utf-8 -*-
from .common import *

website_name = "未央网"
website_short_name = "wyw"
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
            r'category-post-node".*?href="(?P<url>.*?)".*?h2.*?>(?P<title>.*?)<\/h2'
        ],
        "news_patterns": [
            r'<b style="color: #333;">(?P<author>.*?)\|(?P<source>.*?)<\/.*?uk-text-right">.*?<\/p>(?P<content>.*?)<p class="uk-alert-warning"',
            r'<b style="color: #333;">(?P<author>.*?)原文来源：(?P<source>.*?)<\/.*?wyt-post-international-cn.*?>(?P<content>.*?)<\/div',
            r'<meta property="og:site_name" content="(?P<source>.*?)".*?article.*?div style="height.*?>.*?<\/p>(?P<content>.*?)<div'
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
    "传统金融": {
        "url": "http://www.weiyangx.com/category/tranditional-financial-institution/page/%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "ctjr",
        "pattern_type": "news"
    },
    "互联网": {
        "url": "http://www.weiyangx.com/category/based-on-internet/page/%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "hlw",
        "pattern_type": "news"
    },
    "全新金融": {
        "url": "http://www.weiyangx.com/category/new-modes/page/%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "qxjr",
        "pattern_type": "news"
    },
    "经济": {
        "url": "http://www.weiyangx.com/category/internet-economy/page/%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "jj",
        "pattern_type": "news"
    },
    "投融资": {
        "url": "http://www.weiyangx.com/category/investment-and-financing/page/%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "trz",
        "pattern_type": "news"
    },
    "政策": {
        "url": "http://www.weiyangx.com/category/supervision-and-policy/page/%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "zc",
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
                "name": info.get("crawler", "WYWNewsPipline.WYWNewsCrawler"),
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


