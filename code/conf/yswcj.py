# -*- coding: utf-8 -*-
from .common import *

website_name = "央视网经济"
website_short_name = "yswcj"
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
            r'\"title\":\"(?P<title>.*?)\".*?\"dateTime\":\"(?P<pub_date>.*?)\".*?\"url\":\"(?P<url>.*?)\"'
        ],
        "news_patterns" : [
            r'<!--repaste.title.begin-->(?P<title>.*?)<!--repaste.title.end-->.*?来源：<i.*?>(?P<source>.*?)<\/i>.*?<!--repaste.body.begin-->(?P<content>.*?)<!--repaste.body.end-->',
            r'<h1><!--repaste.title.begin-->(?P<title>.*?)<!--repaste.title.end--><\/h1>.*?<i>来源.*?>(?P<source>.*?)<\/a>.*?<!--repaste.body.begin-->(?P<content>.*?)<!--repaste.body.end-->',
        ]
    }
}

b_class_dict = {
    "首页": {"url":"http://jingji.cctv.com/data/index.json", "short_name":"sy", "pattern_type":"news"},
    "财经": {"url":"http://jingji.cctv.com/caijing/data/index.json", "short_name":"cj", "pattern_type":"news"},
    "315": {"url":"http://jingji.cctv.com/315/data/index.json", "short_name":"315", "pattern_type":"news"},
    "公司": {"url":"http://jingji.cctv.com/gongsi/data/index.json", "short_name":"gs", "pattern_type":"news"},
    "观点": {"url":"http://jingji.cctv.com/shiping/data/index.json", "short_name":"gd", "pattern_type":"news"},
    "人物": {"url":"http://jingji.cctv.com/renwu/data/index.json", "short_name":"rw", "pattern_type":"news"},
    "供给侧改革": {"url":"http://jingji.cctv.com/gjc/data/index.json", "short_name":"gjcgg", "pattern_type":"news"},
    "部委动态": {"url":"http://jingji.cctv.com/bwdt/data/index.json", "short_name":"bwdt", "pattern_type":"news"},
    "网评财经": {"url":"http://jingji.cctv.com/cjpl/data/index.json", "short_name":"wpcj", "pattern_type":"news"},
}

def default_generate_next_list_url(crawler):
    # while crawler.page_num < 2:
    #     if crawler.page_num == 0:
            ret_url = crawler.list_url_tpl
            # crawler.list_url_tpl += "index_%d.htm"
            yield ret_url
        # else:
        #     ret_url = crawler.list_url_tpl % (crawler.page_num)
        #     yield ret_url

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
                "pub_date_format":u"%Y-%m-%d %H:%M",
                "next_list_url_generator":info.get("list_url_gen", default_generate_next_list_url) ,
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
            # {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },

        ],
        "uploader": online_mysql_uploader_conf
    }
    #print pipeline_conf
    conf["pipelines"].append(pipeline_conf)

