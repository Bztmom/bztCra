# -*- coding: utf-8 -*-
from .common import *

website_name = "中国改革报"
website_short_name = "zgggb_new"
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
            '<li><span class="newsTitle">·<a   href="(?P<url>.*?)"  target="_blank">(?P<title>.*?)<\/a><\/span><span class="pubTime">(?P<pub_date>.*?)<\/span><\/li>'
        ],
        "news_patterns" : [
            '<div id=\"contentMsg\">.*?\"pubTime\">(.*?)<\/span>.*?\"source\">来源：(<a.*?>)?(《)?(?P<source>.*?)(》)?(<\/a>)?<\/span>.*?contentMain\">.*?<!--enpcontent-->(?P<content>.*?)<!--\/enpcontent-->.*?contentLiability\">\[责任编辑:(?P<author>.*?)\]<\/div>',
        ]
    },
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 1:
        if crawler.page_num == 0:
            crawler.page_num+=1
            crawler.normal=crawler.list_url_tpl
            ret_url = crawler.list_url_tpl.replace("_%d","")
            yield ret_url
        else:
            ret_url = crawler.normal % (crawler.page_num)
            crawler.page_num += 1
            yield ret_url

def qt_generate_next_list_url(crawler):
    while crawler.page_num < 1:
        if crawler.page_num == 0:
            # crawler.page_num+=1
            ret_url = crawler.list_url_tpl
            crawler.list_url_tpl+="?%d"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            # crawler.page_num += 1
            yield ret_url

b_class_dict = {
    "时政": {"url":"http://www.crd.net.cn/node_31602.htm","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url, "short_name":"sz", "pattern_type":"news"},
    "民生": {"url":"http://www.crd.net.cn/node_31505.htm","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url, "short_name":"ms", "pattern_type":"news"},
    "宏观": {"url":"http://www.crd.net.cn/node_31597.htm", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url, "short_name":"hg", "pattern_type":"news"},
    "结构": {"url":"http://www.crd.net.cn/node_31510.htm", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url, "short_name":"jg", "pattern_type":"news"},
    "产业": {"url":"http://www.crd.net.cn/node_31509.htm","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url, "short_name":"cy", "pattern_type":"news"},
    "公司": {"url":"http://www.crd.net.cn/node_31508.htm","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url, "short_name":"gs", "pattern_type":"news"},
    "瞭望": {"url":"http://www.crd.net.cn/node_31590.htm", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url, "short_name":"lw", "pattern_type":"news"},
    "观点": {"url":"http://www.crd.net.cn/node_31512.htm","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url, "short_name":"gd", "pattern_type":"news"},
    "医疗改革": {"url":"http://www.crd.net.cn/node_23161.htm","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url, "short_name":"ylgg", "pattern_type":"news"},
    "上市公司": {"url":"http://www.crd.net.cn/node_31557.htm", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url, "short_name":"ssgs", "pattern_type":"news"},
    "发展改革新闻": {"url":"http://www.crd.net.cn/node_31567.htm","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url, "short_name":"fzggxw", "pattern_type":"news"},
    "新闻纵深": {"url":"http://www.crd.net.cn/node_31585.htm","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url, "short_name":"xwzs", "pattern_type":"news"},
    "要闻-高层动态": {"url":"http://www.crd.net.cn/node_31601.htm", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url, "short_name":"yw_gcdt", "pattern_type":"news"},
    "要闻-报道专题": {"url":"http://www.crd.net.cn/node_31628.htm", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url, "short_name":"yw_bdzt", "pattern_type":"news"},
    "要闻-权威发布": {"url":"http://www.crd.net.cn/node_31499.htm","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url, "short_name":"yw_qwfb", "pattern_type":"news"},
    "要闻-政务信息": {"url":"http://www.crd.net.cn/node_31502.htm","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,  "short_name":"yw_zwxx", "pattern_type":"news"},
    "社会-舆情观察": {"url":"http://www.crd.net.cn/node_31503.htm","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url, "short_name":"sh-yqgc", "pattern_type":"news"},
    "社会-报道专题": {"url":"http://www.crd.net.cn/node_31629.htm", "pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"sh-bdzt", "pattern_type":"news"},
    "社会-科教前沿": {"url":"http://www.crd.net.cn/node_31504.htm","pub_date_format":"%Y-%m-%d",  "next_list_url_generator":default_generate_next_list_url,"short_name":"sh-kjqy", "pattern_type":"news"},
    "经济-宏观调控": {"url":"http://www.crd.net.cn/node_31597.htm", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url, "short_name":"jj-hgtk", "pattern_type":"news"},
    "经济-结构调整": {"url":"http://www.crd.net.cn/node_31510_%d.htm","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url, "short_name":"jj-jgtz", "pattern_type":"news"},
    "经济-报道专题": {"url":"http://www.crd.net.cn/node_31630.htm","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url, "short_name":"jj-bdzt", "pattern_type":"news"},
    "经济-公司在线": {"url":"http://www.crd.net.cn/node_31508.htm","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url, "short_name":"jj-gszx", "pattern_type":"news"},
    "经济-资本市场": {"url":"http://www.crd.net.cn/node_31507.htm","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url, "short_name":"jj-zbsc", "pattern_type":"news"},
    "国际-热点播报": {"url":"http://www.crd.net.cn/node_31591.htm", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url, "short_name":"gj-rdbb", "pattern_type":"news"},
    "国际-国际论道": {"url":"http://www.crd.net.cn/node_31589.htm", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url, "short_name":"gj-gjld", "pattern_type":"news"},
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


