# -*- coding: utf-8 -*-
from .common import *
from XX_Crawler.Utils import get
import re
website_name = "野马财经"
website_short_name = "ymcj"
data_path = "../data/"
ckpt_path = "../ckpt/"
log_path = "../log/"
default_ckpt_days = 50
default_log_level = "info"
default_url ="http://www.yemacaijing.com/index/more.html?"

conf = {
    "domain_name": website_name,
    "pipelines": [
    ]  # end of pipelines for a website
}  # end of config of a website

pattern_conf = {"news":{
        "list_patterns" : [
            r'"id":"(?P<url>.*?)".*?"intro":"(?P<title>.*?)".*?"username":"(?P<author>.*?)"'
        ],
        "news_patterns" : [
            r'<meta property="article:author" content="(?P<author>.*?)"\/>.*?<span>发布时间:(?P<pub_date>.*?)<\/span>.*?layui-elem-quote\">.*?<p>(?P<title>.*?)<\/p>.*?<!-- 正文 -->(?P<content>.*?)<div class="copyright">',
        ]
    }
}

YMCJ_Header = {
    "Referer":"http://www.yemacaijing.com/",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
    "Host":"www.yemacaijing.com"
}


b_class_dict = {
    "首页": {"url":"0","base_url":"http://www.yemacaijing.com/index/view/id/", "short_name":"sy", "header":YMCJ_Header, "pattern_type":"news"},
    "互联网金融": {"url":"1","base_url":"http://www.yemacaijing.com/index/view/id/", "short_name":"hlwjr", "header":YMCJ_Header, "pattern_type":"news"},
    "上市公司": {"url":"2","base_url":"http://www.yemacaijing.com/index/view/id/", "short_name":"ssgs", "header":YMCJ_Header, "pattern_type":"news"},
    "人物": {"url":"4","base_url":"http://www.yemacaijing.com/index/view/id/", "short_name":"rw", "header":YMCJ_Header, "pattern_type":"news"},
    "观点": {"url":"5","base_url":"http://www.yemacaijing.com/index/view/id/", "short_name":"gd", "header":YMCJ_Header, "pattern_type":"news"},
    "自媒体": {"url":"7","base_url":"http://www.yemacaijing.com/index/view/id/", "short_name":"zmt", "header":YMCJ_Header, "pattern_type":"news"},
}



def default_generate_next_list_url(crawler):
    while crawler.page_num < 3:
        crawler.post_body = {
            "page":crawler.page_num,
            "cid":crawler.list_url_tpl
        }
        yield default_url

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
                "pub_date_format":"%Y-%m-%d %H:%M:%S",
                "base_url": info["base_url"],
                "next_list_url_generator":info.get("list_url_gen", default_generate_next_list_url) ,
                "header":info.get("header", None),
                "is_post": True
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


