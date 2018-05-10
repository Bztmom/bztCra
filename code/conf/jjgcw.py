# -*- coding: utf-8 -*-
from .common import *

website_name = "经济观察网"
website_short_name = "jjgcw"
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
    "news":{
        "list_patterns" : [
            r'<li>.*?<span.*?><a href="(?P<url>.*?)" target="_blank">(?P<title>.*?)<\/a>'
        ],
        "news_patterns" : [
            r'<div class="xd-bottom">.*?<h1>(.*)<\/h1>.*?<p>(?P<author>.*?)<span>(?P<pub_date>.*?)<\/span>.*?<div class="xx_boxsing"><p.*?>.*?<\/p>(?P<content>.*?)<\/div>',
        ]
    },
}

b_class_dict = {
    "证券": {"url":"http://www.eeo.com.cn/jinrong/zhengquan/", "short_name":"zq", "pattern_type":"news"},
    "新三板": {"url":"http://www.eeo.com.cn/jinrong/xinsanban/", "short_name":"xsb", "pattern_type":"news"},
    "地产": {"url":"http://www.eeo.com.cn/fcqcxf/dichan/", "short_name":"dc", "pattern_type":"news"},
    "银行": {"url":"http://www.eeo.com.cn/jinrong/jijin/", "short_name":"yh", "pattern_type":"news"},
    "时事": {"url":"http://www.eeo.com.cn/yaowen/dashi/", "short_name":"ss", "pattern_type":"news"},
    "债市": {"url":"http://www.eeo.com.cn/jinrong/zhaishi/", "short_name":"zs", "pattern_type":"news"},
    "资讯": {"url":"http://www.eeo.com.cn/zixun/", "short_name":"zx", "pattern_type":"news"},
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 1:
        yield crawler.list_url_tpl

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
                "pub_date_format": info.get("pub_date_format",None)
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


