# -*- coding: utf-8 -*-
from .common import *

website_name = "中国日报中文网"
website_short_name = "zwwcj"
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
            r'<h3><a href="(?P<url>.*?)" target="_blank">(?P<title>.*?)<\/a><\/h3>'
        ],
        "news_patterns" : [
            r'作者：(?P<author>.*?)来源：(?P<source>.*?)<\/div>.*?id="pubtime">(?P<pub_date>.*?)<\/div>.*?<div id="Content" class="article">(?P<content>.*?)<!--\/enpcontent-->',
            r'来源：(?P<source>.*?)<\/div>.*?id="pubtime">(?P<pub_date>.*?)<\/div>.*?<div id="Content" class="article">(?P<content>.*?)<!--\/enpcontent-->',
            r'来源：(?P<source>.*?)<\/div>.*?id="pubtime">(?P<pub_date>.*?)<\/div>.*?<div class="datu-one" id="Content">(?P<content>.*?)<!--\/enpcontent-->',
            r'<date>(?P<pub_date>.*?)<\/date><author>(?P<author>.*?)<\/author>.*?<div id="Content" class="article">(?P<content>.*?)<!--\/enpcontent-->',
            r'来源:(?P<source>.*?)<\/div>.*?<div class="xinf-le">(?P<pub_date>.*?)<\/div>.*?<div class="article">(?P<content>.*?)<!--\/enpcontent-->',
            r'id="pubtime">(?P<pub_date>.*?)<\/div>.*?id="Content">(?P<content>.*?)<!--/enpcontent-->'
       ]
    },
}


def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url=crawler.list_url_tpl
            crawler.page_num+=1
            crawler.list_url_tpl = crawler.list_url_tpl[:-4]+"_%d.htm"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

def gd_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url=crawler.list_url_tpl
            crawler.page_num+=1
            crawler.list_url_tpl = crawler.list_url_tpl+"index_%d.html"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url
b_class_dict = {
    "财经要闻": {"url":"http://caijing.chinadaily.com.cn/node_53008184.htm", "base_url":"http://caijing.chinadaily.com.cn/","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"cjyw", "pattern_type":"news"},
    "财经独家": {"url":"http://caijing.chinadaily.com.cn/node_1119884.htm", "base_url":"http://caijing.chinadaily.com.cn/","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"cjdj", "pattern_type":"news"},
    "跨国公司": {"url":"http://caijing.chinadaily.com.cn/node_1140261.htm", "base_url":"http://caijing.chinadaily.com.cn/","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"kggs", "pattern_type":"news"},
    "财料": {"url":"http://caijing.chinadaily.com.cn/node_53004690.htm", "ckpt_days":300,"base_url":"http://caijing.chinadaily.com.cn/","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"cl", "pattern_type":"news"},
    "财圈说": {"url":"http://caijing.chinadaily.com.cn/node_53004689.htm","ckpt_days":300,"base_url":"http://caijing.chinadaily.com.cn/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"cqs", "pattern_type":"news"},
    "大咖订阅号": {"url":"http://caijing.chinadaily.com.cn/node_53008185.htm", "ckpt_days":300,"base_url":"http://caijing.chinadaily.com.cn/","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"dkdyh", "pattern_type":"news"},
    "金融-新闻": {"url":"http://finance.chinadaily.com.cn/node_53002229.htm","base_url":"http://finance.chinadaily.com.cn/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"jrxw", "pattern_type":"news"},
    "金融-全球": {"url":"http://finance.chinadaily.com.cn/node_53005879.htm", "base_url":"http://finance.chinadaily.com.cn/","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"jrqq", "pattern_type":"news"},
    "金融-市场": {"url":"http://finance.chinadaily.com.cn/node_53005878.htm", "base_url":"http://finance.chinadaily.com.cn/","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"jrsc", "pattern_type":"news"},
    "金融-证券": {"url":"http://finance.chinadaily.com.cn/node_53005869.htm", "base_url":"http://finance.chinadaily.com.cn/","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"jrzq", "pattern_type":"news"},
    "金融-基金": {"url":"http://finance.chinadaily.com.cn/node_53005871.htm", "base_url":"http://finance.chinadaily.com.cn/","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"jrjj", "pattern_type":"news"},
    "金融-商业": {"url":"http://finance.chinadaily.com.cn/node_53005875.htm", "base_url":"http://finance.chinadaily.com.cn/","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"jrsy", "pattern_type":"news"},
    "滚动": {"url":"http://caijing.chinadaily.com.cn/finance/", "base_url":"http://caijing.chinadaily.com.cn/finance/","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":gd_generate_next_list_url,"short_name":"gd", "pattern_type":"news"},
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
                "base_url":info["base_url"],
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


