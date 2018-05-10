# -*- coding: utf-8 -*-
from .common import *

website_name = "中国证券网"
website_short_name = "zgzqw"
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
            '<li><span class=\"time\">\[(?P<pub_date>.*?)\]<\/span> <a href=\"(?P<url>.*?)\" target=\"_blank\" title=\"(?P<title>.*?)\">.*?<\/a><\/li>'
        ],
        "news_patterns" : [
            '<span class=\"source\">来源：(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<span class=\"author\">作者：(?P<author>.*?)<\/span>.*?id=\"qmt_content_div\">(?P<content>.*?)<input type=\"hidden\"',
        ]
    },
    "cjbk":{
        "list_patterns":[
            '<li><span class=\"time\">(?P<pub_date>.*?)<\/span><a target=\"_blank\" href=\"(?P<url>.*?)\">(?P<title>.*?)<\/a><\/li>'
        ],
        "news_patterns":[
            # '<div class=\"title\">(?P<content>.*?)<\/STRONG><\/SPAN><\/P><\/div>',
            '<div class=\"title\">(?P<content>.*?)<div class=\"comtime\">'
        ]
    },
    "ztc":{
        "list_patterns":[
            '<strong class=\"user-name\">.*?<font color=\".*?\">(?P<author>.*?)<\/font> <font.*?<\/font> <a href=\"(.*?)\" target=\"_blank\">(.*?)<\/a>.*?<\/strong>.*?<div class=\"msg-con\"><a href=\"(?P<url>.*?)\" target=\"_blank\">(?P<title>.*?)<\/a><\/div>.*?<p class=\"msg-time\">(.*?)<\/p>'
        ],
        "news_patterns":[
            '<li class=\"answer-list\">.*?<strong class=\"user-name\">.*?target="_blank">(.*?)<\/a>.*?<\/strong>.*?<div class=\"msg-con\">(?P<content>.*?)<div class=\"msg-extra fn-clear\">.*?<p class=\"msg-time\">(?P<pub_date>.*?)<\/p>.*?<div class=\"sns-box\">'
        ]
    },
    "boke":{
        "list_patterns":[
            '<li><h2><a target=\"_blank\" href=\"(?P<url>.*?)\">(?P<title>.*?)<\/a><\/h2><p class=\"des\">(.*?)<\/p><\/li>'
        ],
        "news_patterns":[
            '<div class=\"logtext\">(?P<content>.*?)<div class=\"comtime\">.*?<\/script>(?P<pub_date>.*?)<\/div><script',
            '<div class=\"ll-time\">(?P<pub_date>.*?)<\/div>.*?<div class=\"logtext\">(?P<content>.*?)<div class=\"comtime\"><div class=\"ll_control\">'
        ]
    },
    "szkx":{
        "list_patterns":[
            '"title":"(?P<title>.*?)".*?"link":"(?P<url>.*?)".*?"time":"(?P<pub_date>.*?)"'
        ],
        "news_patterns":[
            '<div class=\"main-content text-large\" id=\"pager-content\">.*?<h1 class=\"title\">(?P<title>.*?)<\/h1>.*?<span class=\"timer\">(?P<pub_date>.*?)<\/span>.*?<span class=\"source\">来源：(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<span class=\"author\">作者：(?P<author>.*?)<\/span>.*?id=\"qmt_content_div\">(?P<content>.*?)<input type=\"hidden\"'
        ]
    },
    "ggkx":{
        "list_patterns" : [
            '<span class=\"time\">(?P<pub_date>.*?)<\/span><a href=\"(?P<url>.*?)\" target=\"_blank\" title=\"(?P<title>.*?)\">.*?<\/a><\/i>'
        ],
        "news_patterns" : [
            '<span class=\"source\">来源：(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<span class=\"author\">作者：(?P<author>.*?)<\/span>.*?id=\"qmt_content_div\">(?P<content>.*?)<input type=\"hidden\"',
        ]
    },
    "ggjj":{
        "list_patterns" : [
            '<span class=\"time\">(?P<pub_date>.*?)<\/span> <a href=\"(?P<url>.*?)\" target=\"_blank\" title=\"(?P<title>.*?)\">.*?<\/a><\/li>'
        ],
        "news_patterns" : [
            '<span class=\"source\">来源：(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<span class=\"author\">作者：(?P<author>.*?)<\/span>.*?id=\"qmt_content_div\">(?P<content>.*?)<input type=\"hidden\"',
        ]
    },
    "bwdj":{
        "list_patterns" : [
            r'<span class="time">.*?<\/span><a href="(?P<url>.*?)" target="_blank" title="(?P<title>.*?)">'
        ],
        "news_patterns" : [
            'span class="timer">(?P<pub_date>.*?)<\/sp.*?"source">来源：(?P<source>.*?)<\/span.*?作者：(?P<author>.*?)<\/spa.*?class="content".*?>(?P<content>.*?)<\/div>',
        ]
    },
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url = crawler.list_url_tpl
            crawler.page_num+=1
            crawler.list_url_tpl += "%d"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

