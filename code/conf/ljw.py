# -*- coding: utf-8 -*-
from .common import *
import re
website_name = "蓝鲸财经网"
website_short_name = "ljcjw"
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
        r'"title":"(?P<title>.*?)".*?"url":"(?P<url>.*?)".*?"time_week":"(?P<pub_date>.*?)\s',
        ],
        "news_patterns" : [
            r'<div class="article_title">(?P<title>.*?)<\/div>.*?<div class="article_content_wrap">(?P<content>.*?)<\/div>',
       ]
    },
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
            ret_url=crawler.list_url_tpl
            temp=crawler.get(ret_url,header=None)
            temp = temp.decode("gbk","ignore").encode("utf-8")
            source_pattern=re.compile('"last_time":((.|\n)*?)}')
            source_data=source_pattern.findall(temp)[-1]
            next_url = crawler.base_url+source_data[0]
            crawler.list_url_tpl = next_url
            yield ret_url

b_class_dict = {
    "TMT": {"url":"http://www.lanjinger.com/news/waterfall?type=7&last_time=", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"tmt", "pattern_type":"news"},
    "传媒": {"url":"http://www.lanjinger.com/news/waterfall?type=6&last_time=", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"cm", "pattern_type":"news"},
    "保险": {"url":"http://www.lanjinger.com/news/waterfall?type=18&last_time=", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"bx", "pattern_type":"news"},
    "教育": {"url":"http://www.lanjinger.com/news/waterfall?type=15&last_time=", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"jy", "pattern_type":"news"},
    "基金": {"url":"http://www.lanjinger.com/news/waterfall?type=12&last_time=", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"jj", "pattern_type":"news"},
    "银行": {"url":"http://www.lanjinger.com/news/waterfall?type=13&last_time=", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"yh", "pattern_type":"news"},
    "互联网金融": {"url":"http://www.lanjinger.com/news/waterfall?type=10&last_time=", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"hlwjr", "pattern_type":"news"},
    "产经": {"url":"http://www.lanjinger.com/news/waterfall?type=16&last_time=", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"cj", "pattern_type":"news"},
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


