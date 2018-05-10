 # -*- coding: utf-8 -*-
from .common import *

website_name = "央视证券"
website_short_name = "yszq"
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
            '<dt><a href=\".*?\" target=\"_blank\" title=\".*?\"><mark>.*?<a href=\"(?P<url>.*?)\" target=\"_blank\" title=\"(?P<title>.*?)\">.*?<\/a>.*?发布时间：(?P<pub_date>.*?)<\/span>'
        ],
        "news_patterns" : [
            r'<section class=\"artcon\">.*?<li class=.*?<\/li>.*?<li.*?>来源：(?P<source>.*?)<\/li>.*?<section class=\"li_artcon_info_txt\">(?P<content>.*?)<\/section>.*?<\/section>'
        ]
    }
}

b_class_dict = {
    "最新": {"url":"http://www.cctvfinance.com/caijing/list_12_", "short_name":"zx", "pattern_type":"news"},
    "宏观策略": {"url":"http://www.cctvfinance.com/macro/list_13_", "short_name":"hgcl", "pattern_type":"news"},
    "政策解读": {"url":"http://www.cctvfinance.com/zcjd/list_14_", "short_name":"zcjd", "pattern_type":"news"},
    "独家快讯": {"url":"http://www.cctvfinance.com/djkx/list_16_", "short_name":"djkx", "pattern_type":"news"},
    "国内财经": {"url":"http://www.cctvfinance.com/gncj/list_21_", "short_name":"gncj", "pattern_type":"news"},
    "国际财经": {"url":"http://www.cctvfinance.com/gjcj/list_22_", "short_name":"gjcj", "pattern_type":"news"},
    "生活消费": {"url":"http://www.cctvfinance.com/life/list_24_", "short_name":"shxf", "pattern_type":"news"},
    "企业新闻": {"url":"http://www.cctvfinance.com/news/list_126_", "short_name":"qyxw", "pattern_type":"news"},
    "股票-公司解析": {"url":"http://www.cctvfinance.com/gsjx/list_29_", "short_name":"gp-gsjx", "pattern_type":"news"},
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            crawler.page_num+=1
            crawler.list_url_tpl = crawler.list_url_tpl+"%d.html"
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            crawler.page_num += 1
            yield ret_url

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
                "pub_date_format":"%Y-%m-%d",
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


