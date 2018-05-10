# -*- coding: utf-8 -*-
from .common import *
import re
from XX_Crawler.Utils import get
website_name = "证券之星"
website_short_name = "zqzx"
data_path = "../data/"
ckpt_path = "../ckpt/"
log_path = "../log/"
default_ckpt_days = 50
default_log_level = "info"

def multi_news_page(self, news_info, content):
    page_info_pattern = re.compile(
        r'<div id="Page">(?P<page_div>.*?)<\/div>', re.DOTALL)
    page_pattern = re.compile(r'\.shtml" target="_self">(?P<page_num>\d)<\/a> <span class="edit">', re.DOTALL)
    content_pattern = re.compile(r'<div class="article".*?>(?P<content>.*?)<!--.*?published at .*?-->', re.DOTALL)
    page_info_data = page_info_pattern.search(content)
    if page_info_data:
        # print page_info_data.group(1)
        page_div = page_info_data.group("page_div")
        max_page_num = 1
        for m in page_pattern.finditer(page_div):
            cur_page_num = int(m.group("page_num"))
            if cur_page_num > max_page_num:
                max_page_num = cur_page_num
        self.logger.debug(
            "there are %d pages for this news" % (max_page_num))
        cur_url = news_info["url"]
        for page_num in xrange(2, max_page_num+1):
            # next page url is t2017-10-09_32432432.html =>t2017-10-09_32432432_2.html
            next_url = cur_url[:-6] + "_%d" %(page_num) + cur_url[-6:]
            page_content = get(next_url)
            self.logger.debug("got next page %s"%next_url)
            if page_content is not None:
                m = content_pattern.search(page_content.decode("gbk"))
                if m:
                    self.logger.debug("yield next_page content")
                    self.logger.debug(m.group("content"))
                    yield m.group("content")
    pass

