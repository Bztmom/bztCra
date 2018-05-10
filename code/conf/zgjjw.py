# -*- coding: utf-8 -*-
from .common import *

website_name = "中国经济网"
website_short_name = "zgjjw"
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
            r'<td height="28" align="left" class="font14">·<a href="(?P<url>.*?)" target="_blank">(?P<title>.*?)<\/a>.*?<span class="rq1">\[(?P<pub_date>.*?)\]<\/span><\/td>',
            r'<a href="(?P<url>.*?)" target="_blank">(?P<title>.*?)<\/a>&.*?\[(?P<pub_date>.*?)\]',
        ],
        "news_patterns" : [
            r'来源：(?P<source>.*?)<\/span>.*?<div class="content" id="articleText">(?P<content>.*?)<p style="float:right;">\（责任编辑：(?P<author>.*?)\）<\/p>',
            r'来源：(?P<source>.*?)<\/span>.*?<div class="content" id="articleText">(?P<content>.*?)<textarea.*?\（责任编辑：(?P<author>.*?)\）<\/p>'
       ]
    },
    "yy":{
        "list_patterns" : [
            r'◆</td>.*?<a href="(?P<url>.*?)" target="_blank">(?P<title>.*?)<\/a'
        ],
        "news_patterns" : [
            r'articleTime">(?P<pub_date>.*?)<\/span>.*?来源：(?P<source>.*?)<\/span>.*?<div class="content" id="articleText">(?P<content>.*?)<p style="float:right;">\（责任编辑：(?P<author>.*?)\）<\/p>',
            r'articleTime">(?P<pub_date>.*?)<\/span>.*?来源：(?P<source>.*?)<\/span>.*?<div class="content" id="articleText">(?P<content>.*?)<textarea.*?\（责任编辑：(?P<author>.*?)\）<\/p>'
       ]
    },

}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 1:
        if crawler.page_num == 0:
            ret_url=crawler.list_url_tpl
            crawler.list_url_tpl = crawler.list_url_tpl+"index_%d.shtml"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url


