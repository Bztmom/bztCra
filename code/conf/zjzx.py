# -*- coding: utf-8 -*-
from .common import *

website_name = "中金在线"
website_short_name = "zjzx"
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
            r'"Thumb2":"(.*?)","Title":"(?P<title>.*?)","Url":"(?P<url>.*?)",'
        ],
        "news_patterns" : [
            r'<h3 class="artTitle">(?P<title>.*?)<\/h3>.*?<div class="artDes">.*?<span>(?P<pub_date>.*?)<\/span>.*?<span>来源:(?P<source>.*?)<\/span>.*?<span>作者:(?P<author>.*?)<\/span>.*?<div class="Article">(?P<content>.*?)<!--.*? start-->',
            r'<h1 id="Title">(?P<title>.*?)<\/h1>.*?来源：(<span.*?>)?(<a.*?>)?(?P<source>.*?)(<\/span>)?(<\/a>)?\s+.*?(<.*?>)?\s+.*?(<.*?>)?\s+.*?<\/span>.*?<span  id="author_baidu">作者：(?P<author>.*?)<\/span>.*?<span  id="pubtime_baidu">(?P<pub_date>.*?)<\/span>.*?id="Content">(?P<content>.*?)<!--<span id="editor_baidu"',
            r'来源：<.*?><.*?>(?P<source>.*?)<\/sp.*?author_baidu">作者：<span.*?>(?P<author>.*?)<\/.*?pubtime_baidu"><span class="Mr10">(?P<pub_date>.*?)<\/spa.*?__content">(?P<content>.*?)<\/div',
           ]
    },
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 3:
        if crawler.page_num == 0:
            crawler.page_num+=1
            ret_url=crawler.list_url_tpl
            crawler.list_url_tpl = crawler.list_url_tpl[:-1]+"%d"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url


b_class_dict = {
    "财经-国内财经": {"url":"http://app.cnfol.com/test/newlist_api.php?catid=1277&page=1", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"gncj", "pattern_type":"news"},
    "财经-证券要闻": {"url":"http://app.cnfol.com/test/newlist_api.php?catid=1591&page=1", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"zqyw", "pattern_type":"news"},
    "财经-国际财经": {"url":"http://app.cnfol.com/test/newlist_api.php?catid=1278&page=1", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"gjcj", "pattern_type":"news"},
    "财经-产业经济": {"url":"http://app.cnfol.com/test/newlist_api.php?catid=1280&page=1", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"cyjj", "pattern_type":"news"},
    "财经-商业要闻": {"url":"http://app.cnfol.com/test/newlist_api.php?catid=1609&page=1", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"syyw", "pattern_type":"news"},
    "财经-IT": {"url":"http://app.cnfol.com/test/newlist_api.php?catid=1587&page=1", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"it", "pattern_type":"news"},
    "财经-消费": {"url":"http://app.cnfol.com/test/newlist_api.php?catid=1603&page=1", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"xf", "pattern_type":"news"},
    "财经-会议活动": {"url":"http://app.cnfol.com/test/newlist_api.php?catid=1589&page=1", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"hyhd", "pattern_type":"news"},
    "财经-观点评论": {"url":"http://app.cnfol.com/test/newlist_api.php?catid=4043&page=1", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"gdpl", "pattern_type":"news"},
    "股市-股市直播": {"url":"http://app.cnfol.com/test/newlist_api.php?catid=1325&page=1", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"gszb", "pattern_type":"news"},
    "市场-个股资讯": {"url":"http://app.cnfol.com/test/newlist_api.php?catid=4035&page=1", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"ggzx", "pattern_type":"news"},
    "新股-新股要闻": {"url":"http://app.cnfol.com/test/newlist_api.php?catid=1310&page=1", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"xgyw", "pattern_type":"news"},
    "新三板要闻": {"url":"http://app.cnfol.com/test/newlist_api.php?catid=1344&page=1", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"xsbyw", "pattern_type":"news"},
    "新三板公司动态": {"url":"http://app.cnfol.com/test/newlist_api.php?catid=3769&page=1", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"xsbgsdt", "pattern_type":"news"},
    "市场-交易所公告": {"url":"http://app.cnfol.com/test/newlist_api.php?catid=1776&page=1", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"jys", "pattern_type":"news"},

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


