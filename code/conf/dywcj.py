# -*- coding: utf-8 -*-
from .common import *

website_name = "大洋网财经"
website_short_name = "dywcj"
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
            '<h2><a href="(?P<url>.*?)" target="_blank">(?P<title>.*?)<\/a><\/h2>.*?<div class="news-time">(?P<pub_date>.*?)<\/div>'
        ],
        "news_patterns" : [
            r'<span class="source">来源:(?P<source>.*?)<\/span>.*?<!--enpcontent-->(?P<content>.*?)<!--\/enpcontent-->.*?<div class="editor">\[ 编辑：(?P<author>.*?)\]<\/div>',
            ]
    },
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url=crawler.list_url_tpl
            crawler.page_num+=1
            crawler.list_url_tpl =crawler.list_url_tpl[:-6]+"_%d.shtml"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

# def cj_generate_next_list_url(crawler):
#     while crawler.page_num < 2:
#         if crawler.page_num == 0:
#             ret_url=crawler.list_url_tpl
#             crawler.page_num+=1
#             crawler.list_url_tpl ="http://news.dayoo.com/finance/139999"+"_%d.shtml"
#             yield ret_url
#         else:
#             ret_url = crawler.list_url_tpl % (crawler.page_num)
#             yield ret_url

# def sh_generate_next_list_url(crawler):
#     while crawler.page_num < 2:
#         if crawler.page_num == 0:
#             ret_url=crawler.list_url_tpl
#             crawler.page_num+=1
#             crawler.list_url_tpl ="http://news.dayoo.com/society/140000"+"_%d.shtml"
#             yield ret_url
#         else:
#             ret_url = crawler.list_url_tpl % (crawler.page_num)
#             yield ret_url

# def rp_generate_next_list_url(crawler):
#     while crawler.page_num < 2:
#         if crawler.page_num == 0:
#             ret_url=crawler.list_url_tpl
#             crawler.page_num+=1
#             crawler.list_url_tpl ="http://news.dayoo.com/guangzhou/153828"+"_%d.shtml"
#             yield ret_url
#         else:
#             ret_url = crawler.list_url_tpl % (crawler.page_num)
#             yield ret_url

# def sj_generate_next_list_url(crawler):
#     while crawler.page_num < 2:
#         if crawler.page_num == 0:
#             ret_url=crawler.list_url_tpl
#             crawler.page_num+=1
#             crawler.list_url_tpl ="http://news.dayoo.com/guangzhou/150957"+"_%d.shtml"
#             yield ret_url
#         else:
#             ret_url = crawler.list_url_tpl % (crawler.page_num)
#             yield ret_url

# def gj_generate_next_list_url(crawler):
#     while crawler.page_num < 2:
#         if crawler.page_num == 0:
#             ret_url=crawler.list_url_tpl
#             crawler.page_num+=1
#             crawler.list_url_tpl ="http://news.dayoo.com/world/139998"+"_%d.shtml"
#             yield ret_url
#         else:
#             ret_url = crawler.list_url_tpl % (crawler.page_num)
#             yield ret_url

# def zg_generate_next_list_url(crawler):
#     while crawler.page_num < 2:
#         if crawler.page_num == 0:
#             ret_url=crawler.list_url_tpl
#             crawler.page_num+=1
#             crawler.list_url_tpl ="http://news.dayoo.com/world/139997"+"_%d.shtml"
#             yield ret_url
#         else:
#             ret_url = crawler.list_url_tpl % (crawler.page_num)
#             yield ret_url

# def gd_generate_next_list_url(crawler):
#     while crawler.page_num < 2:
#         if crawler.page_num == 0:
#             ret_url=crawler.list_url_tpl
#             crawler.page_num+=1
#             crawler.list_url_tpl ="http://news.dayoo.com/world/139996"+"_%d.shtml"
#             yield ret_url
#         else:
#             ret_url = crawler.list_url_tpl % (crawler.page_num)
#             yield ret_url

# def gz_generate_next_list_url(crawler):
#     while crawler.page_num < 2:
#         if crawler.page_num == 0:
#             ret_url=crawler.list_url_tpl
#             crawler.page_num+=1
#             crawler.list_url_tpl ="http://news.dayoo.com/world/139995"+"_%d.shtml"
#             yield ret_url
#         else:
#             ret_url = crawler.list_url_tpl % (crawler.page_num)
#             yield ret_url

b_class_dict = {
    "广州财经": {"url":"http://news.dayoo.com/guangzhou/150960.shtml", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gzcj", "pattern_type":"news"},
    "社会": {"url":"http://news.dayoo.com/society/140000.shtml", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"sh", "pattern_type":"news"},
    "财经": {"url":"http://news.dayoo.com/finance/139999.shtml", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"cj", "pattern_type":"news"},
    "热评": {"url":"http://news.dayoo.com/guangzhou/153828.shtml", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"rp", "pattern_type":"news"},
    "国际": {"url":"http://news.dayoo.com/world/139998.shtml", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gj", "pattern_type":"news"},
    #"中国": {"url":"http://news.dayoo.com/china/139997.shtml", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"zg", "pattern_type":"news"},
    "广东": {"url":"http://news.dayoo.com/guangdong/139996.shtml", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gd", "pattern_type":"news"},
    "广州": {"url":"http://news.dayoo.com/guangzhou/139995.shtml", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gz", "pattern_type":"news"},
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


