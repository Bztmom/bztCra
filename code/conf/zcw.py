# -*- coding: utf-8 -*-
from .common import *
import re
website_name = "中财网"
website_short_name = "zcw"
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
            r'<span>.*?<\/span>·<a href=(?P<url>.*?)>(?P<title>.*?)<\/a><br>'
        ],
        "news_patterns" : [
            r'<h1>(?P<title>.*?)<\/h1>.*?时间：(?P<pub_date>.*?)&nbsp(?P<source>.*?)<\/td>.*?<!--newstext-->(?P<content>.*?)<!--\/newstext-->',
       ]
    },
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
            ret_url=crawler.list_url_tpl
            temp=crawler.get(ret_url,header=None)
            temp = temp.decode("gbk","ignore").encode("utf-8")
            source_pattern=re.compile('<a href=\"index.aspx?(.*?)\"')
            source_data=source_pattern.search(temp)
            next_url = crawler.base_url+"index.aspx"+source_data.group(1)
            crawler.list_url_tpl = next_url
            yield ret_url
headers = {
    "hwgs" : {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Host" : "stock.cfi.cn",
        "Referer" : "http://stock.cfi.cn/BCA0A4127A4346A4445.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    },
    "jjxw" : {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Host" : "fund.cfi.cn",
        "Referer" : "http://fund.cfi.cn/BCA0A4127A5467A5483.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    },
    "gskd" : {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Host" : "industry.cfi.cn",
        "Referer" : "http://industry.cfi.cn/index.aspx?catid=A0A4127A4128A4142",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    }
}

b_class_dict = {
    "经济": {"url":"http://industry.cfi.cn/index.aspx?catid=A0A4127A4128A4132", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"jj", "pattern_type":"news"},
    "地产": {"url":"http://industry.cfi.cn/index.aspx?catid=A0A4127A4128A4138", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"dc", "pattern_type":"news"},
    "评论": {"url":"http://industry.cfi.cn/index.aspx?catid=A0A4127A4128A4133", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"pl", "pattern_type":"news"},
    "数据": {"url":"http://industry.cfi.cn/index.aspx?catid=A0A4127A4128A4134", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"sj", "pattern_type":"news"},
    "金融": {"url":"http://industry.cfi.cn/index.aspx?catid=A0A4127A4128A4135", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"jr", "pattern_type":"news"},
    "证券": {"url":"http://industry.cfi.cn/index.aspx?catid=A0A4127A4128A4136", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"zq", "pattern_type":"news"},
    "贸易": {"url":"http://industry.cfi.cn/index.aspx?catid=A0A4127A4128A4137", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"my", "pattern_type":"news"},
    "能源": {"url":"http://industry.cfi.cn/index.aspx?catid=A0A4127A4128A4139", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"ny", "pattern_type":"news"},
    "原材料": {"url":"http://industry.cfi.cn/index.aspx?catid=A0A4127A4128A4140", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"ycl", "pattern_type":"news"},
    "工业": {"url":"http://industry.cfi.cn/index.aspx?catid=A0A4127A4128A4141", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"gy", "pattern_type":"news"},
    "消费": {"url":"http://industry.cfi.cn/index.aspx?catid=A0A4127A4128A4142", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"xf", "pattern_type":"news"},
    "IT": {"url":"http://industry.cfi.cn/index.aspx?catid=A0A4127A4128A4143", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"it", "pattern_type":"news"},
    "行业聚焦": {"url":"http://industry.cfi.cn/index.aspx?catid=A0A4127A4128A4144", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"hyjj", "pattern_type":"news"},
    "国际": {"url":"http://industry.cfi.cn/index.aspx?catid=A0A4127A4128A4145", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"gj", "pattern_type":"news"},
    "沪港": {"url":"http://industry.cfi.cn/index.aspx?catid=A0A4127A4128A5063", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"hg", "pattern_type":"news"},
    "两会": {"url":"http://industry.cfi.cn/index.aspx?catid=A0A4127A4128A4495", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"lh", "pattern_type":"news"},
    "公司快递": {"url":"http://industry.cfi.cn/index.aspx?catid=A0A4127A4128A4142", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"gskd", "pattern_type":"news","header":headers['gskd']},
    "海外股市": {"url":"http://stock.cfi.cn/BCA0A4127A4346A4445.html", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"hwgs", "pattern_type":"news","base_url":"http://stock.cfi.cn/","header":headers['hwgs']},
    "基金新闻": {"url":"http://fund.cfi.cn/BCA0A4127A5467A5483.html", "pub_date_format":"%Y年%m月%d日 %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"jjxw", "pattern_type":"news","base_url":"http://fund.cfi.cn/","header":headers['jjxw']},
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
                "base_url":info.get("base_url","http://industry.cfi.cn/"),
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


