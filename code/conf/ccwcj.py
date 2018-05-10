# -*- coding: utf-8 -*-
from .common import *

website_name = "长城网财经"
website_short_name = "ccwcj"
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
            '<li><a href=\"(?P<url>http:\/\/finance.hebei.com.cn\/system(.*?))\" target=\"_blank\" title=\"(?P<title>.*?)\">(.*?)<\/a><span>(?P<pub_date>.*?)<\/span>.*?<div class="clear"><\/div>',
            r'<div style="line-height:30px;">.*?<li><a href="(?P<url>.*?)" target="_blank" >(?P<title>.*?)<\/a>(?P<pub_date>.*?)<\/li>'
        ],
        "news_patterns" : [
            '作者：(?P<author>.*?)来源：.*?<!--enorth cms block start.*?-->(?P<source>.*?)<!--enorth cms block end .*?-->.*?<div class=\"text\">(?P<content>.*?)<div class=\"editor\">',
            r'<!--enorth cms block start.*?-->(?P<source>.*?)<!--enorth cms block end.*?-->.*?<span id="author_baidu">作者：(?P<author>.*?)<\/span>.*?<div id="docContent">(?P<content>.*?)<div id="moreContent"',

       ]
    },
    "default":{
        "list_patterns" : [
             r'<div style="line-height:30px;">.*?<li><a href="(?P<url>.*?)" target="_blank" >(?P<title>.*?)<\/a>(?P<pub_date>.*?)<\/li>'
        ],
        "news_patterns" : [
            r'<!--enorth cms block start.*?-->(?P<source>.*?)<!--enorth cms block end.*?-->.*?<span id="author_baidu">作者：(?P<author>.*?)<\/span>.*?<div id="docContent">(?P<content>.*?)<div id="moreContent"',
            r'<div id="docDetail">.*?<span>(?P<source>.*?)<\/span>.*?作者：(?P<author>.*?)</span>.*?<div id="docContent">(?P<content>.*?)<div id="moreContent"',
            r'<span class="docSourceName">(<.*>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div id="docContent">(?P<content>.*?)<div id="moreContent"'
       ]
    },
}

def default_generate_next_list_url(crawler):
    ret_url=crawler.list_url_tpl
    yield ret_url


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
            print crawler.totalpage
            crawler.list_url_tpl = "http://www.southmoney.com/caijing/caijingyaowen/list_44_"+"%d.html"
            yield ret_url
        else:
            print (crawler.totalpage-crawler.page_num)
            ret_url = crawler.list_url_tpl % (crawler.totalpage-crawler.page_num)
            print ret_url
            yield ret_url


def shxf_generate_next_list_url(crawler):
    while crawler.page_num<3:
        if crawler.page_num == 0:
            crawler.totalpage=int(crawler.base_url.split("#")[1])
            ret_url=crawler.list_url_tpl
            crawler.list_url_tpl = crawler.base_url.split("#")[0]
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.totalpage-crawler.page_num)
            yield ret_url

b_class_dict = {
    "财经头条": {"url":"http://finance.hebei.com.cn/cjzq/cjtt/index.shtml", "base_url":"http://finance.hebei.com.cn/system/more/23022002000000000/0000/23022002000000000_000000%d.shtml#83","pub_date_format":"%Y-%m-%d","next_list_url_generator":shxf_generate_next_list_url,"short_name":"cjtt", "pattern_type":"news"},
    "财经热点": {"url":"http://finance.hebei.com.cn/cjzq/cjrd/index.shtml", "base_url":"http://finance.hebei.com.cn/system/more/23022011000000000/0000/23022011000000000_000000%d.shtml#20","pub_date_format":"%Y-%m-%d","next_list_url_generator":shxf_generate_next_list_url,"short_name":"cjrd", "pattern_type":"news"},
    "长城财发现": {"url":"http://finance.hebei.com.cn/zccfx/index.shtml","base_url":"http://finance.hebei.com.cn/system/more/23031000000000000/0000/23031000000000000_0000000%d.shtml#10","pub_date_format":"%Y-%m-%d","next_list_url_generator":shxf_generate_next_list_url,"short_name":"cccfx", "pattern_type":"news"},
    "企业要闻": {"url":"http://finance.hebei.com.cn/qyyw/index.shtml", "base_url":"http://finance.hebei.com.cn/system/more/23032000000000000/0000/23032000000000000_0000000%d.shtml#5","pub_date_format":"%Y-%m-%d","next_list_url_generator":shxf_generate_next_list_url,"short_name":"qyyw", "pattern_type":"news"},
    "银行新闻": {"url":"http://finance.hebei.com.cn/yhzq/yhxw/", "base_url":"http://finance.hebei.com.cn/system/more/23023002000000000/0001/23023002000000000_00000%d.shtml#168","pub_date_format":"%Y-%m-%d","next_list_url_generator":shxf_generate_next_list_url,"short_name":"yhxw", "pattern_type":"news"},
    "保险新闻": {"url":"http://finance.hebei.com.cn/bxzq/bxxw/", "base_url":"http://finance.hebei.com.cn/system/more/23024002000000000/0001/23024002000000000_00000%d.shtml#145","pub_date_format":"%Y-%m-%d","next_list_url_generator":shxf_generate_next_list_url,"short_name":"bxxw", "pattern_type":"news"},
    "理财案例": {"url":"http://finance.hebei.com.cn/tzlc/lcal/","base_url":None,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"lcal", "pattern_type":"default"},
    "财富故事": {"url":"http://finance.hebei.com.cn/tzlc/cfgs/","base_url":None, "pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"cfgs", "pattern_type":"default"},
    "理财产品": {"url":"http://finance.hebei.com.cn/tzlc/lccp/", "base_url":None,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"lccp", "pattern_type":"default"},
    "理财论坛": {"url":"http://finance.hebei.com.cn/tzlc/lclt/", "base_url":None,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"lclt", "pattern_type":"default"},
    "热点新闻": {"url":"http://finance.hebei.com.cn/tzlc/rdxw/", "base_url":None,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"rdxw", "pattern_type":"default"},
    "投资创业": {"url":"http://finance.hebei.com.cn/tzlc/tzcy/", "base_url":None,"pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"tzcy", "pattern_type":"news"},
    "生活消费": {"url":"http://finance.hebei.com.cn/cjxw/shxf/","base_url":"http://finance.hebei.com.cn/system/more/23025001000000000/0010/23025001000000000_0000%d.shtml#1095", "pub_date_format":"%Y-%m-%d","next_list_url_generator":shxf_generate_next_list_url,"short_name":"shxf", "pattern_type":"news"},

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
                "base_url":info["base_url"],
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


