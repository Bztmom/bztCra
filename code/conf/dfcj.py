# -*- coding: utf-8 -*-
from .common import *

website_name = "东方财经"
website_short_name = "dfcj"
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
            r'<p class="title">.*?<a href="(?P<url>.*?)" target="_blank">(?P<title>.*?)<\/a>'
        ],
        "news_patterns" : [
            r'<div class="time">(?P<pub_date>.*?)<\/div>.*?来源：(<\/span>)?(?P<source>.*?)<\/div>.*?(编辑：(<a.*?>)?(?P<author>.*?)(<\/a>)?<\/span>.*?)?<!-- 正文内容 -->(?P<content>.*?)<!--原文标题-->',

       ]
    },
    "gd":{
        "list_patterns" : [
             r'<li>.*?<a href="(?P<url>http:\/\/news.eastday.com(.*?))".*?title="(?P<title>.*?).*?<span class="black12 fr text4">(?P<pub_date>.*?)<\/span>'
        ],
        "news_patterns" : [
            r'来源:(<\/span>)?(<a.*?>)?(?P<source>.*?)(<\/a>)?<span.*?>(作者:)?(选稿:)?(<\/span>)?(?P<author>.*?)(<!-- EndOfFootnote -->)?<\/p>.*?<div id="zw" class="grey14 lh26">(?P<content>.*?)<!-- 正文 end -->',
            ]
    },
    "scljl":{
        "list_patterns" : [
             r'<div><a href="(?P<url>.*?)" target="_blank" class="grey24" title="(?P<title>.*?)".*?<p class="grey12">(?P<pub_date>.*?)<\/p>'
        ],
        "news_patterns" : [
            r'来源:(<\/span>)?(<a.*?>)?(?P<source>.*?)(<\/a>)?<span.*?>(作者:)?(选稿:)?(<\/span>)?(?P<author>.*?)(<!-- EndOfFootnote -->)?<\/p>.*?<div id="zw" class="grey14 lh26">(?P<content>.*?)<!-- 正文 end -->',
            ]
    },
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            crawler.page_num+=1
        ret_url = crawler.list_url_tpl % (crawler.page_num)
        yield ret_url

def gd_generate_next_list_url(crawler):
    ret_url=crawler.list_url_tpl
    yield ret_url

def scljl_generate_next_list_url(crawler):
    while crawler.page_num < 5:
        if crawler.page_num == 0:
            # crawler.page_num+=1
            ret_url=crawler.list_url_tpl
            crawler.list_url_tpl = crawler.list_url_tpl+"index%d.html"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url


b_class_dict = {
    "上市公司-上市公司": {"url":"http://finance.eastmoney.com/news/cssgs_%d.html","pub_date_format":u"%Y年%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"ssgs", "pattern_type":"news"},
    "上市公司-中国概念股": {"url":"http://stock.eastmoney.com/news/czggng_%d.html","pub_date_format":u"%Y年%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"zggng", "pattern_type":"news"},
    "上市公司-港股新闻": {"url":"http://hk.eastmoney.com/news/cgsbd_%d.html","pub_date_format":u"%Y年%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"ggxw", "pattern_type":"news"},
    "要闻-要闻精华": {"url":"http://finance.eastmoney.com/news/cywjh_%d.html","pub_date_format":u"%Y年%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"ywjh", "pattern_type":"news"},
    "要闻-国内经济": {"url":"http://finance.eastmoney.com/news/cgnjj_%d.html","pub_date_format":u"%Y年%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gnjj", "pattern_type":"news"},
    "要闻-国际经济": {"url":"http://finance.eastmoney.com/news/cgjjj_%d.html","pub_date_format":u"%Y年%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gwjj", "pattern_type":"news"},
    "要闻-证券要闻": {"url":"http://finance.eastmoney.com/news/czqyw_%d.html","pub_date_format":u"%Y年%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"zqyw", "pattern_type":"news"},
    "公司新闻": {"url":"http://finance.eastmoney.com/news/cgsxw_%d.html","pub_date_format":u"%Y年%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gsxw", "pattern_type":"news"},
    "产经新闻": {"url":"http://finance.eastmoney.com/news/ccjxw_%d.html","pub_date_format":u"%Y年%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"cjxw", "pattern_type":"news"},
    "新股要闻": {"url":"http://stock.eastmoney.com/news/cxgyw_%d.html","pub_date_format":u"%Y年%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"xgyw", "pattern_type":"news"},
    "滚动新闻": {"url":"http://news.eastday.com/eastday/13news/auto/news/finance/index_K47.html?t=true","pub_date_format":"%Y/%m/%d %H:%M:%S","next_list_url_generator":gd_generate_next_list_url,"short_name":"gdxw", "pattern_type":"gd"},
    #"市场零距离": {"url":"http://finance.eastday.com/n998118/","pub_date_format":"%Y/%m/%d %H:%M","next_list_url_generator":scljl_generate_next_list_url,"short_name":"scljl", "pattern_type":"scljl"},

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
                # "base_url":info["base_url"],
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


