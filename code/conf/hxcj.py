# -*- coding: utf-8 -*-
from .common import *

website_name = "华讯财经"
website_short_name = "hxcj"
data_path = "../data/"
ckpt_path = "../ckpt/"
log_path = "../log/"
default_ckpt_days = 50
default_log_level = "info"

default_pub_date_format = "%Y-%m-%d %H:%M"
# default_header = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
#     "Host":"www.yicai.com",
#     "Referer":"http://www.yicai.com/news/shijie/",
#     "X-Requested-With":"XMLHttpRequest"
# }

def default_generate_next_list_url(crawler):
    for page_num in range(1, 2):
        yield crawler.list_url_tpl

conf = {
    "domain_name": website_name,
    "pipelines": [
        
    ]  # end of pipelines for a website
}  # end of config of a website
pattern_conf = {
    "news":{
        "list_patterns" : [
            r'<li><a href="(?P<url>[^"_]*?shtml)" target="_blank">(?P<title>.*?)<\/a>(?P<pub_date>\d{4}-\d{2}-\d{2} \d{2}:\d{2})<\/li>'
        ],
        "news_patterns" : [
            r'<div id="main".*?>.*?<div class="info">.*?\d{4}年\d{2}月\d{2}日 \d{2}:\d{2}:\d{2}\s+(?P<source>.*?)<\/div>.*?<div class="newsContainer" id="newsCon">(?P<content>.*?)<div class="pagex">',
        ]
    },
}

b_class_dict = {
    # "国内财经": {"url":"http://finance.591hx.com/lista/gncj.shtml","short_name":"gncj", "pattern_type":"news"},
    # "国际财经": {"url":"http://finance.591hx.com/lista/gjlc.shtml","short_name":"gjcj", "pattern_type":"news"},
    # "公司新闻": {"url":"http://finance.591hx.com/lista/gs.shtml","short_name":"gs", "pattern_type":"news"},
    # "宏观经济": {"url":"http://finance.591hx.com/lista/hgjj.shtml","short_name":"hgjj", "pattern_type":"news"},
    # "产经-房产": {"url":"http://finance.591hx.com/lista/fc.shtml","short_name":"cjfc", "pattern_type":"news"},
    # "产经-汽车": {"url":"http://finance.591hx.com/lista/qc.shtml","short_name":"cjqc", "pattern_type":"news"},
    # "产经-能源": {"url":"http://finance.591hx.com/lista/nysy.shtml","short_name":"cjny", "pattern_type":"news"},
    # "产经-IT": {"url":"http://finance.591hx.com/lista/itjd.shtml","short_name":"cjit", "pattern_type":"news"},
    "股票-上市公司": {"url":"http://stock.591hx.com/list/ssgs.shtml","short_name":"gpssgs", "pattern_type":"news"},

}

# def default_generate_next_list_url(crawler):
#     while crawler.page_num < 1:
#         yield crawler.list_url_tpl

for name, info in b_class_dict.iteritems():
    pipeline_conf = {
        "name": name,
        "log_level": info.get("debug_level",default_log_level),
        "log_filename": "%s/%s_%s.log"%(log_path, website_short_name, info["short_name"]),
        "crawler":
        {
            "name": info.get("crawler","XX_Crawler.XXNewsETL.NewsCrawler"),
            "params":
            {
                "list_url_tpl": info["url"],
                "data_path": "%s/%s/"%(data_path, website_short_name),
                "website_name": website_name,
                "b_class": name,
                "checkpoint_filename": "%s/%s_%s.ckpt"%(ckpt_path, website_short_name, info["short_name"]),
                "checkpoint_saved_days": info.get("ckpt_days",default_ckpt_days) ,
                "list_patterns": pattern_conf[info["pattern_type"]]["list_patterns"],
                "next_list_url_generator":info.get("list_url_gen", default_generate_next_list_url) ,
                "header":info.get("header", None),
                "pub_date_format": info.get("pub_date_format",default_pub_date_format),
                "start_page_num" : 1,
                "base_url": info.get("base_url", None)
                #"log_filename": "./test.log"
            }
        },
        "transformers": [
            {
                "name": "XX_Crawler.XXProcessors.DetailNewsContentParser"  if "parser" not in info else info["parser"],
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
    #print pipeline_conf
    conf["pipelines"].append(pipeline_conf)


