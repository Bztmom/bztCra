# -*- coding: utf-8 -*-
from .common import *
import re
from XX_Crawler.Utils import get

website_name = "南方财富网"
website_short_name = "nfcfw"
data_path = "../data/"
ckpt_path = "../ckpt/"
log_path = "../log/"
default_ckpt_days = 50
default_log_level = "info"

def multi_news_page(self, news_info, content):
    page_info_pattern = re.compile(
        r'<div class="multipage">(?P<page_div>.*?)<\/div>', re.DOTALL)
    page_pattern = re.compile(r'<a>共(?P<page_num>\d)页', re.DOTALL)
    content_pattern = re.compile(r'<div class="articleCon">(?P<content>.*?)<div class="multipage">', re.DOTALL)
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
            next_url = cur_url[:-5] + "_%d" %(page_num) + cur_url[-5:]
            page_content = get(next_url)
            self.logger.debug("get next page %s"%next_url)
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
            r'<li>.*?<a href="(?P<url>.*?)">(?P<title>.*?)<\/a>.*?<span class="date">(?P<pub_date>.*?)<\/span>.*?<\/li>'
        ],
        "news_patterns" : [
            r'来源 begin-->\s+(来源：)?(?P<source>.*?)<!-- 来源end -->.*?<div class="articleCon">(?P<content>.*?)南方财富网微信号',
            r'<div class="articleCon">(?P<content>.*?)南方财富网微信号',
            ]
    },

}


def yw_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            crawler.totalpage =0
            ret_url=crawler.list_url_tpl
            temp=crawler.get(ret_url,header=None)
            temp = temp.decode("gbk","ignore").encode("utf-8")
            source_pattern=re.compile('<li><span class=\"pageinfo\">共 <strong>(.*?)<\/strong>')
            source_data=source_pattern.search(temp)
            crawler.totalpage = int(source_data.group(1))
            crawler.list_url_tpl = "http://www.southmoney.com/caijing/caijingyaowen/list_44_"+"%d.html"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.totalpage-crawler.page_num)
            yield ret_url

b_class_dict = {
    "财经-要闻": {"url":"http://www.southmoney.com/caijing/caijingyaowen/", "pub_date_format":"%Y/%m/%d","next_list_url_generator":yw_generate_next_list_url,"short_name":"cj_yw", "pattern_type":"news"},
    "财经-股市评论": {"url":"http://www.southmoney.com/caijing/gushipinglun/", "pub_date_format":"%Y/%m/%d","next_list_url_generator":yw_generate_next_list_url,"short_name":"cj_gspl", "pattern_type":"news"},
    "财经-公司新闻": {"url":"http://www.southmoney.com/caijing/gongsixinwen/", "pub_date_format":"%Y/%m/%d","next_list_url_generator":yw_generate_next_list_url,"short_name":"cj_gsxw", "pattern_type":"news"},
    "财经-热点": {"url":"http://www.southmoney.com/caijing/redian/", "pub_date_format":"%Y/%m/%d","next_list_url_generator":yw_generate_next_list_url,"short_name":"cj_rd", "pattern_type":"news"},
    "财经-观察": {"url":"http://www.southmoney.com/caijing/caijingguanch/", "pub_date_format":"%Y/%m/%d","next_list_url_generator":yw_generate_next_list_url,"short_name":"cj_gc", "pattern_type":"news"},
    "个股-行情": {"url":"http://www.southmoney.com/hangqing/", "pub_date_format":"%Y/%m/%d","next_list_url_generator":yw_generate_next_list_url,"short_name":"gg_hq", "pattern_type":"news"},
    "个股-分析": {"url":"http://www.southmoney.com/fenxi/", "pub_date_format":"%Y/%m/%d","next_list_url_generator":yw_generate_next_list_url,"short_name":"gg_fx", "pattern_type":"news"},
    "个股-点评": {"url":"http://www.southmoney.com/dianping/", "pub_date_format":"%Y/%m/%d","next_list_url_generator":yw_generate_next_list_url,"short_name":"gg_dp", "pattern_type":"news"},
    "个股-推荐": {"url":"http://www.southmoney.com/tuijian/", "pub_date_format":"%Y/%m/%d","next_list_url_generator":yw_generate_next_list_url,"short_name":"gg_tj", "pattern_type":"news"},
    "个股-评级": {"url":"http://www.southmoney.com/gegu/ggpj/", "pub_date_format":"%Y/%m/%d","next_list_url_generator":yw_generate_next_list_url,"short_name":"gg_pj", "pattern_type":"news"},
    
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
                "base_url":"http://www.southmoney.com/",
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


