# -*- coding: utf-8 -*-
from .common import *

website_name = "和讯网"
website_short_name = "hxw"
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
            r'"entityurl":"(?P<url>.*?)".*?"title":"(?P<title>.*?)"',
            r'title:\'(?P<title>.*?)\'.*?titleLink:\'(?P<url>.*?)\'',
        ],
        "news_patterns" : [
            r'<span class=\"pr20\">(?P<pub_date>.*?)<\/span>.*?nofollow\">(?P<source>.*?)<\/a>.*?<div class=\"art_contextBox\">(?P<content>.*?)\（责任编辑：(?P<author>.*?)\）<\/div>',
            r'<span class=\"pr20\">(?P<pub_date>.*?)<\/span>(?P<source>.*?)<\/div>.*?<div class=\"art_contextBox\">(?P<content>.*?)\（责任编辑：(?P<author>.*?)\）<\/div>',
        
        ]
    },
    "gpxw":{
        "list_patterns" : [
            r'<li><span class="sgd01"><div class="sgd02">.*?\'(?P<url>.*?)\'.*?>(?P<title>.*?)<\/a'
        ],
        "news_patterns" : [
            r'<span class=\"pr20\">(?P<pub_date>.*?)<\/span>.*?nofollow\">(?P<source>.*?)<\/a>.*?<div class=\"art_contextBox\">(?P<content>.*?)\（责任编辑：(?P<author>.*?)\）<\/div>',
            r'<span class=\"pr20\">(?P<pub_date>.*?)<\/span>(?P<source>.*?)<\/div>.*?<div class=\"art_contextBox\">(?P<content>.*?)\（责任编辑：(?P<author>.*?)\）<\/div>',

        ]
    },
}

default_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Host": "roll.hexun.com",
}
news_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Host": "tech.hexun.com",
}

def default_list_url(crawler):
    while crawler.page_num < 2:
        yield crawler.list_url_tpl
b_class_dict = {
    "和讯独家特稿": {"url":"http://open.tool.hexun.com/MongodbNewsService/data/getOriginalNewsList.jsp?id=187804274&s=30&cp=%d", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"djtg", "pattern_type":"news"},
    "国内经济": {"url":"http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=108511056&s=30&callback=&cp=%d", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"gnjj", "pattern_type":"news"},
    "产业报道": {"url":"http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=100018983&s=30&callback=&cp=%d", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"cybd", "pattern_type":"news"},
    "公司新闻": {"url":"http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=108511812&s=30&callback=&cp=%d", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"gsxw", "pattern_type":"news"},
    "国际经济": {"url":"http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=108511065&s=30&callback=&cp=%d", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"gjjj", "pattern_type":"news"},
    "宏观新闻": {"url":"http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=100018985&s=30&callback=&cp=%d", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"hgxw", "pattern_type":"news"},
    "股票-公司-公司要闻": {"url":"http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=100235849&s=30&cp=%d&priority=0&callback=hx_json11516095916063", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"gsyw", "pattern_type":"news"},
    "股票-独家-和讯股票观察": {"url":"http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=184571007&s=30&cp=%d&priority=0&callback=hx_json11516096285047", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"hxgpgc", "pattern_type":"news"},
    "房产-房产要闻": {"url":"http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=100135470&s=50&cp=%d&priority=0&callback=hx_json11524993090642", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"fdcyw", "pattern_type":"news"},
    "房产-深度": {"url":"http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=149394322&s=50&cp=%d&priority=0&callback=hx_json11524993090642", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"fdcsd", "pattern_type":"news"},
    "房产-房地产金融": {"url":"http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=123211837&s=50&cp=%d&priority=0&callback=hx_json11524993090642", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"fdcjr", "pattern_type":"news"},
    "科技": {"url":"http://roll.hexun.com/roolNews_listRool.action?type=all&ids=103&page=%d", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"kj", "pattern_type":"news", "header":default_header ,"news_header":news_header },
    "股票-新闻库": {"url":"http://stock.hexun.com/gpxwk/", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"gpxwk", "pattern_type":"gpxw","list_url_gen":default_list_url},

}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            crawler.page_num+=1;
        ret_url = crawler.list_url_tpl % (crawler.page_num)
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
                "list_patterns": pattern_conf[info["pattern_type"]]["list_patterns"] if "pattern_type" in info else [],
                "pub_date_format":info["pub_date_format"],
                "next_list_url_generator":info.get("list_url_gen", default_generate_next_list_url) ,
                "header":info.get("header", None),
                "news_header":info.get("news_header",None)
                #"log_filename": "./test.log"
            }
        },
        "transformers": [
            {
                "name": "XX_Crawler.XXProcessors.DetailNewsContentParser"  if "parser" not in info else info["parser"],
                "params": {
                    "detail_patterns": pattern_conf[info["pattern_type"]]["news_patterns"]  if "pattern_type" in info else []
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


