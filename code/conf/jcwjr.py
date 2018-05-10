# -*- coding: utf-8 -*-
from .common import *

website_name = "荆楚网金融"
website_short_name = "jcwjr"
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
            r"<li><a href='(?P<url>.*?)' title=(?P<title>.*?)>.*?<\/a><span>(.*?)<\/span><\/li>"
        ],
        "news_patterns" : [
            r'发布时间：(?P<pub_date>.*?)<\/span><span>来源：<span id="source_baidu">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class=TRS_Editor>(?P<content>.*?)<div class="pageControl">.*?编辑：<span class="editor_baidu">(?P<author>.*?)<\/span>',
       ]
    },
    "yh":{
        "list_patterns" : [
            r'<h2><a target="_blank" href="(?P<url>.*?)">(?P<title>.*?)<\/a><\/h2>.*?<div class="p2">(?P<pub_date>.*?)<\/div>'
        ],
        "news_patterns" : [
            r'来源：(?P<source>.*?)<\/p>.*?<div class=TRS_Editor>(?P<content>.*?)<div class="wzy_ewm">',
       ]
    },
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url=crawler.list_url_tpl
            crawler.list_url_tpl = crawler.list_url_tpl+"index_%d.shtml"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url


b_class_dict = {
    "经济新闻": {"url":"http://news.cnhubei.com/xw/jj/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"jjxw", "pattern_type":"news"},
    "银行": {"url":"http://jr.cnhubei.com/yh/", "pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"yh", "pattern_type":"yh"},
    "证券": {"url":"http://jr.cnhubei.com/zq/", "pub_date_format":"%Y-%m-%d", "ckpt_days":300,"next_list_url_generator":default_generate_next_list_url,"short_name":"zq", "pattern_type":"yh"},
    "理财": {"url":"http://jr.cnhubei.com/lc/", "pub_date_format":"%Y-%m-%d", "ckpt_days":300,"next_list_url_generator":default_generate_next_list_url,"short_name":"lc", "pattern_type":"yh"},
    "互联网金融": {"url":"http://jr.cnhubei.com/hlwjr/","ckpt_days":300, "pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"hlwjr", "pattern_type":"yh"},
    "金融大咖秀": {"url":"http://jr.cnhubei.com/jrdkx/", "ckpt_days":300,"pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"jrdkx", "pattern_type":"yh"},
    "保险": {"url":"http://jr.cnhubei.com/bx/", "pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"bx", "pattern_type":"yh"},
    "创富宝典": {"url":"http://jr.cnhubei.com/cfbd/", "ckpt_days":300,"pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"cfbd", "pattern_type":"yh"},
    "头条新闻": {"url":"http://jr.cnhubei.com/ttxw/", "pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"ttxw", "pattern_type":"yh"},
    
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
        "uploader":online_mysql_uploader_conf
    }
    #print pipeline_conf
    conf["pipelines"].append(pipeline_conf)


