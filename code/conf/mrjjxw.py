# -*- coding: utf-8 -*-
from .common import *

website_name = "每日经济新闻"
website_short_name = "mrjjxw"
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
            r'<li class="u-news-title">.*?<a href="(?P<url>.*?)".*?target="_blank">(?P<title>.*?)<\/a>'
        ],
        "news_patterns" : [
            r'<span class="source">(?P<source>.*?)<\/span>.*?<span class="time">(?P<pub_date>.*?)<\/span>.*?<div class="g-articl-text">(?P<content>.*?)<!-- 页数 -->.*?<div class="u-editor">.*?<span>.*?责编(?P<author>.*?)<\/span>',
       ]
    },
}


def yw_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            crawler.page_num+=1
            ret_url=crawler.list_url_tpl
            crawler.list_url_tpl = crawler.list_url_tpl+"page/%d.html"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

b_class_dict = {
    "今日报纸": {"url":"http://www.nbd.com.cn/columns/79/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"jrbz", "pattern_type":"news"},
    "要闻": {"url":"http://www.nbd.com.cn/columns/3/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"yw", "pattern_type":"news"},
    "宏观-焦点": {"url":"http://economy.nbd.com.cn/columns/313/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"jd", "pattern_type":"news"},
    "宏观-形势": {"url":"http://economy.nbd.com.cn/columns/315/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"xs", "pattern_type":"news"},
    "宏观-洞见": {"url":"http://economy.nbd.com.cn/columns/475/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"dj", "pattern_type":"news"},
    "宏观-一线报告": {"url":"http://economy.nbd.com.cn/columns/590/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"yxbg", "pattern_type":"news"},
    "证券-重磅推荐": {"url":"http://stocks.nbd.com.cn/columns/318/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"zbtj", "pattern_type":"news"},
    "证券-两融龙虎榜": {"url":"http://stocks.nbd.com.cn/columns/402/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"lrlhb", "pattern_type":"news"},
    "证券-A股动态": {"url":"http://stocks.nbd.com.cn/columns/275/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"agdt", "pattern_type":"news"},
    "证券-公告速递": {"url":"http://stocks.nbd.com.cn/columns/28/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"ggsd", "pattern_type":"news"},
    "证券-海外市场": {"url":"http://stocks.nbd.com.cn/columns/405/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"hwsc", "pattern_type":"news"},
    "证券-到达投资手记": {"url":"http://stocks.nbd.com.cn/columns/476/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"ddtzsj", "pattern_type":"news"},
    "证券-新三板": {"url":"http://stocks.nbd.com.cn/columns/324/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"xsb", "pattern_type":"news"},
    "金融-要闻": {"url":"http://stocks.nbd.com.cn/columns/329/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"jryw", "pattern_type":"news"},
    "金融-监管": {"url":"http://stocks.nbd.com.cn/columns/415/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"jrjg", "pattern_type":"news"},
    "金融-机构": {"url":"http://stocks.nbd.com.cn/columns/327/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"jrjigou", "pattern_type":"news"},
    "金融-市场": {"url":"http://stocks.nbd.com.cn/columns/326/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"jrsc", "pattern_type":"news"},
    "金融-新金融周刊": {"url":"http://stocks.nbd.com.cn/columns/591/", "ckpt_days":100,"pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"xjrzk", "pattern_type":"news"},
    "金融-保险周刊": {"url":"http://stocks.nbd.com.cn/columns/592/", "ckpt_days":100,"pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"bxzk", "pattern_type":"news"},
    "公司-热点公司": {"url":"http://industry.nbd.com.cn/columns/346/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"rdgs", "pattern_type":"news"},
    "公司-产业趋势": {"url":"http://industry.nbd.com.cn/columns/585/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"cyqs", "pattern_type":"news"},
    "公司-商业人物": {"url":"http://industry.nbd.com.cn/columns/418/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"syrw", "pattern_type":"news"},
    "公司-区域经济": {"url":"http://industry.nbd.com.cn/columns/586/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"qyjj", "pattern_type":"news"},
    "公司-重磅调查": {"url":"http://industry.nbd.com.cn/columns/587/", "ckpt_days":100,"pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"zbdc", "pattern_type":"news"},
    "TMT-互联网": {"url":"http://tmt.nbd.com.cn/columns/448/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"hlw", "pattern_type":"news"},
    "TMT-TMT观察": {"url":"http://tmt.nbd.com.cn/columns/256/", "ckpt_days":100,"pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"tmtgc", "pattern_type":"news"},
    "TMT-人物": {"url":"http://tmt.nbd.com.cn/columns/451/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"rw", "pattern_type":"news"},
    "TMT-记者专栏": {"url":"http://tmt.nbd.com.cn/columns/499/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"jzzk", "pattern_type":"news"},
    "TMT-游戏": {"url":"http://tmt.nbd.com.cn/columns/584/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"yx", "pattern_type":"news"},
    "TMT-新科技": {"url":"http://tmt.nbd.com.cn/columns/583/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"xkj", "pattern_type":"news"},
    "TMT-电商": {"url":"http://tmt.nbd.com.cn/columns/478/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"ds", "pattern_type":"news"},
    "TMT-智能硬件": {"url":"http://tmt.nbd.com.cn/columns/477/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"znyj", "pattern_type":"news"},
    "理财-重磅原创": {"url":"http://money.nbd.com.cn/columns/440/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"zbyc", "pattern_type":"news"},
    "理财-基金投资": {"url":"http://money.nbd.com.cn/columns/441/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"jjtz", "pattern_type":"news"},
    "理财-另类投资": {"url":"http://money.nbd.com.cn/columns/407/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"lltz", "pattern_type":"news"},
    "理财-理财实盘": {"url":"http://money.nbd.com.cn/columns/439/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"lcsp", "pattern_type":"news"},
    "理财-火山众筹": {"url":"http://money.nbd.com.cn/columns/589/","ckpt_days":300, "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"hszc", "pattern_type":"news"},
    "新三板-要闻": {"url":"http://money.nbd.com.cn/columns/324/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"xsbyw", "pattern_type":"news"},
    "新三板-访谈": {"url":"http://www.nbd.com.cn/columns/xinsanban/605/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"xsbft", "pattern_type":"news"},
    "新三板-资讯": {"url":"http://www.nbd.com.cn/columns/xinsanban/606/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"xsbzx", "pattern_type":"news"},
    "新三板-活动": {"url":"http://www.nbd.com.cn/columns/xinsanban/607/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":yw_generate_next_list_url,"short_name":"xsbhd", "pattern_type":"news"},
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


