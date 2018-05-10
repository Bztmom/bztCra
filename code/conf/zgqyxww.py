# -*- coding: utf-8 -*-
from .common import *

website_name = "中国企业新闻网"
website_short_name = "zgqyxww"
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
            r'<span class="vvv"><a href="(?P<url>.*?)"  target="_blank"  title="(?P<title>.*?)" >.*?日期：(?P<pub_date>.*?)<\/span>',
            ],
        "news_patterns" : [
            r'来源：(?P<source>.*?)<!--.*?<div class="ssevg">(?P<content>.*?)<div class="disclaimer">.*?\[责任编辑(?P<author>.*?)\]',
            r'来源：(?P<source>.*?)<!--.*?<div class="ssevg">(?P<content>.*?)<div class="wrrr">.*?<div class="segg">\[责任编辑：(?P<author>.*?)\]',
            r'来源：(?P<source>.*?)<!--.*?id="articlecon">(?P<content>.*?)<div class="wrrr">.*?<div class="segg">\[责任编辑：(?P<author>.*?)\]',
            r'发表时间：(?P<pub_date>.*?)  来源：(?P<source>.*?)<\/div.*?conBox".*?<\/center>(?P<content>.*?)<div',
           ]
    },
    "tpxw":{
        "list_patterns" : [
            r'<dl class="iikk"><dt><a href="(?P<url>.*?)" target="_black" class="autofill">.*?title="(?P<title>.*?)" >.*?<span>日期：(?P<pub_date>.*?)<\/span>',
            ],
        "news_patterns" : [
            r'来源：(?P<source>.*?)<\/div>.*?<div class="conBox">(?P<content>.*?)<div class="h20">',
           ]
    },
}


def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url=crawler.list_url_tpl
            crawler.page_num+=1
            crawler.list_url_tpl = crawler.list_url_tpl[:-9]+"page=%d"+crawler.list_url_tpl[-9:]
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

b_class_dict = {
    "财经产经": {"url":"http://www.gdcenn.cn/news_list.asp?ClassID=8","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"cjcj", "pattern_type":"news"},
    "时政热点": {"url":"http://www.gdcenn.cn/news_list.asp?ClassID=94","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"szrd", "pattern_type":"news"},
    "新闻联播": {"url":"http://www.gdcenn.cn/news_list.asp?ClassID=73","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"xwlb", "pattern_type":"news"},
    "热点话题": {"url":"http://www.gdcenn.cn/news_list.asp?ClassID=71","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"rdht", "pattern_type":"news"},
    "品牌中国": {"url":"http://www.gdcenn.cn/news_list.asp?ClassID=67","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"ppzg", "pattern_type":"news"},
    "港澳直通": {"url":"http://www.gdcenn.cn/news_list.asp?ClassID=68","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"gazt", "pattern_type":"news"},
    "图片新闻": {"url":"http://www.gdcenn.cn/news_list.asp?ClassID=81","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"tpxw", "pattern_type":"tpxw"},
    "企业纵深": {"url":"http://www.gdcenn.cn/news_list.asp?ClassID=44","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"qyzs", "pattern_type":"news"},
    "民生焦点": {"url":"http://www.gdcenn.cn/news_list.asp?ClassID=112","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"msjd", "pattern_type":"news"},
    "新闻调查": {"url":"http://www.gdcenn.cn/news_list.asp?ClassID=75","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"xwdc", "pattern_type":"news"},
    "创业就业": {"url":"http://www.gdcenn.cn/news_list.asp?ClassID=113","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"cyjy", "pattern_type":"news"},
    "企业发布": {"url":"http://www.gdcenn.cn/news_list.asp?ClassID=74","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"qyfb", "pattern_type":"news"},
    
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
                "base_url":"http://www.gdcenn.cn/",
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


