# -*- coding: utf-8 -*-
from .common import *

website_name = "凤凰网财经"
website_short_name = "fhwcj"
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
            r'<p class="text"><a href="(?P<url>.*?)" target="_blank" title="">(?P<title>.*?)<\/a><\/p>.*?<p class="time">(.*?)<span>'
        ],
        "news_patterns" : [
            r'<span itemprop="datePublished" class="ss01">(?P<pub_date>.*?)<\/span>.*?<span itemprop="name" class="ss03">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--161104a begin-->',
            r'<span itemprop="datePublished" class="ss01">(?P<pub_date>.*?)<\/span>.*?<span itemprop="name" class="ss03">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--mainContent end-->',
            r'<span itemprop="datePublished" class="ss01">(?P<pub_date>.*?)<\/span>.*?<span itemprop="name" class="ss03">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--mainContent end-->',
            r'<span itemprop="datePublished" class="ss01">(?P<pub_date>.*?)<\/span>.*?ss03 weMediaicon">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--161104a begin-->.*?<p class="iphone_none">',
            r'<span itemprop="datePublished" class="ss01">(?P<pub_date>.*?)<\/span>.*?<span itemprop="name" class="ss03">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--161104a begin-->'
        ]
    },
    "qq":{
        "list_patterns" : [
            r'<h2> <a class="js_url" href="(?P<url>.*?)" target="_blank">(?P<title>.*?)<\/a> <\/h2>.*?<a>(?P<pub_date>.*?)<\/a>'
        ],
        "news_patterns" : [
            r'<span itemprop="datePublished" class="ss01">(.*?)<\/span>.*?<span itemprop="name" class="ss03">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--161104a begin-->.*?<p class="iphone_none">',
            r'<span itemprop="datePublished" class="ss01">(.*?)<\/span>.*?<span itemprop="name" class="ss03">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--mainContent end-->.*?<p class="iphone_none">',
            r'<span itemprop="datePublished" class="ss01">(.*?)<\/span>.*?<span itemprop="name" class="ss03">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--mainContent end-->',
            r'ss03 weMediaicon">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--161104a begin-->.*?<p class="iphone_none">',
            r'<span itemprop="datePublished" class="ss01">(.*?)<\/span>.*?<span itemprop="name" class="ss03">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--161104a begin-->'
        ]
    },
    "ssgs":{
        "list_patterns" : [
            r'<li><span class="txt01"><a  href="(?P<url>.*?)" target="_blank">(?P<title>.*?)<\/a><\/span><span class="time01">(?P<pub_date>.*?)<\/span><\/li>'
        ],
        "news_patterns" : [
            r'<span itemprop="datePublished" class="ss01">(.*?)<\/span>.*?<span itemprop="name" class="ss03">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--161104a begin-->.*?<p class="iphone_none">',
            r'<span itemprop="datePublished" class="ss01">(.*?)<\/span>.*?<span itemprop="name" class="ss03">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--mainContent end-->.*?<p class="iphone_none">',
            r'<span itemprop="datePublished" class="ss01">(.*?)<\/span>.*?<span itemprop="name" class="ss03">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--mainContent end-->',
            r'ss03 weMediaicon">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--161104a begin-->.*?<p class="iphone_none">',
            r'<span itemprop="datePublished" class="ss01">(.*?)<\/span>.*?<span itemprop="name" class="ss03">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--161104a begin-->'
        ]
    },
    "yc":{
        "list_patterns" : [
            r'<div class="Function"> <span>(?P<pub_date>.*?)<\/span>.*?href="(?P<url>.*?)".*?title="(?P<title>.*?)"'
        ],
        "news_patterns" : [
            r'<span itemprop="datePublished" class="ss01">(.*?)<\/span>.*?<span itemprop="name" class="ss03">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--161104a begin-->.*?<p class="iphone_none">',
            r'<span itemprop="datePublished" class="ss01">(.*?)<\/span>.*?<span itemprop="name" class="ss03">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--mainContent end-->.*?<p class="iphone_none">',
            r'<span itemprop="datePublished" class="ss01">(.*?)<\/span>.*?<span itemprop="name" class="ss03">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--mainContent end-->',
            r'ss03 weMediaicon">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--161104a begin-->.*?<p class="iphone_none">',
            r'<span itemprop="datePublished" class="ss01">(.*?)<\/span>.*?<span itemprop="name" class="ss03">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="bg_top"><span><\/span><\/div>(?P<content>.*?)<!--161104a begin-->'
        ]
    },
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 1:
        ret_url = crawler.list_url_tpl
        yield ret_url

def qq_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url = crawler.list_url_tpl
            crawler.page_num+=1
            crawler.list_url_tpl = crawler.list_url_tpl[:-18]+"%d"+crawler.list_url_tpl[-16:]
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

b_class_dict = {
    "首页": {"url":"http://finance.ifeng.com/", "pub_date_format":["%Y-%m-%d %H:%M:%S","%Y年%m月%d日 %H:%M:%S"],"next_list_url_generator":default_generate_next_list_url,"short_name":"sy", "pattern_type":"news"},
    "全球财经快报": {"url":"http://finance.ifeng.com/listpage/1/marketlist.shtml", "pub_date_format":["%Y-%m-%d %H:%M","%Y-%m-%d %H：%M"],"next_list_url_generator":qq_generate_next_list_url,"short_name":"qqcjkx", "pattern_type":"qq"},
    "上市公司": {"url":"http://finance.ifeng.com/listpage/111/1/list.shtml", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"ssgs", "pattern_type":"ssgs"},
    "凤凰科技-原创": {"url":"http://tech.ifeng.com/listpage/3539/1/list.shtml", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"kjyc", "pattern_type":"yc"},
    "凤凰科技-互联网": {"url":"http://tech.ifeng.com/listpage/803/1/list.shtml", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"hlw", "pattern_type":"yc"},
    "证券要闻": {"url":"http://finance.ifeng.com/listpage/110/1/list.shtml", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"zqyw", "pattern_type":"ssgs"},

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