def szkx_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url = crawler.list_url_tpl+"&page=1"
            crawler.page_num=2
            crawler.list_url_tpl += "&page=%d"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

b_class_dict = {
    "要闻": {"url":"http://news.cnstock.com/news/sns_yw/", "next_list_url_generator":default_generate_next_list_url,"short_name":"yw", "pub_date_format":"%Y-%m-%d %H:%M","pattern_type":"news"},
    "券页": {"url":"http://news.cnstock.com/news/sns_qy/", "next_list_url_generator":default_generate_next_list_url,"short_name":"qy", "pub_date_format":"%Y-%m-%d %H:%M","pattern_type":"news"},
    "机构": {"url":"http://news.cnstock.com/news/sns_jg/","next_list_url_generator":default_generate_next_list_url,"short_name":"jg","pub_date_format":"%Y-%m-%d %H:%M", "pattern_type":"news"},
    "资讯库": {"url":"http://news.cnstock.com/news/sns_zxk/", "next_list_url_generator":default_generate_next_list_url,"short_name":"zxk","pub_date_format":"%Y-%m-%d %H:%M", "pattern_type":"news"},
    "热点机会": {"url":"http://stock.cnstock.com/stock/smk_rdyj/", "next_list_url_generator":default_generate_next_list_url,"short_name":"rdjh","pub_date_format":"%m-%d %H:%M", "pattern_type":"news"},
    "政策动态": {"url":"http://stock.cnstock.com/xg/sx_zcdt/","next_list_url_generator":default_generate_next_list_url, "short_name":"zcdt", "pub_date_format":"%m-%d %H:%M","pattern_type":"news"},
    "IPO评论": {"url":"http://stock.cnstock.com/xg/sx_ipopl/","next_list_url_generator":default_generate_next_list_url, "short_name":"IPO", "pub_date_format":"%m-%d %H:%M","pattern_type":"news"},
    "上证快讯": {"url":"http://app.cnstock.com/api/xcx/kx?colunm=szkx&num=15","next_list_url_generator":szkx_generate_next_list_url, "short_name":"szkx","pub_date_format":"%Y-%m-%d %H:%M:%S","pattern_type":"szkx"},
    "公告快讯": {"url":"http://ggjd.cnstock.com/gglist/search/ggkx", "next_list_url_generator":default_generate_next_list_url,"short_name":"ggkx","pub_date_format":"%m-%d %H:%M", "pattern_type":"ggkx"},
    "上市公司-公告集锦": {"url":"http://ggjd.cnstock.com/company/scp_ggjd/tjd_ggjj", "next_list_url_generator":default_generate_next_list_url,"short_name":"ssgs-ggjj", "pub_date_format":"%Y-%m-%d","pattern_type":"ggjj"},
    "上市公司-公司聚焦": {"url":"http://company.cnstock.com/company/scp_gsxw", "next_list_url_generator":default_generate_next_list_url,"short_name":"ssgs-gsjj", "pub_date_format":"%Y-%m-%d","pattern_type":"ggjj"},
    "上市公司-本网独家": {"url":"http://ggjd.cnstock.com/gglist/search/qmtbbdj", "next_list_url_generator":default_generate_next_list_url,"short_name":"ssgs-bwdj", "pub_date_format":"%Y-%m-%d %H:%M:%S","pattern_type":"bwdj"},

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
                "list_patterns": pattern_conf[info["pattern_type"]]["list_patterns"] if "pattern_type" in info else [],
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
                    "detail_patterns": pattern_conf[info["pattern_type"]]["news_patterns"]  if "pattern_type" in info else []
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


