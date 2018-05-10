# -*- coding: utf-8 -*-
from .common import *
import re
from XX_Crawler.Utils import get

website_name = "财联社"
website_short_name = "cls"
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
            r'"title":"(?P<title>.*?)".*?"id":(?P<url>.*?),'
        ],
        "news_patterns": [
            r'class="writer".*?>(?P<author>.*?)<\/span.*?class="ctime".*?>(?P<pub_date>.*?)<\/div>.*?class="thisContent".*?>(?P<content>.*?)<\/div'
        ]
    },
}


def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        ret_url = crawler.list_url_tpl % (crawler.page_num)
        print ret_url
        yield ret_url


b_class_dict = {
    "题材": {
        "url": "https://www.cailianpress.com/nodeapi/themes?page=%d&per_page=15",
        "base_url": "https://www.cailianpress.com/theme/",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "tc",
        "pattern_type": "news"
    },
    "深度": {
        "url": "https://www.cailianpress.com/nodeapi/depths?page=%d&per_page=15",
        "base_url": "https://www.cailianpress.com/depth/",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "short_name": "sd",
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


