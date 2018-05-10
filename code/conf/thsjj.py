# -*- coding: utf-8 -*-
from .common import *

website_name = "同花顺经济"
website_short_name = "thsjj"
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
            r'<span class="arc-title">.*?<a target="_blank" title="(?P<title>.*?)" href="(?P<url>.*?)">.*?<\/a>.*?<span>(?P<pub_date>.*?)<\/span>'
        ],
        "news_patterns" : [
            r'(来源：(\s+)?(<a.*?>)?(\s+)?(?P<source>[^<]*?)(<\/a>)?(\s+)?(<\/a>)?<\/span>.*?)?(作者：(?P<author>.*?)<\/span>.*?)?atc-content">(?P<content>.*?)返回首页',
            r'article-con">(?P<content>.*?)<!--articletag-->',
        ]
    },
        "xinsanban":{
        "list_patterns" : [
            r'<h3 class="conts_tit"><a target="_blank" title="(?P<title>.*?)" href="(?P<url>.*?)">.*?<\/a><\/h3>.*?<p class="news_time">(?P<pub_date>.*?)<\/p>'
        ],
        "news_patterns" : [
            r'(来源：(\s+)?(<a.*?>)?(\s+)?(?P<source>[^<]*?)(<\/a>)?(\s+)?(<\/a>)?<\/span>.*?)?(作者：(?P<author>.*?)<\/span>.*?)?atc-content">(?P<content>.*?)返回首页',
            r'article-con">(?P<content>.*?)<!--articletag-->',
            r'(来源：(\s+)?(<a.*?>)?(\s+)?(?P<source>[^<]*?)(<\/a>)?(\s+)?<\/a>.*?)?<div class="introRi">(?P<content>.*?)返回首页',
            ]
    },
    "gundongxinwen":{
        "list_patterns" : [
            r'"title":"(?P<title>.*?)",.*?"url":"(?P<url>.*?)","source":"(?P<source>.*?)",.*?"pubDate":"(?P<pub_date>.*?)",',
        ],
        "news_patterns" : [
            r'(来源：(\s+)?(<a.*?>)?(\s+)?(?P<source>[^<]*?)(<\/a>)?(\s+)?(<\/a>)?<\/span>.*?)?(作者：(?P<author>.*?)<\/span>.*?)?atc-content">(?P<content>.*?)返回首页',
            r'(来源：(<span.*?>)?(?P<source>.*?)(<\/span>)?<\/div>.*?)?<div class="nml_arti">(?P<content>.*?)<\/div>',
            r'article-con">(?P<content>.*?)<!--articletag-->',
            r'(来源：(\s+)?(<a.*?>)?(\s+)?(?P<source>[^<]*?)(<\/a>)?(\s+)?<\/a>.*?)?<div class="introRi">(?P<content>.*?)返回首页',
            r'Refresh" content=.*?URL=(?P<content>.*?)"',
        ]
    },
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 3:
        if crawler.page_num == 0:
            ret_url = crawler.list_url_tpl
            crawler.page_num+=1
            crawler.list_url_tpl = crawler.list_url_tpl+"index_%d.shtml"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

def xsb_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url = crawler.list_url_tpl+"xsbgd_list/"
            crawler.page_num+=1
            crawler.list_url_tpl = crawler.list_url_tpl+"xsbgd_list/"+"index_%d.shtml"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

def gdxw_generate_next_list_url(crawler):
    while crawler.page_num < 1:
        ret_url = crawler.list_url_tpl
        yield ret_url

b_class_dict = {
    "股票-滚动新闻": {"url":"http://stock.10jqka.com.cn/thsgd/siteall.js?_=1516090213200", "pub_date_format":"%Y/%m/%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gs-gdxw", "pattern_type":"gundongxinwen"},
    "公司要闻": {"url":"http://stock.10jqka.com.cn/gsyw_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gsyw", "pattern_type":"news"},
    "拟上市公司新闻": {"url":"http://stock.10jqka.com.cn/nssgsxw_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"nssgsxw", "pattern_type":"news"},
    "股票-行业研究": {"url":"http://stock.10jqka.com.cn/bkfy_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gp-hyyj", "pattern_type":"news"},
    "股票-要闻": {"url":"http://stock.10jqka.com.cn/stocknews_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gp-yw", "pattern_type":"news"},
    "财经-财经要闻": {"url":"http://news.10jqka.com.cn/today_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"cj-cjyw", "pattern_type":"news"},
    "财经-宏观经济": {"url":"http://news.10jqka.com.cn/cjzx_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"cj-hgjj", "pattern_type":"news"},
    "财经-产经新闻": {"url":"http://news.10jqka.com.cn/cjkx_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"cj-cjxw", "pattern_type":"news"},
    "财经-国际财经": {"url":"http://news.10jqka.com.cn/guojicj_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"cj-gjcj", "pattern_type":"news"},
    "财经-金融市场": {"url":"http://news.10jqka.com.cn/jrsc_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"cj-jrsc", "pattern_type":"news"},
    "财经-非上市公司新闻": {"url":"http://news.10jqka.com.cn/fssgsxw_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"cj-fssgsxw", "pattern_type":"news"},
    "财经-区域经济": {"url":"http://news.10jqka.com.cn/region_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"cj-qyjj", "pattern_type":"news"},
    "财经-财经评论": {"url":"http://news.10jqka.com.cn/fortune_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"cj-cjpl", "pattern_type":"news"},
    "财经-财经人物": {"url":"http://news.10jqka.com.cn/cjrw_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"cj-cjrw", "pattern_type":"news"},  
    "股票-公司资讯": {"url":"http://stock.10jqka.com.cn/companynews_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gp-gszx", "pattern_type":"news"},
    "股票-公告解读": {"url":"http://stock.10jqka.com.cn/ggjd_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gp-ggjd", "pattern_type":"news"},
    "股票-个股聚焦": {"url":"http://stock.10jqka.com.cn/ggjj_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gp-ggjj", "pattern_type":"news"},
    "股票-公司研究": {"url":"http://stock.10jqka.com.cn/gegudp_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gp-gsyj", "pattern_type":"news"},
    "股票-个股公告": {"url":"http://stock.10jqka.com.cn/gegugg_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gp-gggg", "pattern_type":"news"},
    "股票-独家公司活动": {"url":"http://yuanchuang.10jqka.com.cn/djgshd_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gp-djgshd", "pattern_type":"news"},
    "港股-公司新闻": {"url":"http://stock.10jqka.com.cn/hks/ggdt_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gg-gsxw", "pattern_type":"news"},
    "港股-A+H动态": {"url":"http://stock.10jqka.com.cn/hks/ahdt_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gg-A+H", "pattern_type":"news"},
    "港股-港股权证": {"url":"http://stock.10jqka.com.cn/hks/wlzx_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gg-ggqz", "pattern_type":"news"},
    "港股-港股新股": {"url":"http://stock.10jqka.com.cn/hks/ggxg_list/", "pub_date_format":u"%m月%d日 %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gg-ggxg", "pattern_type":"news"},
    "新三板-all": {"url":"http://xinsanban.10jqka.com.cn/", "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":xsb_generate_next_list_url,"short_name":"xsb-all", "pattern_type":"xinsanban"},
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


