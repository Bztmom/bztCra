# -*- coding: utf-8 -*-
from .common import *

website_name = "虎嗅网"
website_short_name = "huxiu"
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
            r'author-name">.*?>(?P<author>.*?)<\/a>.*?article-time.*?">(?P<pub_date>.*?)<\/span>.*?<!--文章头图-->(?P<content>.*)(<\/div>.*?<div class="Qr-code">)'
        ]
    },
}


def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            crawler.page_num += 1
        yield crawler.list_url_tpl

b_class_dict = {
    "电商消费": {
        "url": "https://www.huxiu.com/channel/103.html",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"https://www.huxiu.com/",
        "short_name": "dsxf",
        "pattern_type": "news"
    },
    "雪花一代": {
        "url": "https://www.huxiu.com/channel/106.html",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"https://www.huxiu.com/",
        "short_name": "xhyd",
        "pattern_type": "news"
    },
    "车与出行": {
        "url": "https://www.huxiu.com/channel/21.html",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"https://www.huxiu.com/",
        "short_name": "cycx",
        "pattern_type": "news"
    },
    "医疗健康": {
        "url": "https://www.huxiu.com/channel/111.html",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"https://www.huxiu.com/",
        "short_name": "yljk",
        "pattern_type": "news"
    },
    "企业服务": {
        "url": "https://www.huxiu.com/channel/110.html",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"https://www.huxiu.com/",
        "short_name": "qyfw",
        "pattern_type": "news"
    },
    "社交通讯": {
        "url": "https://www.huxiu.com/channel/112.html",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"https://www.huxiu.com/",
        "short_name": "sjtx",
        "pattern_type": "news"
    },
    "娱乐淘金": {
        "url": "https://www.huxiu.com/channel/22.html",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"https://www.huxiu.com/",
        "short_name": "yltj",
        "pattern_type": "news"
    },
    "人工智能": {
        "url": "https://www.huxiu.com/channel/104.html",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"https://www.huxiu.com/",
        "short_name": "rgzn",
        "pattern_type": "news"
    },
    "智能终端": {
        "url": "https://www.huxiu.com/channel/105.html",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"https://www.huxiu.com/",
        "short_name": "znzd",
        "pattern_type": "news"
    },
    "金融地产": {
        "url": "https://www.huxiu.com/channel/102.html",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"https://www.huxiu.com/",
        "short_name": "jrdc",
        "pattern_type": "news"
    },
    "创业维艰": {
        "url": "https://www.huxiu.com/channel/2.html",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"https://www.huxiu.com/",
        "short_name": "cywj",
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


