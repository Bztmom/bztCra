# -*- coding: utf-8 -*-
from .common import *

website_name = "猎金"
website_short_name = "liejin99"
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
pattern_conf = {"jp":{
        "list_patterns" : [
            r'<div class="title"><a href="(?P<url>.*?)" title="(?P<title>.*?)" target="_blank">.*?<\/a><\/div>'
        ],
        "news_patterns" : [
            r'<span class="source-from">.*?作者：(?P<author>.*?)<\/span>.*?<span class="source-time">(?P<pub_date>.*?)<\/span>.*?<div class="art-content">(?P<content>.*?)<!--articletag-->',
            ]
    },
        "gd":{
        "list_patterns" : [
            r'<div class="plaintext_m">.*?<h3 class="title"><a href="(?P<url>.*?)" target="_blank">(?P<title>.*?)<\/a><\/h3>.*?<p class="time">(?P<pub_date>.*?)<\/p>'
        ],
        "news_patterns" : [
            r'(来源：(?P<source>[^<]*?)<\/span>.*?)?<span class="source-time">.*?<\/span>.*?<div class="art-content">(?P<content>.*?)<!--articletag-->',
            r'Refresh".*?URL=(?P<content>.*?)"',
            ]
    },
}

def gd_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url = crawler.list_url_tpl+"fortune_list/"
            crawler.page_num+=1
            crawler.list_url_tpl = crawler.list_url_tpl+"fortune_list/"+"index_%d.shtml"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

def jp_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url = crawler.list_url_tpl+"ljdjjp_list/"
            crawler.page_num+=1
            crawler.list_url_tpl = crawler.list_url_tpl+"ljdjjp_list/"+"index_%d.shtml"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

def yhdt_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url = crawler.list_url_tpl+"yhdt_list/"
            crawler.page_num+=1
            crawler.list_url_tpl = crawler.list_url_tpl+"yhdt_list/"+"index_%d.shtml"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url


b_class_dict = {
    "精评": {"url":"http://www.liejin99.com/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":jp_generate_next_list_url,"short_name":"jp", "pattern_type":"jp"},
    "观点": {"url":"http://www.liejin99.com/", "pub_date_format":u"%Y年%m月%d日  %H:%M","next_list_url_generator":gd_generate_next_list_url,"short_name":"gd", "pattern_type":"gd"},
    "央行动态": {"url":"http://www.liejin99.com/", "pub_date_format":u"%Y年%m月%d日  %H:%M","next_list_url_generator":yhdt_generate_next_list_url,"short_name":"yhdt", "pattern_type":"gd"},
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


