# -*- coding: utf-8 -*-
from .common import *

website_name = "大众网财经"
website_short_name = "dzwcj"
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
            r'<h3><a href="(?P<url>.*?)".*?>(?P<title>[^<]*?)<\/a><span>(?P<pub_date>.*?)<\/span><\/h3>'
        ],
        "news_patterns" : [
            '<!--fabutime-->(.*?)<!--\/fabutime-->.*?<!--laiyuan-->(<a.*?>)?(?P<source>.*?)(<\/a>)?<!--\/laiyuan-->.*?<!--zuozhe-->(?P<author>.*?)<!--\/zuozhe-->.*?<!--zhengwen-->(?P<content>.*?)<!--\/zhengwen-->',
        ]
    },
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url=crawler.list_url_tpl
            crawler.list_url_tpl = crawler.list_url_tpl+"default%d.htm"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

b_class_dict = {
    "钱沿热点": {"url":"http://finance.dzwww.com/jiaodian/zxbb/", "pub_date_format":u"%m月%d日","next_list_url_generator":default_generate_next_list_url,"short_name":"qyrd", "pattern_type":"news"},
    "大众财眼": {"url":"http://finance.dzwww.com/jiaodian/jrtt/", "pub_date_format":u"%m月%d日", "next_list_url_generator":default_generate_next_list_url,"short_name":"dzcy", "pattern_type":"news"},
    "财经舆情": {"url":"http://finance.dzwww.com/cjyl/","pub_date_format":u"%m月%d日", "next_list_url_generator":default_generate_next_list_url,"short_name":"cjyq", "pattern_type":"news"},
    "投资-投基有道": {"url":"http://finance.dzwww.com/tz/tjyd/", "pub_date_format":u"%m月%d日","next_list_url_generator":default_generate_next_list_url,"short_name":"tjyd", "pattern_type":"news"},
    "股市-机构论市": {"url":"http://finance.dzwww.com/gs/jgls/", "pub_date_format":u"%m月%d日", "next_list_url_generator":default_generate_next_list_url,"short_name":"jgls", "pattern_type":"news"},
    "股市-证券新闻": {"url":"http://finance.dzwww.com/gs/zqxw/","pub_date_format":u"%m月%d日", "next_list_url_generator":default_generate_next_list_url,"short_name":"zqxw", "pattern_type":"news"},
    "投资-企业快讯": {"url":"http://finance.dzwww.com/tz/zjby/", "pub_date_format":u"%m月%d日", "next_list_url_generator":default_generate_next_list_url,"short_name":"qykx", "pattern_type":"news"},
    "股市-板块动态": {"url":"http://finance.dzwww.com/gs/ssjp/","pub_date_format":u"%m月%d日", "next_list_url_generator":default_generate_next_list_url,"short_name":"bkdt", "pattern_type":"news"},
    "投资-外汇期货": {"url":"http://finance.dzwww.com/tz/whqh/", "pub_date_format":u"%m月%d日","next_list_url_generator":default_generate_next_list_url,"short_name":"whqh", "pattern_type":"news"},
    "保险-行业动态": {"url":"http://finance.dzwww.com/baoxian/bxzx/", "pub_date_format":u"%m月%d日", "next_list_url_generator":default_generate_next_list_url,"short_name":"hydt", "pattern_type":"news"},
    "保险-公司新闻": {"url":"http://finance.dzwww.com/baoxian/sdbx/","pub_date_format":u"%m月%d日", "next_list_url_generator":default_generate_next_list_url,"short_name":"gsxw", "pattern_type":"news"},
    "保险-百宝箱": {"url":"http://finance.dzwww.com/baoxian/bxxp/", "pub_date_format":u"%m月%d日","next_list_url_generator":default_generate_next_list_url,"short_name":"bbx", "pattern_type":"news"},
    "保险-政策监管": {"url":"http://finance.dzwww.com/baoxian/jgdt/", "pub_date_format":u"%m月%d日", "next_list_url_generator":default_generate_next_list_url,"short_name":"zcjg", "pattern_type":"news"},
    "保险-保险人物": {"url":"http://finance.dzwww.com/baoxian/bxrw/", "pub_date_format":u"%m月%d日", "next_list_url_generator":default_generate_next_list_url,"short_name":"bxrw", "pattern_type":"news"},
    "银行-银行新闻": {"url":"http://finance.dzwww.com/yinhang/yhxw/","pub_date_format":u"%m月%d日", "next_list_url_generator":default_generate_next_list_url,"short_name":"yhxw", "pattern_type":"news"},
    "银行-理财超市": {"url":"http://finance.dzwww.com/yinhang/lccs/", "pub_date_format":u"%m月%d日","next_list_url_generator":default_generate_next_list_url,"short_name":"lccs", "pattern_type":"news"},
    "互动-理财维权": {"url":"http://finance.dzwww.com/lcwq/", "pub_date_format":u"%m月%d日", "next_list_url_generator":default_generate_next_list_url,"short_name":"lcwq", "pattern_type":"news"},
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


