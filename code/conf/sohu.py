# -*- coding: utf-8 -*-
from .common import *
from XX_Crawler.Utils import get
import re

website_name = "搜狐网"
website_short_name = "sohu"
data_path = "../data/"
ckpt_path = "../ckpt/"
log_path = "../log/"
default_ckpt_days = 50
default_log_level = "debug"

default_pub_date_format = "%Y-%m-%d %H:%M"

conf = {
    "domain_name": website_name,
    "pipelines": [

    ]  # end of pipelines for a website
}  # end of config of a website
pattern_conf = {
    "news": {
        "list_patterns": [
        ],
        "news_patterns": [
            r'<article class="article".*?>(?P<content>.*?)<\/article>',
            r'<iframe src="(?P<content>.*?)"',
        ]
    },
    "gd": {
        "list_patterns": [
            r'<a test=a href=\'(?P<url>.*?)\'.*?>(?P<title>.*?)<\/'
        ],
        "news_patterns": [
            r'id="news-time".*?>(?P<pub_date>.*?)<\/.*?data-role="original-link">来源:<a.*?>(?P<source>.*?)<\/.*?<article class="article".*?>(?P<content>.*?)<\/article>',
            r'div class="news-title">.*?class="writer">(?P<source>.*?)<\/span.*?class="time".*?>(?P<pub_date>.*?)<\/.*?id="contentText">(?P<content>.*?)<\/div>',
        ]
    },
}

def default_generate_next_list_url(crawler):
    for page_num in range(1, 2):
        yield crawler.list_url_tpl % page_num

def next_list_url(crawler):
    yield crawler.list_url_tpl

b_class_dict = {
    "宏观": {
        "url": "http://v2.sohu.com/public-api/feed?scene=CATEGORY&sceneId=994&page=%d&size=20&callback=jQuery112407202415589868012_1514036797310",
        "short_name": "hg", "pattern_type": "news", "crawler_func": "SOHUNewsPipeline.SOHUNewsCrawler", },
    "行业": {
        "url": "http://v2.sohu.com/public-api/feed?scene=CATEGORY&sceneId=996&page=%d&size=20&callback=jQuery112407202415589868012_1514036797310",
        "short_name": "hy", "pattern_type": "news", "crawler_func": "SOHUNewsPipeline.SOHUNewsCrawler", },
    "股票": {
        "url": "http://v2.sohu.com/public-api/feed?scene=CATEGORY&sceneId=997&page=%d&size=20&callback=jQuery112407202415589868012_1514036797310",
        "short_name": "gp", "pattern_type": "news", "crawler_func": "SOHUNewsPipeline.SOHUNewsCrawler", },
    "金融理财": {
        "url": "http://v2.sohu.com/public-api/feed?scene=CATEGORY&sceneId=998&page=%d&size=20&callback=jQuery112407202415589868012_1514036797310",
        "short_name": "jrlc", "pattern_type": "news", "crawler_func": "SOHUNewsPipeline.SOHUNewsCrawler", },
    "经营管理": {
        "url": "http://v2.sohu.com/public-api/feed?scene=CATEGORY&sceneId=995&page=%d&size=20&callback=jQuery112407202415589868012_1514036797310",
        "short_name": "jygl", "pattern_type": "news", "crawler_func": "SOHUNewsPipeline.SOHUNewsCrawler", },
    "滚动新闻": {
        "url": "http://business.sohu.com/business_scrollnews.shtml",
        "short_name": "gdxw","pub_date_format": ["%Y-%m-%d %H:%M","%Y-%m-%d %H:%M:%S"], "pattern_type": "gd","list_url_gen": next_list_url},

}




for name, info in b_class_dict.iteritems():
    pipeline_conf = {
        "name": name,
        "log_level": info.get("debug_level", default_log_level),
        "log_filename": "%s/%s_%s.log" % (log_path, website_short_name, info["short_name"]),
        "crawler":
            {
                # "name": info.get("crawler","SOHUNewsPipeline.SOHUNewsCrawler"),
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
                        "next_list_url_generator": info.get("list_url_gen", default_generate_next_list_url),
                        "header": info.get("header", None),
                        "pub_date_format": info.get("pub_date_format", default_pub_date_format),
                        "start_page_num": 1,
                        # "log_filename": "./test.log"
                    }
            },
        "transformers": [
            {
                "name": "XX_Crawler.XXProcessors.DetailNewsContentParser" if "parser" not in info else info["parser"],
                "params": {
                    "detail_patterns": pattern_conf[info["pattern_type"]]["news_patterns"],
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
