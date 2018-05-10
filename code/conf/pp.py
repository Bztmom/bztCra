# -*- coding: utf-8 -*-
from .common import *

website_name = "澎湃"
website_short_name = "pp"
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
            r'<h2><a href="(?P<url>.*?)".*?>(?P<title>.*?)<\/a>'
        ],
        "news_patterns": [
            r'class="news_about">\s*<p>(?P<title>.*?)<\/p>\s*?<p>\s*(?P<pub_date>.*?)<span>(?P<source>.*?)<\/span.*?<\/div>\s*<\/div>(?P<content>.*?)<div class="go_to_topic'
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
    "10%公司": {
        "url": "http://www.thepaper.cn/load_index.jsp?nodeids=25434&topCids=&pageidx=%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.thepaper.cn/",
        "short_name": "gs",
        "pattern_type": "news"
    },
    "能见度": {
        "url": "http://www.thepaper.cn/load_index.jsp?nodeids=25436&topCids=&pageidx=%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.thepaper.cn/",
        "short_name": "njd",
        "pattern_type": "news"
    },
    "地产界": {
        "url": "http://www.thepaper.cn/load_index.jsp?nodeids=25433&topCids=&pageidx=%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.thepaper.cn/",
        "short_name": "dcj",
        "pattern_type": "news"
    },
    "财经上下游": {
        "url": "http://www.thepaper.cn/load_index.jsp?nodeids=25438&topCids=&pageidx=%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.thepaper.cn/",
        "short_name": "cjsxy",
        "pattern_type": "news"
    },
    "金改实验室": {
        "url": "http://www.thepaper.cn/load_index.jsp?nodeids=25435&topCids=&pageidx=%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.thepaper.cn/",
        "short_name": "jgsys",
        "pattern_type": "news"
    },
    "牛市点线面": {
        "url": "http://www.thepaper.cn/load_index.jsp?nodeids=25437&topCids=&pageidx=%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.thepaper.cn/",
        "short_name": "nsdxm",
        "pattern_type": "news"
    },
    "科技湃": {
        "url": "http://www.thepaper.cn/load_index.jsp?nodeids=27234&topCids=&pageidx=%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.thepaper.cn/",
        "short_name": "kjp",
        "pattern_type": "news"
    },
    "澎湃商学院": {
        "url": "http://www.thepaper.cn/load_index.jsp?nodeids=25485&topCids=&pageidx=%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.thepaper.cn/",
        "short_name": "ppsxy",
        "pattern_type": "news"
    },
    "自贸区连线": {
        "url": "http://www.thepaper.cn/load_index.jsp?nodeids=25432&topCids=&pageidx=%d",
        "pub_date_format": "%Y-%m-%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":"http://www.thepaper.cn/",
        "short_name": "zmqlx",
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


