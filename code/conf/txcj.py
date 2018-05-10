# -*- coding: utf-8 -*-
from .common import *

website_name = "腾讯"
website_short_name = "txcj"
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
    "news": {
        "list_patterns": [
            r'<a target="_blank" href="(?P<url>.*?)">(?P<title>.*?)<\/a>'
        ],
        "news_patterns": [
            r'<div class="qq_article">.*?<div class="a_Info">.*?<span class="a_source".*?>(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>(<span class="a_author">)?(<a.*?>)?(?P<author>.*?)(<\/a>)?.*?<span class="a_time">(?P<pub_date>\d{4}-\d{2}-\d{2} \d{2}:\d{2})<\/span>.*?<div class="bd".*?>(?P<content>.*?)<div class="qq_articleFt">',
            r'<meta name="_pubtime" content="(?P<pub_date>.*?)">.*?<div class="content-article">(?P<content>.*?)<div id="Comment">',
            r'<div class="main" role="main">.*?<span class="where color-a-1".*?><a.*?>(?P<source>.*?)<\/a>.*?<span class="pubTime article-time">(?P<pub_date>.*?)<\/span>.*?<div id="Cnt-Main-Article-QQ".*?>(?P<content>.*?)<\/div>',
        ]
    },
    "zhengquan": {
        "list_patterns": [
            r"{title:'(?P<title>.*?)',url:'(?P<url>.*?)'.*?pubtime:'(?P<pub_time>.*?)'"
        ],
        "news_patterns": [
            r'bosszone="jgname">(?P<source>.*?)<\/span.*?class="pubTime article-time">(?P<pub_date>.*?)<\/.*?bossZone="content">(?P<content>.*?)<\/div>'
        ]
    },
    "xsb":{
        "list_patterns": [
            r'<a target="_blank" href="(?P<url>.*?)">(?P<title>.*?)<\/a>'
        ],
        "news_patterns": [
            r'bosszone="jgname">(?P<source>.*?)<\/span.*?class="pubTime article-time">(?P<pub_date>.*?)<\/.*?bossZone="content">(?P<content>.*?)<\/div>'
        ]
    },
    "keji":{
        "list_patterns": [
            r'<a.*?href="http://tech.qq.com/a(?P<url>.*?)">(?P<title>.*?)<\/a'
        ],
        "news_patterns": [
            r'<div class="qq_article">.*?<div class="a_Info">.*?<span class="a_source".*?>(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>(<span class="a_author">)?(<a.*?>)?(?P<author>.*?)(<\/a>)?.*?<span class="a_time">(?P<pub_date>\d{4}-\d{2}-\d{2} \d{2}:\d{2})<\/span>.*?<div class="bd".*?>(?P<content>.*?)<div class="qq_articleFt">',
            r'<meta name="_pubtime" content="(?P<pub_date>.*?)">.*?<div class="content-article">(?P<content>.*?)<div id="Comment">',
            r'<div class="main" role="main">.*?<span class="where color-a-1".*?><a.*?>(?P<source>.*?)<\/a>.*?<span class="pubTime article-time">(?P<pub_date>.*?)<\/span>.*?<div id="Cnt-Main-Article-QQ".*?>(?P<content>.*?)<\/div>',
        ]
    },
}
headers = {
    "listHeaders": {
        'Referer': "http://roll.finance.qq.com/",
        'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'Keep-Alive',
        'Host': 'roll.finance.qq.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    },
    "gdHeaders": {
        'Referer': "http://finance.qq.com/",
        'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'Keep-Alive',
        'Host': 'finance.qq.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    },
    "newsPageHeaders": {
        'Host': 'news.qq.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }
}


def default_generate_next_list_url(crawler):
    while crawler.page_num <= 1:
        yield crawler.list_url_tpl

b_class_dict = {
    "滚动要闻": {"url":"https://finance.qq.com/c/gdyw_%d.htm", "short_name":"gdyw", "pattern_type":"news","base_url":"https://finance.qq.com","header":headers["gdHeaders"]},
    "宏观经济": {"url":"https://finance.qq.com/c/hgjjllist_%d.htm", "short_name":"hgjj", "pattern_type":"news","base_url":"https://finance.qq.com","header":headers["gdHeaders"]},
    "公司报道": {"url":"https://finance.qq.com/c/gsbdlist_%d.htm", "short_name":"gsbd", "pattern_type":"news","base_url":"https://finance.qq.com","header":headers["gdHeaders"]},
    "消费": {"url":"https://finance.qq.com/c/xfwtlist_%d.htm", "short_name":"xfwt", "pattern_type":"news","base_url":"https://finance.qq.com","header":headers["gdHeaders"]},
    "国际": {"url":"https://finance.qq.com/c/gjcjlist_%d.htm", "short_name":"gjcj", "pattern_type":"news","base_url":"https://finance.qq.com","header":headers["gdHeaders"]},
    "财经-金融": {"url":"https://finance.qq.com/c/jrscllist_%d.htm", "short_name":"cjjr", "pattern_type":"news","base_url":"https://finance.qq.com","header":headers["gdHeaders"]},
    "财经-新三板": {"url":"https://finance.qq.com/c/xsbdt_%d.htm", "short_name":"xsbdt", "pattern_type":"xsb","base_url":"https://finance.qq.com","header":headers["gdHeaders"],},
    "滚动首页": {
        "url": "http://roll.finance.qq.com/interface/roll.php?&page=%d&mode=1&of=json", "short_name": "gdsy",
        "pattern_type": "news", "base_url": None, "crawler_func": "TXCJNewsPipline.TXCJNewsCrawler",
        "header": headers["listHeaders"],
        "news_header": headers["newsPageHeaders"]
    },
    "证券-港股公司新闻": {"url":"http://stock.qq.com/l/hk/ggxw/list20150520152324.htm","pub_date_format": "%Y-%m-%d %H:%M","short_name":"zqgggsxw", "pattern_type":"zhengquan","base_url":"","next_list_url_generator":default_generate_next_list_url,},
    "科技": {"url":"http://tech.qq.com/l/201804/scroll_20.htm","pub_date_format": "%Y-%m-%d %H:%M","short_name":"keji", "pattern_type":"keji","base_url":"http://tech.qq.com/a","next_list_url_generator":default_generate_next_list_url,},



}


for name, info in b_class_dict.iteritems():
    pipeline_conf = {
        "name": name,
        "log_level": info.get("debug_level", default_log_level),
        "log_filename": "%s/%s_%s.log" % (log_path, website_short_name, info["short_name"]),
        "crawler":
            {
                "name": info.get("crawler", "XX_Crawler.XXNewsETL.NewsCrawler" if "crawler_func" not in info else info[
                    "crawler_func"]),
                "params":
                    {
                        "list_url_tpl": info["url"],
                        "data_path": "%s/%s/" % (data_path, website_short_name),
                        "website_name": website_name,
                        "b_class": name,
                        "checkpoint_filename": "%s/%s_%s.ckpt" % (ckpt_path, website_short_name, info["short_name"]),
                        "checkpoint_saved_days": info.get("ckpt_days", default_ckpt_days),
                        "list_patterns": pattern_conf[info["pattern_type"]]["list_patterns"],
                        "next_list_url_generator": info.get("next_list_url_generator", None),
                        "header": info.get("header", None),
                        "news_header": info.get("news_header", None),
                        "pub_date_format": info.get("pub_date_format", None),
                        "base_url": info.get("base_url", None),
                        "start_page_num": 1,
                        "allow_redirect": False,
                        # "log_filename": "./test.log"
                    }
            },
        "transformers": [
            {
                "name": "XX_Crawler.XXProcessors.DetailNewsContentParser" if "parser" not in info else info["parser"],
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
    # print pipeline_conf
    conf["pipelines"].append(pipeline_conf)
