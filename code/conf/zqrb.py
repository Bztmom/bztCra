# -*- coding: utf-8 -*-
from .common import *

website_name = "证券日报网"
website_short_name = "zqrb"
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
            '<li><span class=\"date\">(?P<pub_date>.*?)<\/span>·<a title=\"(?P<title>.*?)\" href=\"(?P<url>.*?)\">.*?<\/a>'
        ],
        "news_patterns" : [
            r'文章来源：(<a.*?>)?(?P<source>.*?)(<\/a>)?(&nbsp;&nbsp;)?更新时间：.*?<!--con-->(?P<content>.*?)(<span class="author">(?P<author>.*?)<\/span>.*?)?<!--end-->',
            r'<div class="info_news">(?P<pub_date>.*?)来源：(?P<source>.*?)<\/div>.*?<!--con-->(?P<content>.*?)<!--end-->',
        ]
    },
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            crawler.page_num+=1
            crawler.list_url_tpl += "index_p%d.html"
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url


b_class_dict = {
    "证券要闻": {"url":"http://www.zqrb.cn/stock/gupiaoyaowen/", "next_list_url_generator":default_generate_next_list_url,"short_name":"zqyw", "pattern_type":"news"},
    "上市公司": {"url":"http://www.zqrb.cn/gscy/gongsi/","next_list_url_generator":default_generate_next_list_url, "short_name":"ssgs", "pattern_type":"news"},
    "板块聚焦": {"url":"http://www.zqrb.cn/stock/bankuaijujiao/","next_list_url_generator":default_generate_next_list_url, "short_name":"bkjj", "pattern_type":"news"},
    "最新播报": {"url":"http://www.zqrb.cn/stock/zuixinbobao/", "next_list_url_generator":default_generate_next_list_url,"short_name":"zxbb", "pattern_type":"news"},
    "个股评论": {"url":"http://www.zqrb.cn/stock/gegupinglun/", "next_list_url_generator":default_generate_next_list_url,"short_name":"ggpl", "pattern_type":"news"},
    "公司评级": {"url":"http://www.zqrb.cn/stock/gongsipingji/","next_list_url_generator":default_generate_next_list_url, "short_name":"gspj", "pattern_type":"news"},
    "公司研究": {"url":"http://www.zqrb.cn/stock/gongsiyanjiu/", "next_list_url_generator":default_generate_next_list_url,"short_name":"gsyj", "pattern_type":"news"},
    "环球股市": {"url":"http://www.zqrb.cn/stock/huanqiugushi/", "next_list_url_generator":default_generate_next_list_url,"short_name":"hqgs", "pattern_type":"news"},
    "B股": {"url":"http://www.zqrb.cn/stock/bstock/", "next_list_url_generator":default_generate_next_list_url,"short_name":"bg", "pattern_type":"news"},
    "中小板": {"url":"http://www.zqrb.cn/stock/zhongxiaoban/","next_list_url_generator":default_generate_next_list_url, "short_name":"zxb", "pattern_type":"news"},
    "保险": {"url":"http://www.zqrb.cn/jrjg/insurance/","next_list_url_generator":default_generate_next_list_url, "short_name":"bx", "pattern_type":"news"},
    "新股要闻": {"url":"http://www.zqrb.cn/ipo/yaowen/","next_list_url_generator":default_generate_next_list_url, "short_name":"xgyw", "pattern_type":"news"},
    "上市预测": {"url":"http://www.zqrb.cn/ipo/shangshiyuce/","next_list_url_generator":default_generate_next_list_url, "short_name":"ssyc", "pattern_type":"news"},
    "宏观经济": {"url":"http://www.zqrb.cn/finance/hongguanjingji/","next_list_url_generator":default_generate_next_list_url, "short_name":"hgjj", "pattern_type":"news"},
    "行业动态": {"url":"http://www.zqrb.cn/finance/hangyedongtai/","next_list_url_generator":default_generate_next_list_url, "short_name":"hydt", "pattern_type":"news"},
    "时事要闻": {"url":"http://www.zqrb.cn/shishiywen/", "next_list_url_generator":default_generate_next_list_url,"short_name":"ssyw", "pattern_type":"news"},
    "房产信息": {"url":"http://www.zqrb.cn/finace/house/", "next_list_url_generator":default_generate_next_list_url,"short_name":"fcxx", "pattern_type":"news"},
    "产经评论": {"url":"http://www.zqrb.cn/review/chanjingpinglun/","next_list_url_generator":default_generate_next_list_url, "short_name":"cjpl", "pattern_type":"news"},
    "国际聚焦": {"url":"http://www.zqrb.cn/review/guojijujiao/", "next_list_url_generator":default_generate_next_list_url,"short_name":"gjjj", "pattern_type":"news"},
    "汽车动态": {"url":"http://www.zqrb.cn/auto/qichedongtai/", "next_list_url_generator":default_generate_next_list_url,"short_name":"qcdt", "pattern_type":"news"},
    "四大证券报头条": {"url":"http://www.zqrb.cn/meiribidu/","ckpt_days":1500,"next_list_url_generator":default_generate_next_list_url, "short_name":"sdzqbtt", "pattern_type":"news"},
    "热点关注": {"url":"http://www.zqrb.cn/stock/redian/", "next_list_url_generator":default_generate_next_list_url,"short_name":"rdgz", "pattern_type":"news"},
    "民生消费": {"url":"http://www.zqrb.cn/finance/minshengxiaofei/", "next_list_url_generator":default_generate_next_list_url,"short_name":"msxf", "pattern_type":"news"},
    "国际要闻": {"url":"http://www.zqrb.cn/finance/guojijingji/", "next_list_url_generator":default_generate_next_list_url,"short_name":"gjyw", "pattern_type":"news"},
    "创业板": {"url":"http://www.zqrb.cn/stock/chuangyeban/", "next_list_url_generator":default_generate_next_list_url,"short_name":"cyb", "pattern_type":"news"},
    "银行": {"url":"http://www.zqrb.cn/jrjg/bank/", "next_list_url_generator":default_generate_next_list_url,"short_name":"yh", "pattern_type":"news"},
    "理财频道": {"url":"http://www.zqrb.cn/money/", "next_list_url_generator":default_generate_next_list_url,"short_name":"lcpd", "pattern_type":"news"},
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
                "pub_date_format":"%Y-%m-%d %H:%M",
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


