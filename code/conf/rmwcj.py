# -*- coding: utf-8 -*-
from .common import *

website_name = "人民网"
website_short_name = "rmwcj"
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
            '<h5><a href=\'(?P<url>.*?)\'.*?>(?P<title>.*?)<\/a><\/h5>'
        ],
        "news_patterns" : [
            r'<h5>.*?\/>(?P<pub_date>.*?)来源：(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/h5>.*?<div class="pic">(?P<content>.*?)<div class="zdfy clearfix">',
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="来源：(?P<source>.*?)">.*?<div class="box_pic">(?P<content>.*?)<div class=\"box_pic\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>',  
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="来源：(?P<source>.*?)">.*?<div class="otitle">(?P<content>.*?)<div class=\"box_pic\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>', 
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="来源：(?P<source>.*?)">.*?<div class="title">(?P<content>.*?)<div class=\"edit clearfix\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>',
            ]
    },
        "gj":{
        "list_patterns" : [
            "<strong><a href=\'(?P<url>.*?)\' target=\"_blank\">(?P<title>.*?)<\/a><\/strong>"
        ],
        "news_patterns" : [
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="来源：(?P<source>.*?)">.*?<div class="box_pic">(?P<content>.*?)<div class=\"box_pic\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>',  
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="来源：(?P<source>.*?)">.*?<div class="otitle">(?P<content>.*?)<div class=\"box_pic\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>', 
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="来源：(?P<source>.*?)">.*?<div class="title">(?P<content>.*?)<div class=\"edit clearfix\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>',
           
           
        ]
    },
     "fc":{
        "list_patterns" : [
            "<li><a href=\'(?P<url>.*?)\' target=_blank>(?P<title>.*?)<\/a> <i class=\"gray\">(?P<pub_date>.*?)<\/i>"
        ],
        "news_patterns" : [
            '<meta name=\"publishdate\" content=\".*?\">.*?<meta name=\"source\" content=\"来源：(?P<source>.*?)\">.*?<div class=\"title\">(?P<content>.*?)<div class=\"edit clearfix\">.*?<i id=\"p_editor">(\(责编：)?(?P<author>.*?)(\))?<\/i>',
            '<meta name=\"publishdate\" content=\".*?\">.*?<meta name=\"source\" content=\"来源：(?P<source>.*?)\">.*?<div class=\"otitle\">(?P<content>.*?)<div class=\"box_pic\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>',
            '<meta name=\"publishdate\" content=\".*?\">.*?<meta name=\"source\" content=\"来源：(?P<source>.*?)\">.*?<div class=\"box_pic\">(?P<content>.*?)<div class=\"box_pic\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>',
            '<meta name=\"publishdate\" content=\".*?\">.*?<meta name=\"source\" content=\"来源：(?P<source>.*?)\">.*?<div class=\"box_pic\">(?P<content>.*?)<div class=\"box_pic\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>'
        ]
    },
    "cydc":{
        "list_patterns" : [
            "<h3 class=\"content-title\"><a href=\'(?P<url>.*?)\' target=\"_blank\">(?P<title>.*?)<\/a><\/h3>"
        ],
        "news_patterns" : [
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="来源：(?P<source>.*?)">.*?<div class="box_pic">(?P<content>.*?)<div class=\"box_pic\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>',  
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="来源：(?P<source>.*?)">.*?<div class="otitle">(?P<content>.*?)<div class=\"box_pic\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>', 
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="来源：(?P<source>.*?)">.*?<div class="title">(?P<content>.*?)<div class=\"edit clearfix\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>',
            ]
    },
    "lppd":{
        "list_patterns" : [
            "<h5><a href=\'(?P<url>.*?)\' target=\"_blank\">(?P<title>.*?)<\/a><\/h5>"
        ],
        "news_patterns" : [
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="(来源：)?(?P<source>.*?)">.*?<div class="box_pic">(?P<content>.*?)<div class=\"box_pic\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>',  
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="(来源：)?(?P<source>.*?)">.*?<div class="otitle">(?P<content>.*?)<div class=\"box_pic\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>', 
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="(来源：)?(?P<source>.*?)">.*?<div class="title">(?P<content>.*?)<div class=\"edit clearfix\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>',
            ]
    },
    "qc":{
        "list_patterns" : [
            "<dt><a href=\'(?P<url>.*?)\' target=\"_blank\">(?P<title>.*?)<\/a><\/dt>"
        ],
        "news_patterns" : [
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="来源：(?P<source>.*?)">.*?<div class="box_pic">(?P<content>.*?)<div class=\"box_pic\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>',  
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="来源：(?P<source>.*?)">.*?<div class="otitle">(?P<content>.*?)<div class=\"box_pic\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>', 
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="来源：(?P<source>.*?)">.*?<div class="title">(?P<content>.*?)<div class=\"edit clearfix\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>',
            ]
    },
    "it":{
        "list_patterns" : [
            "<strong><a href=\'(?P<url>.*?)\' target=_blank>(?P<title>.*?)<\/a><\/strong>"
        ],
        "news_patterns" : [
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="来源：(?P<source>.*?)">.*?<div class="box_pic">(?P<content>.*?)<div class=\"box_pic\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>',  
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="来源：(?P<source>.*?)">.*?<div class="otitle">(?P<content>.*?)<div class=\"box_pic\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>', 
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="来源：(?P<source>.*?)">.*?<div class="title">(?P<content>.*?)<div class=\"edit clearfix\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>',
            ]
    },
    "ny":{
        "list_patterns" : [
            "<strong><a href=\'(?P<url>.*?)\' target=\"_blank\">(?P<title>.*?)<\/a><\/strong>"
        ],
        "news_patterns" : [
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="来源：(?P<source>.*?)">.*?<div class="box_pic">(?P<content>.*?)<div class=\"box_pic\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>',  
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="来源：(?P<source>.*?)">.*?<div class="otitle">(?P<content>.*?)<div class=\"box_pic\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>', 
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<meta name="source" content="来源：(?P<source>.*?)">.*?<div class="title">(?P<content>.*?)<div class=\"edit clearfix\"><\/div>.*?\"edit clearfix\">(\(责编：)?(?P<author>.*?)(\))?<\/div>',
            r'<meta name="publishdate" content="(?P<pub_date>.*?)">.*?<h1>(?P<title>.*?)<\/h1>.*?<div class="box_pic">.*?</div>(?P<content>.*?)\s?来源：(?P<source>.*?)<\/p>',
            ]
    }
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            crawler.page_num+=1
            crawler.list_url_tpl = crawler.list_url_tpl+"index%d.html"
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

