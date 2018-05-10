# -*- coding: utf-8 -*-
from .common import *

website_name = "证券时报网"
website_short_name = "zqsb"
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
            '<p class=\"tit\"><a href=\"(?P<url>.*?)\" target=\"_blank\" title=\"(?P<title>.*?)\">(.*?)<\/a><span>\[(?P<pub_date>.*?)\]<\/span><\/p>'
        ],
        "news_patterns" : [
            '<div class=\"intal_tit\">.*?<h2>(?P<title>.*?)<\/h2>.*?<div class=\"info\">(.*?)来源：(<a.*?>)?(<\/a>)?(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/div>.*?<div class=\"txt_con\" id=\"ctrlfscont\">(?P<content>.*?)<div class=\"adv\"',
            '<div class=\"intal_tit\">.*?<h2>(?P<title>.*?)<\/h2>.*?<div class=\"info\">(.*?)来源：(<a.*?>)?(<\/a>)?(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/div>.*?<div class=\"txt_con\" id=\"ctrlfscont\">(?P<content>.*?)<!--',
            '<div class=\"intal_tit\">.*?<h2>(?P<title>.*?)<\/h2>.*?<div class=\"info\">((.*?)来源：(<a.*?>)?(<\/a>)?(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/div>)?.*?<div class=\"txt_con\" id=\"ctrlfscont\">(?P<content>.*?)<\/div',
        ]
    },
    "yqjj":{
        "list_patterns":[
            '<li><a href=\"(?P<url>http:\/\/yq.stcn.com\/20(.*?).shtml)\" target=\"_blank\">(?P<title>.*?)<\/a><span>(?P<pub_date>.*?)<\/span><\/li>'
        ],
        "news_patterns":[
            '<div class=\"content_tit\">.*?<h2>(?P<title>.*?)<\/h2>.*?(<p>)?来源：(<a.*?>)?(<\/a>)?(<a.*?>)?(?P<source>.*?)(<\/a>)?作者：(?P<author>.*?)<span>(.*?)<\/span>.*?id=\"ctrlfscont\">(?P<content>.*?)<div class=\"txt_ft\">',
            '<div class=\"content_tit\">.*?<h2>(?P<title>.*?)<\/h2>.*?<p>来源：(<a.*?>)?(<\/a>)?(<a.*?>)?(?P<source>.*?)(<\/a>)?<span>(.*?)<\/span>.*?id=\"ctrlfscont\">(?P<content>.*?)<div class=\"txt_ft\">',
            '<div class=\"content_tit\">.*?<h2>(?P<title>.*?)<\/h2>.*?<span>(.*?)<\/span>.*?id=\"ctrlfscont\">(?P<content>.*?)<div class=\"txt_ft\">',
            r'<div class="vote-main">(?P<content>.*?)<!-- @end 挂件-投票 -->',
        ]
    },
    "48xsrqb":{
        "list_patterns":[
            '<li><label class=\"ph.*?<a href=\"(?P<url>http:\/\/kuaixun.stcn.com\/(.*?)shtml)\" target=\"_blank\" title=\"(?P<title>.*?)\">(.*?)<\/a><\/li>'
        ],
        "news_patterns":[
            '<div class=\"content_tit\">.*?<h2>(?P<title>.*?)<\/h2>.*?来源：(<a.*?>)?(<\/a>)?(<a.*?>)?(?P<source>.*?)(<\/a>)?作者：(?P<author>.*?)<span>(.*?)<\/span>.*?id=\"ctrlfscont\">(?P<content>.*?)<div class=\"txt_ft\">',
            '<div class=\"content_tit\">.*?<h2>(?P<title>.*?)<\/h2>.*?<span>(.*?)<\/span>.*?id=\"ctrlfscont\">(?P<content>.*?)<div class=\"txt_ft\">',
            '<div class=\"content_tit\">.*?<h2>(?P<title>.*?)<\/h2>.*?<p>来源：(<a.*?>)?(<\/a>)?(<a.*?>)?(?P<source>.*?)(<\/a>)?<span>(.*?)<\/span>.*?id=\"ctrlfscont\">(?P<content>.*?)<div class=\"txt_ft\">',
        ]
    },
    "yq":{
        "list_patterns":[
            '<li><a href=\"(?P<url>http:\/\/yq.stcn.com\/20(.*?).shtml)\" target=\"_blank\">(?P<title>.*?)<\/a><span>(?P<pub_date>.*?)<\/span><\/li>'
        ],
        "news_patterns":[
            '<div class=\"content_tit\">.*?<h2>(?P<title>.*?)<\/h2>.*?来源：(<a.*?>)?(<\/a>)?(<a.*?>)?(?P<source>.*?)(<\/a>)?作者：(?P<author>.*?)<span>(.*?)<\/span>.*?id=\"ctrlfscont\">(?P<content>.*?)<div class=\"txt_ft\">',
            '<div class=\"content_tit\">.*?<h2>(?P<title>.*?)<\/h2>.*?<p>来源：(<a.*?>)?(<\/a>)?(<a.*?>)?(?P<source>.*?)(<\/a>)?<span>(.*?)<\/span>.*?id=\"ctrlfscont\">(?P<content>.*?)<div class=\"txt_ft\">',
        ]
    },
    "kuaixun":{
        "list_patterns" : [
            '<li><p class=\"tit\"><a (.*?)<a href=\"(?P<url>.*?)\" target=\"_blank\">(?P<title>.*?)<\/a><span>\[(?P<pub_date>.*?)\]<\/span><\/p><\/li>'#快讯
        ],
        "news_patterns" : [
            '<div class=\"intal_tit\">.*?<h2>(?P<title>.*?)<\/h2>.*?<div class=\"info\">(.*?)来源：(<a.*?>)?(<\/a>)?(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/div>.*?<div class=\"txt_con\" id=\"ctrlfscont\">(?P<content>.*?)<div class=\"adv\"',
            '<div class=\"intal_tit\">.*?<h2>(?P<title>.*?)<\/h2>.*?<div class=\"info\">(.*?)来源：(<a.*?>)?(<\/a>)?(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/div>.*?<div class=\"txt_con\" id=\"ctrlfscont\">(?P<content>.*?)<!--',
            '<div class=\"intal_tit\">.*?<h2>(?P<title>.*?)<\/h2>.*?<div class=\"info\">(.*?)来源：(<a.*?>)?(<\/a>)?(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/div>.*?<div class=\"txt_con\" id=\"ctrlfscont\">(?P<content>.*?)<\/div',
        ]
    },
     "gsyyb":{
        "list_patterns":[
            '<li>.*?<p class=\"tit\"><a href=\"(?P<url>.*?)\" target=\"_blank\" title=\"(?P<title>.*?)\">(.*?)<\/a><span>\[(?P<pub_date>.*?)\]<\/span><\/p>'
        ],
        "news_patterns":[
            '<div class=\"intal_tit\">.*?<h2>(?P<title>.*?)<\/h2>.*?<div class=\"info\">(.*?)来源：(<a.*?>)?(<\/a>)?(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/div>.*?<div class=\"txt_con\" id=\"ctrlfscont\">(?P<content>.*?)<div class=\"adv\"',
            '<div class=\"intal_tit\">.*?<h2>(?P<title>.*?)<\/h2>.*?<div class=\"info\">(.*?)来源：(<a.*?>)?(<\/a>)?(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/div>.*?<div class=\"txt_con\" id=\"ctrlfscont\">(?P<content>.*?)<!--',
            '<div class=\"intal_tit\">.*?<h2>(?P<title>.*?)<\/h2>.*?<div class=\"info\">(.*?)来源：(<a.*?>)?(<\/a>)?(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/div>.*?<div class=\"txt_con\" id=\"ctrlfscont\">(?P<content>.*?)<\/div',
        ]
    }
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            crawler.page_num +=1
            crawler.list_url_tpl += "%d.shtml"
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

