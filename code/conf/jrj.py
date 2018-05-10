# -*- coding: utf-8 -*-
from .common import *

website_name = "金融界"
website_short_name = "jrj"
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
            r'<li><i>(?P<pub_date>.*?)<\/i><a href="(?P<url>.*?)">(?P<title>.*?)<\/a><\/li>'
        ],
        "news_patterns" : [
            r'<span>来源：<!--jrj_final_source_start-->(<a.*?>)?(?P<source>.*?)(<\/a>)?<!--jrj_final_source_end-->.*?(作者：<!--jrj_final_author_start-->(?P<author>.*?)<!--jrj_final_author_end-->.*?)?<div class="texttit_m1">(?P<content>.*?)<!--jrj_final_context_end-->.*?责任编辑：(.*?)<\/span>',
            r'<span>来源：<!--jrj_final_source_start--><!--jrj_final_source_end-->.*?<A.*?>(?P<source>.*?)<\/A>.*?(作者：<!--jrj_final_author_start-->(?P<author>.*?)<!--jrj_final_author_end-->.*?)?<div class="texttit_m1">(?P<content>.*?)<!--jrj_final_context_end-->.*?责任编辑：(.*?)<\/span>',
       ]
    },
    "xfbgt":{
        "list_patterns" : [
            r'<li><label><a href="(?P<url>.*?)" target="_blank" title=(?P<title>.*?)>(.*?)<\/a><\/label>(?P<pub_date>.*?)<\/li>'
        ],
        "news_patterns" : [
            r'<span>来源：<!--jrj_final_source_start-->(<a.*?>)?(?P<source>.*?)(<\/a>)?<!--jrj_final_source_end-->.*?(作者：<!--jrj_final_author_start-->(?P<author>.*?)<!--jrj_final_author_end-->.*?)?<div class="texttit_m1">(?P<content>.*?)<!--jrj_final_context_end-->.*?责任编辑：(.*?)<\/span>',
            r'<span>来源：<!--jrj_final_source_start--><!--jrj_final_source_end-->.*?<A.*?>(?P<source>.*?)<\/A>.*?(作者：<!--jrj_final_author_start-->(?P<author>.*?)<!--jrj_final_author_end-->.*?)?<div class="texttit_m1">(?P<content>.*?)<!--jrj_final_context_end-->.*?责任编辑：(.*?)<\/span>',
       ]
    },
    "ssgs":{
        "list_patterns" : [
            r'<li><span>(?P<pub_date>.*?)<\/span><a href="(?P<url>.*?)" title="(?P<title>.*?)">.*?<\/a><\/li>'
        ],
        "news_patterns" : [
            r'<span>来源：<!--jrj_final_source_start-->(<a.*?>)?(?P<source>.*?)(<\/a>)?<!--jrj_final_source_end-->.*?(作者：<!--jrj_final_author_start-->(?P<author>.*?)<!--jrj_final_author_end-->.*?)?<div class="texttit_m1"><P align=center></P>\s*?<div.*?</script>\s*<\/div>(?P<content>.*?)<!--jrj_final_context_end-->.*?责任编辑：(.*?)<\/span>',
            r'<span>来源：<!--jrj_final_source_start-->(<a.*?>)?(?P<source>.*?)(<\/a>)?<!--jrj_final_source_end-->.*?(作者：<!--jrj_final_author_start-->(?P<author>.*?)<!--jrj_final_author_end-->.*?)?<div class="texttit_m1">(?P<content>.*?)<!--jrj_final_context_end-->.*?责任编辑：(.*?)<\/span>',
            r'<span>来源：<!--jrj_final_source_start--><!--jrj_final_source_end-->.*?<A.*?>(?P<source>.*?)<\/A>.*?(作者：<!--jrj_final_author_start-->(?P<author>.*?)<!--jrj_final_author_end-->.*?)?<div class="texttit_m1">(?P<content>.*?)<!--jrj_final_context_end-->.*?责任编辑：(.*?)<\/span>',
       ]
    },
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 3:
        if crawler.page_num == 0:
            ret_url=crawler.list_url_tpl
            crawler.page_num+=1
            crawler.list_url_tpl = crawler.list_url_tpl[:-6]+"-%d.shtml"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url


