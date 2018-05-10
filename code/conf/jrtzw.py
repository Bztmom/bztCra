# -*- coding: utf-8 -*-
from .common import *

website_name = "金融投资网"
website_short_name = "jrtzw"
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
            r'class="tit">(?P<title>.*?)<\/a>.*?<p class="txt">(.*?)<\/p>.*?<div class="btns"><span class="time">(?P<pub_date>.*?)<\/span><span class="msg">.*?<a href="(?P<url>.*?)" class="more">',
        ],
        "news_patterns" : [
            r'class="txt_from".*?>(?P<source>.*?)<\/a>.*?<div class="txt_body" id="txt_body">(?P<content>.*?)<div class="block">',
       ]
    },

}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url=crawler.list_url_tpl
            crawler.page_num+=1
            crawler.list_url_tpl = crawler.list_url_tpl[:-5]+"p=%d&"+crawler.list_url_tpl[-5:]
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url


b_class_dict = {
    "要闻": {"url":"http://www.jrtzb.com.cn/list.asp?c=346", "pub_date_format":"%Y/%m/%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"yw", "pattern_type":"news"},
    "股票": {"url":"http://www.jrtzb.com.cn/list.asp?c=347", "pub_date_format":"%Y/%m/%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"gp", "pattern_type":"news"},
    "基金": {"url":"http://www.jrtzb.com.cn/list.asp?c=348", "pub_date_format":"%Y/%m/%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"jj", "pattern_type":"news"},
    "银行": {"url":"http://www.jrtzb.com.cn/list.asp?c=349", "pub_date_format":"%Y/%m/%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"yh", "pattern_type":"news"},
    "保险": {"url":"http://www.jrtzb.com.cn/list.asp?c=350", "pub_date_format":"%Y/%m/%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"bx", "pattern_type":"news"},
    "理财超市": {"url":"http://www.jrtzb.com.cn/list.asp?c=351", "pub_date_format":"%Y/%m/%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"lccs", "pattern_type":"news"},
    "新三板-公司新闻": {"url":"http://www.jrtzb.com.cn/list.asp?c=380", "pub_date_format":"%Y/%m/%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"gsxw", "pattern_type":"news"},
    "新三板-个股看台": {"url":"http://www.jrtzb.com.cn/list.asp?c=378", "pub_date_format":"%Y/%m/%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"ggkt", "pattern_type":"news"},
    "新三板-动态": {"url":"http://www.jrtzb.com.cn/list.asp?c=379", "pub_date_format":"%Y/%m/%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"dt", "pattern_type":"news"},
    "新三板-今日行情": {"url":"http://www.jrtzb.com.cn/list.asp?c=375", "pub_date_format":"%Y/%m/%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"jrhq", "pattern_type":"news"},
    "新三板-一周综述": {"url":"http://www.jrtzb.com.cn/list.asp?c=376", "pub_date_format":"%Y/%m/%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"yzzs", "pattern_type":"news"},
    "创新创业": {"url":"http://www.jrtzb.com.cn/list.asp?c=356", "pub_date_format":"%Y/%m/%d %H:%M:%S","next_list_url_generator":default_generate_next_list_url,"short_name":"cxcy", "pattern_type":"news"},
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
                "base_url":"http://www.jrtzb.com.cn",
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