def kx_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            crawler.page_num +=1
            ret_url = crawler.list_url_tpl
            crawler.list_url_tpl += "index_%d.shtml"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

def yb_generate_next_list_url(crawler):
    while crawler.page_num < 1:
            yield crawler.list_url_tpl

b_class_dict = {
    "研报": {"url":"http://kuaixun.stcn.com/list/kxyb.shtml","pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":kx_generate_next_list_url, "short_name":"yb", "pattern_type":"news"},
    "公司新闻": {"url":"http://company.stcn.com/gsxw/", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gsxw", "pattern_type":"news"},
    "产经新闻": {"url":"http://company.stcn.com/cjnews/","pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url, "short_name":"cjxw", "pattern_type":"news"},
    "保险": {"url":"http://finance.stcn.com/baoxian/", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"bx", "pattern_type":"news"},
    "舆情聚焦": {"url":"http://yq.stcn.com/yqjj/", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":kx_generate_next_list_url,"short_name":"yqjj", "pattern_type":"yqjj"},
    "舆情速览": {"url":"http://yq.stcn.com/yqsl/index.shtml", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":kx_generate_next_list_url,"short_name":"yqsl", "pattern_type":"yqjj"},
    "推荐": {"url":"http://yq.stcn.com/tjyd/index.shtml", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":kx_generate_next_list_url,"short_name":"tj", "pattern_type":"yqjj"},
    "榜单": {"url":"http://yq.stcn.com/bd/index.shtml", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":kx_generate_next_list_url,"short_name":"bd", "pattern_type":"yqjj"},
    "回应与澄清": {"url":"http://yq.stcn.com/hyycq/index.shtml","pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":kx_generate_next_list_url, "short_name":"hyycq", "pattern_type":"yqjj"},
    "IPO": {"url":"http://yq.stcn.com/Ijj/index.shtml","pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":kx_generate_next_list_url, "short_name":"IPO", "pattern_type":"yqjj"},
    "新三板": {"url":"http://yq.stcn.com/xsb/index.shtml", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":kx_generate_next_list_url,"short_name":"xsb", "pattern_type":"yqjj"},
    "中心动态": {"url":"http://yq.stcn.com/zxdt/index.shtml","pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":kx_generate_next_list_url, "short_name":"zxdt", "pattern_type":"yqjj"},
    "舆情": {"url":"http://yq.stcn.com/tt/index.shtml", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":kx_generate_next_list_url,"short_name":"yq", "pattern_type":"yq"},
    "快讯": {"url":"http://kuaixun.stcn.com/index.shtml","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":kx_generate_next_list_url, "short_name":"kx", "pattern_type":"kuaixun"},
    "公司与研报": {"url":"http://sanban.stcn.com/gsyyb/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":kx_generate_next_list_url,"short_name":"gsyyb", "pattern_type":"gsyyb"},
    "政策与市场": {"url":"http://sanban.stcn.com/zcysc/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":kx_generate_next_list_url,"short_name":"zcysc", "pattern_type":"gsyyb"},
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


