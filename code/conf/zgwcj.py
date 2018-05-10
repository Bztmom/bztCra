# -*- coding: utf-8 -*-
from .common import *

website_name = "中国网"
website_short_name = "zgwcj"
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
            r'<li><span>(?P<pub_date>\d{4}-\d{2}-\d{2} \d{2}:\d{2}(:\d{2})?)<\/span>\s{0,2}(\[.*?\])?\s{0,2}<a href="(?P<url>.*?)".*?>(?P<title>.*?)<\/a><\/li>'
        ],
        "news_patterns" : [
            r'<div class="wrap c top">.*?<span class="fl time2">\d{4}年\d{2}月\d{2}日\d{2}:\d{2}\s{2}\s{0,2}(<a.*?>)?(?P<source>.*?)(<\/a>)?\s{2}<em>(作者：)?(?P<author>.*?)<\/em>.*?<div class="navp c" id="fontzoom">(?P<content>.*?)<div class="fr bianj">\(责任编辑：(?P<editor>.*?)\)</div>',
        ]
    },
    "wyt":{
        "list_patterns":[
            r'<div class="toux">.*?<i>(?P<author>.*?)<\/i>.*?<h2 class="bshare-title">.*?<a href="(?P<url>.*?)".*?>(?P<title>.*?)<\/a>.*?<span class="newsdetail_left">.*?<i>(?P<pub_date>.*?)<\/i>'
        ],
        "news_patterns":[
            r'<div class="article_content">(?P<content>.*?)<div class="copyright">'
        ]
    }
}


b_class_dict = {
    #"原创": {"url":"http://app.finance.china.com.cn/news/my.php?cname=财经&p=%d", "short_name":"yc", "pattern_type":"news","list_url_gen":None},
    #"宏观": {"url":"http://app.finance.china.com.cn/news/column.php?cname=新闻&p=%d", "short_name":"hg", "pattern_type":"news","list_url_gen":None},
    #"房产": {"url":"http://app.finance.china.com.cn/news/my.php?cname=房产&p=%d", "short_name":"fc", "pattern_type":"news","list_url_gen":None},
    "滚动": {"url":"http://app.finance.china.com.cn/news/live.php?channel=财经&p=%d", "short_name":"gd", "pattern_type":"news","list_url_gen":None,"pub_date_format":"%Y-%m-%d %H:%M:%S"},
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url = crawler.list_url_tpl
            crawler.list_url_tpl += "index_%d.htm"
            yield ret_url
        else:
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