def ny_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url = crawler.list_url_tpl
            crawler.page_num+=1
            crawler.list_url_tpl = crawler.list_url_tpl+"index%d.html"
            yield ret_url
        else:
            # crawler.page_num += 1
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

b_class_dict = {
    "时政": {"url":"http://politics.people.com.cn/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"sz", "pattern_type":"news"},
    # "国际": {"url":"http://world.people.com.cn/", "pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"gj", "pattern_type":"gj"},
    "财经": {"url":"http://finance.people.com.cn/","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"cj", "pattern_type":"news"},
    "房产": {"url":"http://house.people.com.cn/GB/194441/", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"fc", "pattern_type":"fc"},
    "品牌房企-房产": {"url":"http://house.people.com.cn/GB/164306/", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"ppfq", "pattern_type":"fc"},
    "产业地产-房产": {"url":"http://house.people.com.cn/GB/395478/","ckpt_days":300,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url, "short_name":"cydc", "pattern_type":"cydc"},
    "楼盘频道-房产": {"url":"http://house.people.com.cn/GB/395441/","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"lppd", "pattern_type":"lppd"},
    "宏观政策": {"url":"http://house.people.com.cn/GB/167739/", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"hgzc", "pattern_type":"fc"},
    "人民出品": {"url":"http://house.people.com.cn/GB/164291/", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"rmcp", "pattern_type":"fc"},
    "住房保障": {"url":"http://house.people.com.cn/GB/164315/", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"zfbz", "pattern_type":"fc"},
    "各地楼市": {"url":"http://house.people.com.cn/GB/164305/", "pub_date_format":"%Y-%m-%d %H:%M","next_list_url_generator":default_generate_next_list_url,"short_name":"gdls", "pattern_type":"fc"},
    "汽车-独家": {"url":"http://auto.people.com.cn/GB/1052/98358/98363/","ckpt_days":300, "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"qc_dj", "pattern_type":"qc"},
    "汽车-国内新闻": {"url":"http://auto.people.com.cn/GB/1049/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"qc_gnxw", "pattern_type":"qc"},
    "汽车-国际新闻": {"url":"http://auto.people.com.cn/GB/173005/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"qc_gjxw", "pattern_type":"qc"},
    "汽车-政策法规": {"url":"http://auto.people.com.cn/GB/1051/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"qc_zcfg", "pattern_type":"qc"},
    "汽车-行业动态": {"url":"http://auto.people.com.cn/GB/14555/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"qc_hydt", "pattern_type":"qc"},
    "汽车-价格行情": {"url":"http://auto.people.com.cn/GB/1052/25089/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"qc_jghq", "pattern_type":"qc"},
    "汽车-人民汽车抢先测": {"url":"http://auto.people.com.cn/GB/10309/120257/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"qc_rmqcqxc", "pattern_type":"qc"},
    "汽车-汽车导购": {"url":"http://auto.people.com.cn/GB/1052/27602/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"qc_qcdg", "pattern_type":"qc"},
    "汽车-上市新车": {"url":"http://auto.people.com.cn/GB/1052/81336/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"qc_ssxc", "pattern_type":"qc"},
    "汽车-汽车财经": {"url":"http://auto.people.com.cn/GB/174271/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"qc_qccj", "pattern_type":"qc"},
    "汽车-观点评论": {"url":"http://auto.people.com.cn/GB/1050/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"qc_gdpl", "pattern_type":"qc"},
    "IT-新闻": {"url":"http://it.people.com.cn/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"it_xw", "pattern_type":"it"},
    "旅游": {"url":"http://travel.people.com.cn/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url, "short_name":"ly", "pattern_type":"lppd"},
    "能源": {"url":"http://energy.people.com.cn/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":ny_generate_next_list_url,"short_name":"ny", "pattern_type":"ny"},
    "环保": {"url":"http://env.people.com.cn/", "pub_date_format":"%Y-%m-%d","next_list_url_generator":ny_generate_next_list_url,"short_name":"hb", "pattern_type":"ny"},
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


