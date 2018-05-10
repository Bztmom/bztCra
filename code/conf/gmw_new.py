# -*- coding: utf-8 -*-
from .common import *

website_name = "光明网"
website_short_name = "gmw"
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
            '<li><a href=(?P<url>2(.*?).htm) target=_blank>(?P<title>.*?)<\/a><span class=\"channel-newsTime\">(?P<pub_date>.*?)<\/span'
        ],
        "news_patterns" : [
            '来源：(<a.*?>)?(?P<source>.*?)<\/a><\/span>.*?editor_baidu\">(责任编辑：)?(?P<author>.*?)<\/span>.*?contentMain\">(?P<content>.*?)<!--\/enpcontent-->',
            '来源：.*?\">(?P<source>.*?)<\/a>.*?contentMain\">(?P<content>.*?)<\/div><div id=\"contentLiability\".*?>(责任编辑：)?(?P<author>.*?)<\/div>',
        ]
    },
    "wangshi":{
        "list_patterns" : [
            '<h1 class="title"><a atremote href="(?P<url>.*?)" target="_blank">(?P<title>.*?)<\/a><\/h1>',
        ],
        "news_patterns" : [
            '<META name="publishdate" content="(?P<pub_date>.*?)">.*?来源：(<a.*?>)?(?P<source>.*?)<\/a><\/span>.*?editor_baidu\">(责任编辑：)?(?P<author>.*?)<\/span>.*?contentMain\">(?P<content>.*?)<!--\/enpcontent-->',
            '<META name="publishdate" content="(?P<pub_date>.*?)">.*?来源：.*?\">(?P<source>.*?)<\/a>.*?contentMain\">(?P<content>.*?)<\/div><div id=\"contentLiability\".*?>(责任编辑：)?(?P<author>.*?)<\/div>',
        ]
    },
}


b_class_dict = {
    "经济要闻": {"url":"http://economy.gmw.cn/node_8971.htm","base_url":"http://economy.gmw.cn/", "short_name":"jjyw", "pattern_type":"news"},
    "金融要闻": {"url":"http://finance.gmw.cn/node_42534.htm","base_url":"http://finance.gmw.cn/", "short_name":"jryw", "pattern_type":"news"},
    "经济观点": {"url":"http://economy.gmw.cn/node_59269.htm","base_url":"http://economy.gmw.cn/", "short_name":"jjgd", "pattern_type":"news"},
    "财经眼": {"url":"http://economy.gmw.cn/node_9141.htm","base_url":"http://economy.gmw.cn/", "short_name":"cjy", "pattern_type":"news"},
    "经济人物": {"url":"http://economy.gmw.cn/node_59269.htm","base_url":"http://economy.gmw.cn/", "short_name":"jjrw", "pattern_type":"news"},
    "产经": {"url":"http://economy.gmw.cn/node_21787.htm","base_url":"http://economy.gmw.cn/", "short_name":"cj", "pattern_type":"news"},
    "网事": {"url":"http://tech.gmw.cn/node_10609.htm","base_url":"http://economy.gmw.cn/", "short_name":"ws", "pattern_type":"wangshi"},

}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 3:
        if crawler.page_num == 0:
            ret_url = crawler.list_url_tpl
            crawler.logger.debug(ret_url)
            crawler.page_num = 2
            yield ret_url
        else:
            crawler.list_url_tpl = crawler.list_url_tpl.replace(".htm","_%d.htm")
            ret_url = crawler.list_url_tpl%(crawler.page_num)
            crawler.logger.debug(ret_url)
            yield ret_url

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
                "pub_date_format":"%Y-%m-%d",
                "base_url": info["base_url"],
                "next_list_url_generator":info.get("list_url_gen", default_generate_next_list_url) ,
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


