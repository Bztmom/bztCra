# -*- coding: utf-8 -*-
from .common import *

website_name = "钛媒体"
website_short_name = "tmt"
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
            r'<h3><a.*?href="(?P<url>.*?)" title="(?P<title>.*?)"'
        ],
        "news_patterns": [
            r'<!-- 文章相关信息.*?"date">(?P<pub_date>.*?)<\/span.*文章来源：\s*(?P<source>.*?)\s*<\/s.*<!-- 描述 -->(?P<content>.*?)<!-- @end 文章内容 -->',
            r'<div class="post-info">.*?<a title="(?P<author>.*?)".*?class="time.*?>(?P<pub_date>.*?)<\/span>.*?<\/div>(?P<content>.*?)<\/article>'
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
    "大公司": {
        "url": "http://www.tmtpost.com/column/2446153/%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.tmtpost.com/",
        "short_name": "dgs",
        "pattern_type": "news"
    },
    "创投": {
        "url": "http://www.tmtpost.com/column/2446155/%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.tmtpost.com/",
        "short_name": "ct",
        "pattern_type": "news"
    },
    "汽车出行": {
        "url": "http://www.tmtpost.com/column/2573550/%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.tmtpost.com/",
        "short_name": "qccx",
        "pattern_type": "news"
    },
    "快讯": {
        "url": "http://www.tmtpost.com/column/2581216/%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.tmtpost.com/",
        "short_name": "kx",
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


