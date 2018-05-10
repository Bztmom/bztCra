# -*- coding: utf-8 -*-
from .common import *

website_name = "金融界" #from 叶檀财经
website_short_name = "ytcj"
data_path = "../data/"
ckpt_path = "../ckpt/"
log_path = "../log/"
default_ckpt_days = 50
default_log_level = "info"

default_pub_date_format = "%Y-%m-%d %H:%M:%S"

conf = {
    "domain_name": website_name,
    "pipelines": [
        
    ]  # end of pipelines for a website
}  # end of config of a website
pattern_conf = {
    "news":{
        "list_patterns" : [
            r'<li class="dot"><label><a href="(?P<url>.*?)">(?P<title>.*?)<\/a><\/label>\d{2}-\d{2}<\/li>'
        ],
        "news_patterns" : [
            r'<span><!--jrj_final_date_start-->(?P<pub_date>.*?)<!--jrj_final_date_end-->.*?<\/span><span>来源：<!--jrj_final_source_start-->(?P<source>.*?)<!--jrj_final_source_end-->.*?</span>.*?<span>作者：<!--jrj_final_author_start-->(?P<author>.*?)<!--jrj_final_author_end--></span>.*?<div class="texttit_m1">(?P<content>.*?)<!--jrj_final_context_end-->',
        ]
    },
}

b_class_dict = {
    "叶檀财经": {"url":"http://finance.jrj.com.cn/expert/expert_97.shtml", "short_name":"ytcj", "pattern_type":"news"},
    
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
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
                "pub_date_format": info.get("pub_date_format",default_pub_date_format),
                "start_page_num" : 1
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


