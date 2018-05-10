# -*- coding: utf-8 -*-
from .common import *

website_name = "舜网财经"
website_short_name = "swcj"
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
            r'<li><span>\[(?P<pub_date>.*?)\]<\/span><a href="(?P<url>.*?)" target="_blank">(?P<title>.*?)<\/a><\/li>'
        ],
        "news_patterns" : [
            r'<META name="source" content="(?P<source>.*?)">.*?<div id="endSummary">(?P<content>.*?)<div class="author">.*?网络编辑:(?P<author>.*?)值班主任',
            r'<META name="source" content="(?P<source>.*?)">.*?<div id="endSummary">(?P<content>.*?)<div class="author">.*?网络编辑:(?P<author>.*?)<\/div>',
            r'<META name="source" content="(?P<source>.*?)">.*?<div class="h16">(?P<content>.*?)<div class="author">.*?网络编辑:(?P<author>.*?)<\/div>',
            
       ]
    },
    "lcjq":{
        "list_patterns" : [
            r'<li><span>(?P<pub_date>.*?)<\/span><a href="(?P<url>.*?)" target="_blank">(?P<title>.*?)<\/a><\/li>'
        ],
        "news_patterns" : [
            r'<META name="source" content="(?P<source>.*?)">.*?<div id="endSummary">(?P<content>.*?)<div class="author">.*?网络编辑:(?P<author>.*?)值班主任',
            r'<META name="source" content="(?P<source>.*?)">.*?<div id="endSummary">(?P<content>.*?)<div class="author">.*?网络编辑:(?P<author>.*?)<\/div>',
            r'<META name="source" content="(?P<source>.*?)">.*?<div class="h16">(?P<content>.*?)<div class="author">.*?网络编辑:(?P<author>.*?)<\/div>',
       ]
    },
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            crawler.page_num+=1
            ret_url=crawler.list_url_tpl
            crawler.list_url_tpl = crawler.list_url_tpl+"%d.html"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url


b_class_dict = {
    "财经新闻": {"url":"http://money.e23.cn/content/jrdt/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"cjxw", "pattern_type":"news"},
    "理财技巧": {"url":"http://money.e23.cn/content/lcjq/","ckpt_days":300,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"lcjq", "pattern_type":"lcjq"},
    "行业资讯保险": {"url":"http://money.e23.cn/content/hyzxb/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"hyzxbx", "pattern_type":"news"},
    "行业资讯证券": {"url":"http://money.e23.cn/content/hyzxz/", "ckpt_days":300,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"hyzxzq", "pattern_type":"news"},
    "深度评论": {"url":"http://money.e23.cn/content/sdpl/", "ckpt_days":300,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"sdpl", "pattern_type":"news"},
    "理财产品新": {"url":"http://money.e23.cn/content/lccpx/", "ckpt_days":300,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"lccpx", "pattern_type":"news"},
    "银行动态": {"url":"http://money.e23.cn/content/zcjd/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"yhdt", "pattern_type":"lcjq"},
    "信贷咨询": {"url":"http://money.e23.cn/content/xdzx/", "ckpt_days":300,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"xdzx", "pattern_type":"lcjq"},
    "电子银行": {"url":"http://money.e23.cn/content/sswy/", "ckpt_days":1000,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"dzyh", "pattern_type":"lcjq"},
    "银行卡资讯": {"url":"http://money.e23.cn/content/yhkzx/", "ckpt_days":500,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"yhkzx", "pattern_type":"lcjq"},
    "监管动态保险": {"url":"http://money.e23.cn/content/jgdtb/","ckpt_days":300, "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"jgdtbx", "pattern_type":"news"},
    "社保园地": {"url":"http://money.e23.cn/content/sbyd/", "ckpt_days":500,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"sbyd", "pattern_type":"news"},
    "保险产品": {"url":"http://money.e23.cn/content/bxcp/", "ckpt_days":1000,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"bxcp", "pattern_type":"lcjq"},
    "监管动态证券": {"url":"http://money.e23.cn/content/jgdtz/","ckpt_days":300, "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"jgdtzq", "pattern_type":"news"},
    "市场点评": {"url":"http://money.e23.cn/content/scdp/", "ckpt_days":300,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"scdp", "pattern_type":"news"},
    "股市风云": {"url":"http://money.e23.cn/content/gsfy/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"gsfy", "pattern_type":"news"},
    "投诉维权": {"url":"http://money.e23.cn/content/tswq/", "ckpt_days":300,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"tswq", "pattern_type":"news"},
    "理财之星新": {"url":"http://money.e23.cn/content/lczxx/", "ckpt_days":500,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"lczxx", "pattern_type":"news"},
    "畅谈商机": {"url":"http://money.e23.cn/content/ctsj/", "ckpt_days":100,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"ctsj", "pattern_type":"news"},
    
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


