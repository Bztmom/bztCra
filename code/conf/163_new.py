# -*- coding: utf-8 -*-
from .common import *

website_name = "网易"
website_short_name = "163"
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
            r'<h2><a href="(?P<url>.*?)">(?P<title>.*?)<\/a><\/h2>.*?<span class="time">(?P<pub_date>.*?)<\/span>'
        ],
        "news_patterns" : [
            "来源.*?>(?P<source>.*?)<.*?<div class=\"post_text\".*?>(?P<content>.*?)<\/div>.*?<div class=\"post_btmshare\">"
            ]
    },
    "qq":{
        "list_patterns" : [
            r'"title":"(?P<title>.*?)".*?"docurl":"(?P<url>.*?)".*?"time":"(?P<pub_date>.*?)"',
            r't:"(?P<title>.*?)",l:"(?P<url>.*?)",p:"(?P<pub_date>.*?)"',
        ],
        "news_patterns" : [
            "来源.*?>(?P<source>.*?)<.*?<div class=\"post_text\".*?>(?P<content>.*?)<\/div>.*?<div class=\"post_btmshare\">",
            '· <\/sp.*?<span>(?P<source>.*?)<\/span>.*?id="content".*?>(?P<content>.*?)<\/div>'
        ]
    },
    "gd":{
        "list_patterns" : [
            r'c:0,t:"(?P<title>.*?)",l:"(?P<url>.*?)",p:"(?P<pub_date>.*?)"',
        ],
        "news_patterns" : [
            "来源.*?>(?P<source>.*?)<.*?<div class=\"post_text\".*?>(?P<content>.*?)<\/div>.*?<div class=\"post_btmshare\">",
            '· <\/sp.*?<span>(?P<source>.*?)<\/span>.*?id="content".*?>(?P<content>.*?)<\/div>'
        ]
    },


}

def default_generate_next_list_url(crawler):
    if crawler.page_num == 0:
        crawler.page_num += 1
        ret_url = crawler.list_url_tpl
        crawler.list_url_tpl = ".".join(crawler.list_url_tpl.split(".")[:-1]) + "_%d."+crawler.list_url_tpl.split(".")[-1]
        yield ret_url

    ret_url = crawler.list_url_tpl % (crawler.page_num)
    crawler.page_num += 1
    yield ret_url

def qq_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url = crawler.list_url_tpl
            crawler.page_num+=1
            crawler.list_url_tpl = crawler.list_url_tpl[:-6]+"%d"+crawler.list_url_tpl[-5:]
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url
def sy_list_url(crawler):
    while crawler.page_num < 2:
        yield crawler.list_url_tpl

b_class_dict = {
    "滚动新闻": {"url":"http://money.163.com/special/002557S5/newsdata_idx_index.js?callback=data_callback", "pub_date_format":"%m/%d/%Y %H:%M:%S","next_list_url_generator":sy_list_url,"short_name":"sy", "pattern_type":"qq"},
    "财经-滚动新闻": {"url":"http://money.163.com/special/00251G8F/news_json.js?callback=data_callback", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":sy_list_url,"short_name":"sy", "pattern_type":"qq"},
    # "首页": {"url":"http://money.163.com/special/002557S5/newsdata_idx_index.js?callback=data_callback", "pub_date_format":"%m/%d/%Y %H:%M:%S","next_list_url_generator":sy_list_url,"short_name":"sy", "pattern_type":"qq"},
    # "股票": {"url":"http://money.163.com/special/002557S5/newsdata_idx_stock.js?callback=data_callback", "pub_date_format":"%m/%d/%Y %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"gp", "pattern_type":"qq"},
    # "商业": {"url":"http://money.163.com/special/002557S5/newsdata_idx_biz.js?callback=data_callback", "pub_date_format":"%m/%d/%Y %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"shangye", "pattern_type":"qq"},
    # "产经": {"url":"http://money.163.com/special/002557NJ/chanjing_data_chanjing_02.js?callback=data_callback", "pub_date_format":"%m/%d/%Y %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"cj", "pattern_type":"qq"},
    # "美股": {"url":"http://money.163.com/special/002557S0/data_meigu_usstock_02.js?callback=data_callback", "pub_date_format":"%m/%d/%Y %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"mg", "pattern_type":"qq"},
    # "宏观": {"url":"http://money.163.com/special/00252G50/macro.html", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":qq_generate_next_list_url,"short_name":"hg", "pattern_type":"news"},
    # "国际": {"url":"http://money.163.com/special/00252C1E/gjcj.html", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":qq_generate_next_list_url,"short_name":"gj", "pattern_type":"news"},
    # "商贸": {"url":"http://money.163.com/special/002526O3/trade09.html", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":qq_generate_next_list_url,"short_name":"sm", "pattern_type":"news"},
    # "能源": {"url":"http://money.163.com/special/002524SO/energy.html", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":qq_generate_next_list_url,"short_name":"ny", "pattern_type":"news"},
    # "交通": {"url":"http://money.163.com/special/002526O5/transport.html", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":qq_generate_next_list_url,"short_name":"jt", "pattern_type":"news"},
    # "房产": {"url":"http://money.163.com/special/002534NU/house2010.html", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":qq_generate_next_list_url,"short_name":"fc", "pattern_type":"news"},
    # "汽车": {"url":"http://money.163.com/special/002534NV/auto_house.html", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":qq_generate_next_list_url,"short_name":"qc", "pattern_type":"news"},
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


