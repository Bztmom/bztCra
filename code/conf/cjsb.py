# -*- coding: utf-8 -*-
from .common import *

website_name = "长江商报"
website_short_name = "cjsb"
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
            '<div class=\'limain\'><a href=\'(?P<url>.*?)\'.*?title\'>(?P<title>.*?)<\/p><p class=\'pdate\'>(?P<pub_date>.*?)<\/p><p class=\'content\'>(.*?)<\/p>'
        ],
        "news_patterns" : [
            r'<h1>(?P<title>.*?)<\/h1>.*?<span id="source_baidu">来源：(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<\/script>(?P<content>.*?)责编：(?P<author>.*?)<\/p>',
       ]
    },
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url=crawler.list_url_tpl
            crawler.page_num+=1
            crawler.list_url_tpl = crawler.list_url_tpl+"%d.htm"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url   

b_class_dict = {
    "上市公司": {"url":"http://www.changjiangtimes.com/c/4378/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"ssgs", "pattern_type":"news"},
    "IPO观察": {"url":"http://www.changjiangtimes.com/c/4391/", "pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"ipo", "pattern_type":"news"},
    "公司调查": {"url":"http://www.changjiangtimes.com/c/4377/","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"gsdc", "pattern_type":"news"},
    "车市": {"url":"http://www.changjiangtimes.com/c/4390/","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"cs", "pattern_type":"news"},
    "地产圈": {"url":"http://www.changjiangtimes.com/c/4386/", "pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"dcq", "pattern_type":"news"},
    "3C": {"url":"http://www.changjiangtimes.com/c/4385/","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"3C", "pattern_type":"news"},
    "政经": {"url":"http://www.changjiangtimes.com/c/china/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"zj", "pattern_type":"news"},
    "财经": {"url":"http://www.changjiangtimes.com/c/fin/", "pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"cj", "pattern_type":"news"},
    "产经": {"url":"http://www.changjiangtimes.com/c/4365/","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"chanjing", "pattern_type":"news"},
    "金融": {"url":"http://www.changjiangtimes.com/c/4381/", "pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"jr", "pattern_type":"news"},
    "财评天下": {"url":"http://www.changjiangtimes.com/c/pl/","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"cptx", "pattern_type":"news"},
    "公共时政": {"url":"http://www.changjiangtimes.com/c/shizheng/","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"ggsz", "pattern_type":"news"},
    "国际纵横": {"url":"http://www.changjiangtimes.com/c/world/", "pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"gjzh", "pattern_type":"news"},
    
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
                "base_url":"http://www.changjiangtimes.com",
                "data_path": "%s/%s/"%(data_path, website_short_name),
                "website_name": website_name,
                "b_class": name,
                "checkpoint_filename": "%s/%s_%s.ckpt"%(ckpt_path, website_short_name, info["short_name"]),
                "checkpoint_saved_days": info.get("ckpt_days",default_ckpt_days) ,
                "list_patterns": pattern_conf[info["pattern_type"]]["list_patterns"],
                "encoding":"gbk",
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