b_class_dict = {
    "今日财经": {"url":"http://finance.jrj.com.cn/list/cjgundong.shtml", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"jrcj", "pattern_type":"news"},
    "国内财经": {"url":"http://finance.jrj.com.cn/list/guoneicj.shtml", "pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"gncj", "pattern_type":"news"},
    "国际财经": {"url":"http://finance.jrj.com.cn/list/guojicj.shtml","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"gjcj", "pattern_type":"news"},
    "产经新闻": {"url":"http://finance.jrj.com.cn/list/industrynews.shtml","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"cjxw", "pattern_type":"news"},
    "商业资讯": {"url":"http://biz.jrj.com.cn/biz_index.shtml", "pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"syzx", "pattern_type":"news"},
    "消费者曝光": {"url":"http://finance.jrj.com.cn/consumer/","pub_date_format":"%Y/%m/%d %H:%M", "next_list_url_generator":default_generate_next_list_url,"short_name":"xfzbg", "pattern_type":"xfbgt"},
    "最精华": {"url":"http://opinion.jrj.com.cn/list/zjh.shtml", "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"zjh", "pattern_type":"news"},
    "经济时评": {"url":"http://opinion.jrj.com.cn/list/jjsp.shtml", "pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"jjsp", "pattern_type":"news"},
    "产业观察": {"url":"http://opinion.jrj.com.cn/list/cygc.shtml","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"cygc", "pattern_type":"news"},
    "民生杂谈": {"url":"http://opinion.jrj.com.cn/list/mszt.shtml", "pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"mszt", "pattern_type":"news"},
    "海外视角": {"url":"http://opinion.jrj.com.cn/list/wmkzg.shtml","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"hwsj", "pattern_type":"news"},
    "谈股论今": {"url":"http://opinion.jrj.com.cn/list/tglj.shtml","pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"tglj", "pattern_type":"news"},
    "媒体热评": {"url":"http://opinion.jrj.com.cn/list/mtrp.shtml", "pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"mtrp", "pattern_type":"news"},
    "资本市场": {"url":"http://finance.jrj.com.cn/list/zbsc.shtml", "pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"zbsc", "pattern_type":"news"},
    "科技资讯": {"url":"http://finance.jrj.com.cn/tech/", "pub_date_format":"%Y-%m-%d", "next_list_url_generator":default_generate_next_list_url,"short_name":"kjzx", "pattern_type":"news"},
    "市场分析": {"url":"http://stock.jrj.com.cn/invest/scgc.shtml", "pub_date_format":"%Y-%m-%d  %H:%M", "next_list_url_generator":default_generate_next_list_url,"short_name":"scfx", "pattern_type":"ssgs"},
    "新三板": {"url":"http://stock.jrj.com.cn/list/stocksbsc.shtml", "pub_date_format":"%Y-%m-%d  %H:%M", "next_list_url_generator":default_generate_next_list_url,"short_name":"xsb", "pattern_type":"ssgs"},
    "股市资讯": {"url":"http://stock.jrj.com.cn/list/stockgszx.shtml", "pub_date_format":"%Y-%m-%d  %H:%M", "next_list_url_generator":default_generate_next_list_url,"short_name":"gszx", "pattern_type":"ssgs"},
    "上市公司": {"url":"http://stock.jrj.com.cn/list/stockssgs.shtml", "pub_date_format":"%Y-%m-%d  %H:%M", "next_list_url_generator":default_generate_next_list_url,"short_name":"ssgs", "pattern_type":"ssgs"},

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
                "encoding":"gb2312",
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