b_class_dict = {
    "财经滚动新闻": {"url":"http://finance.ce.cn/rolling/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"cjgdxw", "pattern_type":"news"},
    "股市-大势研判": {"url":"http://finance.ce.cn/10cjsy/ds/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"dsyp", "pattern_type":"news"},
    "股市-公司动态": {"url":"http://finance.ce.cn/10cjsy/gs/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gsdt", "pattern_type":"news"},
    "股市-并购重组": {"url":"http://finance.ce.cn/10cjsy/bg/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"bgcz", "pattern_type":"news"},
    "股市-上市观察": {"url":"http://finance.ce.cn/10cjsy/ss/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"ssgc", "pattern_type":"news"},
    "股市-行业新闻": {"url":"http://finance.ce.cn/10cjsy/hy/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"hyxw", "pattern_type":"news"},
    "股市-板块研究": {"url":"http://finance.ce.cn/10cjsy/bk/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"bkyj", "pattern_type":"news"},
    "股市-主力动态": {"url":"http://finance.ce.cn/10cjsy/zl/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"zldt", "pattern_type":"news"},
    "股市-股指期货": {"url":"http://finance.ce.cn/10cjsy/qt/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gzqh", "pattern_type":"news"},
    "股市-海外市场": {"url":"http://finance.ce.cn/10cjsy/hw/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"hwsc", "pattern_type":"news"},
    "股市-滚动新闻": {"url":"http://finance.ce.cn/stock/gsgdbd/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gsgdxw", "pattern_type":"news"},
    "基金滚动新闻": {"url":"http://finance.ce.cn/jjpd/jjpdgd/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"jjgdxw", "pattern_type":"news"},
    "银行滚动新闻": {"url":"http://finance.ce.cn/bank12/scroll/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"yhgdxw", "pattern_type":"news"},
    "保险": {"url":"http://finance.ce.cn/insurance1/scroll-news/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"bx", "pattern_type":"news"},
    "期货滚动新闻": {"url":"http://finance.ce.cn/futures/qhgdbd/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"qhgdxw", "pattern_type":"news"},
    "热点聚焦": {"url":"http://finance.ce.cn/2015home/jj/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"rdjj", "pattern_type":"news"},
    "基金看市": {"url":"http://finance.ce.cn/jjpd/jjpddyp/jjks/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"jjks", "pattern_type":"news"},
    "基金研报": {"url":"http://finance.ce.cn/jjpd/jjdsp/yb/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"jjyb", "pattern_type":"news"},
    "基金创新": {"url":"http://finance.ce.cn/jjpd/jjdsp/jjcx/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"jjcx", "pattern_type":"news"},
    "基金公告": {"url":"http://finance.ce.cn/jjpd/jjdsp/jjgg/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"jjgg", "pattern_type":"news"},
    "新基速递": {"url":"http://finance.ce.cn/jjpd/jjdsp/tj/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"xjsd", "pattern_type":"news"},
    "期货要闻": {"url":"http://finance.ce.cn/futures/qhywq/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"qhyw", "pattern_type":"news"},
    "期货评论及研报": {"url":"http://finance.ce.cn/futures/qhscpl/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"qhpljyb", "pattern_type":"news"},
    "期货资讯及公告": {"url":"http://finance.ce.cn/futures/qtzx/", "pub_date_format":"%Y/%m/%d  %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"qhzxjgg", "pattern_type":"news"},
    "产业市场-食品-行业动态": {"url":"http://www.ce.cn/cysc/sp/info/", "pub_date_format":["%Y/%m/%d %H:%M","%Y年%m月%d日 %H:%M","%Y-%m-%d %H:%M"],"next_list_url_generator":default_generate_next_list_url,"short_name":"sphydt", "pattern_type":"news"},
    "产业市场-食品-公司观察": {"url":"http://www.ce.cn/cysc/sp/info/", "pub_date_format":["%Y/%m/%d %H:%M","%Y年%m月%d日 %H:%M","%Y-%m-%d %H:%M"],"next_list_url_generator":default_generate_next_list_url,"short_name":"spssgs", "pattern_type":"news"},
    "产业市场-食品-曝光台": {"url":"http://www.ce.cn/cysc/sp/baoguantai/", "pub_date_format":["%Y/%m/%d %H:%M","%Y年%m月%d日 %H:%M","%Y-%m-%d %H:%M"],"next_list_url_generator":default_generate_next_list_url,"short_name":"spbgt", "pattern_type":"news"},
    "产业市场-食品-本网专稿": {"url":"http://www.ce.cn/cysc/sp/bwzg/", "pub_date_format":["%Y/%m/%d %H:%M","%Y年%m月%d日 %H:%M","%Y-%m-%d %H:%M"],"next_list_url_generator":default_generate_next_list_url,"short_name":"spbwzg", "pattern_type":"news"},
    "产业市场-房地产-本网专稿": {"url":"http://www.ce.cn/cysc/newmain/right/zg/", "pub_date_format":["%Y/%m/%d %H:%M","%Y年%m月%d日 %H:%M","%Y-%m-%d %H:%M"],"next_list_url_generator":default_generate_next_list_url,"short_name":"fdcbwzg", "pattern_type":"news"},
    "产业市场-IT-滚动": {"url":"http://www.ce.cn/cysc/tech/gd2012/", "pub_date_format":["%Y/%m/%d %H:%M","%Y年%m月%d日 %H:%M","%Y-%m-%d %H:%M"],"next_list_url_generator":default_generate_next_list_url,"short_name":"itgd", "pattern_type":"news"},
    "产业市场-家电-今日更新": {"url":"http://www.ce.cn/cysc/zgjd/kx/", "pub_date_format":["%Y/%m/%d %H:%M","%Y年%m月%d日 %H:%M","%Y-%m-%d %H:%M"],"next_list_url_generator":default_generate_next_list_url,"short_name":"jdjrgx", "pattern_type":"news"},
    "产业市场-交通-要闻": {"url":"http://www.ce.cn/cysc/jtys/yw/", "pub_date_format":["%Y/%m/%d %H:%M","%Y年%m月%d日 %H:%M","%Y-%m-%d %H:%M"],"next_list_url_generator":default_generate_next_list_url,"short_name":"jtyw", "pattern_type":"news"},
    "产业市场-人事-人事变动": {"url":"http://www.ce.cn/cysc/newmain/pplm/qyrw/", "pub_date_format":["%Y/%m/%d %H:%M","%Y年%m月%d日 %H:%M","%Y-%m-%d %H:%M"],"next_list_url_generator":default_generate_next_list_url,"short_name":"rsrsbd", "pattern_type":"news"},
    "产业市场-医药-行业动态": {"url":"http://www.ce.cn/cysc/yy/hydt/", "pub_date_format":["%Y/%m/%d %H:%M","%Y年%m月%d日 %H:%M","%Y-%m-%d %H:%M"],"next_list_url_generator":default_generate_next_list_url,"short_name":"yyhydt", "pattern_type":"news"},
    "产业市场-医药-黑红榜": {"url":"http://www.ce.cn/cysc/yy/yyhhb/", "pub_date_format":["%Y/%m/%d %H:%M","%Y年%m月%d日 %H:%M","%Y-%m-%d %H:%M"],"next_list_url_generator":default_generate_next_list_url,"short_name":"yyhhb", "pattern_type":"yy"},
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