conf = {
    "domain_name": website_name,
    "pipelines": [
        
    ]  # end of pipelines for a website
}  # end of config of a website
pattern_conf = {"news":{
        "list_patterns" : [
            r'<li><span>(?P<pub_date>.*?)<\/span><a href="(?P<url>.*?)">(?P<title>.*?)<\/a><\/li>'
        ],
        "news_patterns" : [
            r'来源：(<a.*?>)?(?P<source>.*?)(<\/a>)<\/span>.*?<div class="article".*?>(?P<content>.*?)<!--.*?published at .*?-->',
            r'<span id="source_baidu".*?>(<a.*?>)?(?P<source>.*?)(<\/a>)?</span>.*?<div class="article".*?>(?P<content>.*?)<!--.*?published at .*?-->'
            ]
    },
        "gd":{
        "list_patterns" : [
            r'<li><span>(?P<pub_date>.*?)<\/span>(\[<a href=".*?">(.*?)<\/a>\]  )?<a href="(?P<url>.*?)">(?P<title>.*?)<\/a><\/li>'
        ],
        "news_patterns" : [
            r'来源：(<a.*?>)?(?P<source>.*?)(<\/a>)<\/span>.*?<div class="article".*?>(?P<content>.*?)<!--.*?published at .*?-->',
            r'<span id="source_baidu".*?>(<a.*?>)?(?P<source>.*?)(<\/a>)?</span>.*?<div class="article".*?>(?P<content>.*?)<!--.*?published at .*?-->'
            ]
    },
        "jjyw":{
        "list_patterns" : [
            r'<li>·<a href="(?P<url>.*?)">(?P<title>.*?)<\/a><\/li>.*?<li class="li_time">(?P<pub_date>.*?)<\/li>',
        ],
        "news_patterns" : [
            r'来源：(<a.*?>)?(?P<source>.*?)(<\/a>)<\/span>.*?<div class="article".*?>(?P<content>.*?)<!--.*?published at .*?-->',
            r'<span id="source_baidu".*?>(<a.*?>)?(?P<source>.*?)(<\/a>)?</span>.*?<div class="article".*?>(?P<content>.*?)<!--.*?published at .*?-->'
            ]
    }, 
        "guangchang":{
        "list_patterns" : [
            r'<li><span>(?P<pub_date>.*?)<\/span><a href="(?P<url>.*?)">(?P<title>.*?)<\/a><\/li>'
        ],
        "news_patterns" : [
            r'(作者：(<a.*?>)?(?P<author>.*?)(<\/a>)?<\/span>.*?)?来源：(<span.*?>)?(<a.*?>)?(?P<source>.*?)<\/span>(<\/a>)?.*?<div class="article".*?>(?P<content>.*?)复制链接',
           ]
    },
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 3:
        if crawler.page_num == 0:
            ret_url = crawler.list_url_tpl
            crawler.page_num+=1
            crawler.list_url_tpl = crawler.base_url+"_%d.shtml"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

def zxybsd_generate_next_list_url(crawler):
    ret_url = crawler.list_url_tpl
    yield ret_url

def guangchang_generate_next_list_url(crawler):
    while crawler.page_num < 3:
        if crawler.page_num == 0:
            crawler.page_num+=1
            ret_url=crawler.list_url_tpl
            crawler.list_url_tpl = crawler.list_url_tpl[:-6]+"%d"+".shtml"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

b_class_dict = {
    "股票-板块掘金": {"url":"http://stock.stockstar.com/list/sectors.htm", "base_url":"http://stock.stockstar.com/list/1577","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"sz", "pattern_type":"news"},
    "热点报道-财经聚焦": {"url":"http://www.stockstar.com/focus/", "base_url":"http://www.stockstar.com/focus/list_1223","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"cjjj", "pattern_type":"news"},
    "股票-证券要闻": {"url":"http://stock.stockstar.com/list/headlines.htm", "base_url":"http://www.stockstar.com/list/2","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"zqyw", "pattern_type":"news"},
    "股票-公司新闻": {"url":"http://stock.stockstar.com/list/10.shtml", "base_url":"http://www.stockstar.com/list/10","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"gsxw", "pattern_type":"news"},
    "股票-主流研究": {"url":"http://stock.stockstar.com/list/main.htm", "base_url":"http://stock.stockstar.com/list/2365","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"zlyj", "pattern_type":"news"},
    "股票-短线趋势": {"url":"http://stock.stockstar.com/list/short.htm", "base_url":"http://stock.stockstar.com/list/1031","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"dxqs", "pattern_type":"news"},
    "股票-中长线趋势": {"url":"http://stock.stockstar.com/list/long.htm", "base_url":"http://stock.stockstar.com/list/96","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"zcxqs", "pattern_type":"news"},
    "最新研报速递": {"url":"http://stock.stockstar.com/report/", "base_url":None,"pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":zxybsd_generate_next_list_url,"short_name":"zxybsd", "pattern_type":"news"},
    "最新公司研究": {"url":"http://stock.stockstar.com/report_list/report1.htm", "base_url":"http://stock.stockstar.com/list/3491","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"zxgsyj", "pattern_type":"news"},
    "研究报告查询": {"url":"http://stock.stockstar.com/report_list/report2.htm", "base_url":"http://stock.stockstar.com/list/3489","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"yjbgcx", "pattern_type":"news"},
    "策略趋势": {"url":"http://stock.stockstar.com/list/4019_2.shtml", "base_url":"http://stock.stockstar.com/list/4019","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"clqs", "pattern_type":"news"},
    "券商晨会": {"url":"http://stock.stockstar.com/report_list/report4.htm", "base_url":"http://stock.stockstar.com/list/4021","ckpt_days":300,"pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"qsch", "pattern_type":"news"},
    "宏观研究": {"url":"http://stock.stockstar.com/report_list/report5.htm", "base_url":"http://stock.stockstar.com/list/2739","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"hgyj", "pattern_type":"news"},
    "基金-基金要闻": {"url":"http://fund.stockstar.com/list/1293.shtml", "base_url":"http://fund.stockstar.com/list/1293","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"jjyw", "pattern_type":"jjyw"},
    "财经-名家观点": {"url":"http://finance.stockstar.com/list/1303.shtml", "base_url":"http://finance.stockstar.com/list/1303","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"mjgd", "pattern_type":"news"},
    "财经-国内经济": {"url":"http://finance.stockstar.com/list/1221.shtml", "base_url":"http://finance.stockstar.com/list/1221","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"gnjj", "pattern_type":"news"},
    "财经-行业新闻": {"url":"http://finance.stockstar.com/list/2921.shtml", "base_url":"http://finance.stockstar.com/list/2921","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"hyxw", "pattern_type":"news"},
    "财经-国际要闻": {"url":"http://finance.stockstar.com/list/955.shtml", "base_url":"http://finance.stockstar.com/list/955","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"gjyw", "pattern_type":"news"},
    "财经-公司新闻": {"url":"http://finance.stockstar.com/list/2863.shtml", "base_url":"http://finance.stockstar.com/list/2863","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"gsxw", "pattern_type":"news"},
    "财经-全球市场": {"url":"http://finance.stockstar.com/list/global.htm", "base_url":"http://finance.stockstar.com/list/1765","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"qqsc", "pattern_type":"news"},
    "滚动全部": {"url":"http://www.stockstar.com/roll/all.shtml", "base_url":"http://www.stockstar.com/roll/all","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"gd", "pattern_type":"gd"},
    "股票-新三板要闻": {"url":"http://stock.stockstar.com/list/third.htm", "base_url":"http://stock.stockstar.com/list/1615","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"xsbyw", "pattern_type":"news"},
    "股票-新三板公司": {"url":"http://stock.stockstar.com/list/5257.shtml", "base_url":"http://stock.stockstar.com/list/5257","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"xsbgs", "pattern_type":"news"},
    "股票-新三板学堂": {"url":"http://stock.stockstar.com/list/5165.shtml", "base_url":"http://stock.stockstar.com/list/5165","pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"xsbxt", "pattern_type":"news"},
    "媒体广场-国际金融": {"url":"http://finance.stockstar.com/list/media_4743_.shtml","base_url":None, "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":guangchang_generate_next_list_url,"short_name":"mtgc-gjjr", "pattern_type":"guangchang"},
    "媒体广场-金融时报": {"url":"http://finance.stockstar.com/list/media_4729_.shtml", "base_url":None,"pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":guangchang_generate_next_list_url,"short_name":"mtgc-jrsb", "pattern_type":"guangchang"},
    "媒体广场-经济观察报": {"url":"http://finance.stockstar.com/list/media_2793_.shtml", "base_url":None,"pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":guangchang_generate_next_list_url,"short_name":"mtgc-jjgcb", "pattern_type":"guangchang"},
    "媒体广场-每日经济新闻": {"url":"http://finance.stockstar.com/list/media_2785_.shtml", "base_url":None,"pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":guangchang_generate_next_list_url,"short_name":"mtgc-mrjjxw", "pattern_type":"guangchang"},
    "媒体广场-上海金融报": {"url":"http://finance.stockstar.com/list/media_2777_.shtml","base_url":None, "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":guangchang_generate_next_list_url,"short_name":"mtgc-shjrb", "pattern_type":"guangchang"},
    "媒体广场-时代周报": {"url":"http://finance.stockstar.com/list/media_4943_.shtml","base_url":None, "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":guangchang_generate_next_list_url,"short_name":"mtgc-sdzb", "pattern_type":"guangchang"},
    "媒体广场-投资者报": {"url":"http://finance.stockstar.com/list/media_4723_.shtml","base_url":None, "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":guangchang_generate_next_list_url,"short_name":"mtgc-tzzb", "pattern_type":"guangchang"},
    "媒体广场-证券日报": {"url":"http://finance.stockstar.com/list/media_2783_.shtml","base_url":None, "pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":guangchang_generate_next_list_url,"short_name":"mtgc-zqrb", "pattern_type":"guangchang"},
    "媒体广场-证券时报": {"url":"http://finance.stockstar.com/list/media_2781_.shtml", "base_url":None,"pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":guangchang_generate_next_list_url,"short_name":"mtgc-zqsb", "pattern_type":"guangchang"},
    "媒体广场-中国证券报": {"url":"http://finance.stockstar.com/list/media_2775_.shtml", "base_url":None,"pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":guangchang_generate_next_list_url,"short_name":"mtgc-zgzqb", "pattern_type":"guangchang"},
    "媒体广场-工商时报": {"url":"http://finance.stockstar.com/list/media_5009_.shtml", "base_url":None,"pub_date_format":"%Y-%m-%d %H:%M:%S","next_list_url_generator":guangchang_generate_next_list_url,"short_name":"mtgc-gssb", "pattern_type":"guangchang"},
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
                "base_url":info["base_url"],
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
                    "detail_patterns": pattern_conf[info["pattern_type"]]["news_patterns"],
                    "multi_news_page_func": multi_news_page,
                }
            },
            # {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },

        ],
        "uploader": online_mysql_uploader_conf
    }
    #print pipeline_conf
    conf["pipelines"].append(pipeline_conf)


