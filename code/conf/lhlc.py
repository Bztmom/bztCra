# -*- coding: utf-8 -*-
from .common import *

website_name = "龙虎财经"
website_short_name = "lhlc"
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
pattern_conf = {"news":{
        "list_patterns" : [
            r'<li class="list-group-item list-group-item-nobor"><a href="(?P<url>.*?)" target="_blank">(?P<title>.*?)<\/a><\/li>'
        ],
        "news_patterns" : [
            r'<div class="message">(?P<pub_date>.*?)<span.*?<div class="articalCont">(?P<content>.*?)<p class="articalWrite"><a class="long" .*?来源：(?P<source>.*?)编辑：(?P<author>.*?)<\/p>',
       ]
    },
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 1:
            yield crawler.list_url_tpl


b_class_dict = {
    "金融理财": {"url":"http://finance.longhoo.net/jinronglicai/index.html", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"jrlc", "pattern_type":"news"},
    "商业资讯": {"url":"http://finance.longhoo.net/shangyezixun/index.html", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"syzx", "pattern_type":"news"},
    "通讯IT": {"url":"http://finance.longhoo.net/tongxunit/index.html", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"IT", "pattern_type":"news"},
    "品牌资讯": {"url":"http://finance.longhoo.net/pinpaizixun/index.html", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"ppzx", "pattern_type":"news"},
    "健康美容": {"url":"http://finance.longhoo.net/jiankangmeirong/index.html", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"jkmr", "pattern_type":"news"},
}


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
                "pub_date_format":info["pub_date_format"],
                "next_list_url_generator":info.get("list_url_gen",info["next_list_url_generator"]),
                "header":info.get("header", None)
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


