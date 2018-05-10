# -*- coding: utf-8 -*-
from .common import *

website_name = "全景网"
website_short_name = "qjw"
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
pattern_conf = {"news": {
    "list_patterns": [
        r'<li class="clearfix">.*?<a href="(?P<url>.*?)" target="_blank">(?P<title>.*?)<\/a>.*?<div class="setinfo3">(?P<pub_date>.*?)<\/div>'
    ],
    "news_patterns": [
        r'<div class="newscontent_right2">.*?<h1>(?P<title>.*?)<\/h1>.*?<i class="zhuoze">(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/i>.*?<i>(?P<author>.*?)<\/i>.*?<div class="article_content2">(?P<content>.*?)<div class="unique2">',
    ]
},
    "wyt": {
        "list_patterns": [
            r'<div class="toux">.*?<i>(?P<author>.*?)<\/i>.*?<h2 class="bshare-title">.*?<a href="(?P<url>.*?)".*?>(?P<title>.*?)<\/a>.*?<span class="newsdetail_left">.*?<i>(?P<pub_date>.*?)<\/i>'
        ],
        "news_patterns": [
            r'<div class="article_content">(?P<content>.*?)<div class="copyright">'
        ]
    }
}

WYT_Header = {
    "Referer": "http://weyt.p5w.net/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Host": "weyt.p5w.net"
}

b_class_dict = {
    "港股新闻": {"url": "http://www.p5w.net/stock/hkstock/hknews/", "short_name": "ggxw", "pattern_type": "news"},
    "股票-综合": {"url": "http://www.p5w.net/stock/news/zonghe/", "short_name": "gpzh", "pattern_type": "news"},
    "公司新闻": {"url": "http://www.p5w.net/stock/news/gsxw/", "short_name": "gsxw", "pattern_type": "news"},
    "国内财经": {"url": "http://www.p5w.net/news/gncj/", "short_name": "gncj", "pattern_type": "news"},
    "国际财经": {"url": "http://www.p5w.net/news/gjcj/", "short_name": "gjcj", "pattern_type": "news"},
    "产经": {"url": "http://www.p5w.net/news/cjxw/", "short_name": "cjxw", "pattern_type": "news"},
    "评论": {"url": "http://www.p5w.net/news/xwpl/", "short_name": "xwpl", "pattern_type": "news"},
    "科技": {"url": "http://www.p5w.net/news/tech/", "short_name": "tech", "pattern_type": "news"},
    "商业": {"url": "http://www.p5w.net/news/biz/", "short_name": "biz", "pattern_type": "news"},
    "房产": {"url": "http://www.p5w.net/news/cjxw/fdcy/", "short_name": "fdcy", "pattern_type": "news", "ckpt_days": 500},
    "曝光台": {"url": "http://www.p5w.net/news/pgt/", "short_name": "pgt", "pattern_type": "news", "ckpt_days": 500},
    "快讯-7x24滚动新闻": {"url": "http://www.p5w.net/kuaixun/tj/", "short_name": "kxtj", "pattern_type": "news"},
    "快讯-独家观察": {"url": "http://www.p5w.net/kuaixun/dj/", "short_name": "kxdj", "pattern_type": "news"},
    "快讯-公司": {"url": "http://www.p5w.net/kuaixun/gs/", "short_name": "kxgs", "pattern_type": "news"},
    "快讯-路演": {"url": "http://www.p5w.net/kuaixun/ly/", "short_name": "kxly", "pattern_type": "news"},
    "快讯-市场": {"url": "http://www.p5w.net/kuaixun/sc/", "short_name": "kxsc", "pattern_type": "news"},
    "快讯-其他": {"url": "http://www.p5w.net/kuaixun/qt/", "short_name": "kxqt", "pattern_type": "news"},
    "快讯-第一资讯": {"url": "http://www.p5w.net/kuaixun/dyzx/", "short_name": "kxdyzx", "pattern_type": "news",
                "ckpt_days": 1000},
    "we言堂": {"url": "http://weyt.p5w.net/ajaxGetArticleList?page=%d&search=&size=10", "short_name": "weyt",
             "list_url_gen": None, "pattern_type": "wyt", "header": WYT_Header,
             "crawler": "QJWNewsPipeline.QJW_WYTNewsCrawler"},
    "舆情-快讯": {"url": "http://www.p5w.net/yuqing/kuaixun/", "short_name": "yqkx", "ckpt_days": 500,
              "debug_level": "debug", "pattern_type": "news"},
    "舆情-观察": {"url": "http://www.p5w.net/yuqing/guancha/", "short_name": "yqgc", "ckpt_days": 500,
              "debug_level": "debug", "pattern_type": "news"},
    "舆情-榜单-财经新闻top5": {"url": "http://www.p5w.net/yuqing/phb/cjxw/", "short_name": "yqbdcj", "ckpt_days": 500,
                       "debug_level": "debug", "pattern_type": "news"},
    "理财综合": {"url": "http://www.p5w.net/money/zh/", "short_name": "zhlc", "pattern_type": "news"},
    "舆情-榜单-预警度top5": {"url": "http://www.p5w.net/yuqing/phb/yqyjd/", "short_name": "yqyjd", "ckpt_days": 50,
                      "debug_level": "debug", "crawler": "QJWNewsPipeline.QJW_YQNewsCrawler", "pattern_type": "news"},
    "舆情-榜单-媒体关注度top5": {"url": "http://www.p5w.net/yuqing/phb/mtgzd/", "short_name": "yqgzd", "ckpt_days": 50,
                        "debug_level": "debug", "crawler": "QJWNewsPipeline.QJW_YQNewsCrawler", "pattern_type": "news"},
    "舆情-基金": {"url": "http://www.p5w.net/yuqing/jjyq/", "short_name": "yqjj", "ckpt_days": 50, "debug_level": "debug",
              "crawler": "QJWNewsPipeline.QJW_YQNewsCrawler", "pattern_type": "news"},
    "舆情-ipo": {"url": "http://www.p5w.net/yuqing/ipo/", "short_name": "yqipo", "ckpt_days": 50, "debug_level": "debug",
               "crawler": "QJWNewsPipeline.QJW_YQNewsCrawler", "pattern_type": "news"},
    "舆情-报告": {"url": "http://www.p5w.net/yuqing/yubg/", "short_name": "yqbg", "ckpt_days": 50, "debug_level": "debug",
              "crawler": "QJWNewsPipeline.QJW_YQNewsCrawler", "pattern_type": "news"},
    "舆情-案例": {"url": "http://www.p5w.net/yuqing/yqbg/", "short_name": "yqal", "ckpt_days": 50, "debug_level": "debug",
              "crawler": "QJWNewsPipeline.QJW_YQNewsCrawler", "pattern_type": "news"},
}


def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            ret_url = crawler.list_url_tpl
            crawler.list_url_tpl += "index_%d.htm"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url


for name, info in b_class_dict.iteritems():
    pipeline_conf = {
        "name": name,
        "log_level": info.get("debug_level", default_log_level),
        "log_filename": "%s/%s_%s.log" % (log_path, website_short_name, info["short_name"]),
        "crawler":
            {
                "name": info.get("crawler", "XX_Crawler.XXNewsETL.NewsCrawler"),
                "params":
                    {
                        "list_url_tpl": info["url"],
                        "data_path": "%s/%s/" % (data_path, website_short_name),
                        "website_name": website_name,
                        "b_class": name,
                        "checkpoint_filename": "%s/%s_%s.ckpt" % (ckpt_path, website_short_name, info["short_name"]),
                        "checkpoint_saved_days": info.get("ckpt_days", default_ckpt_days),
                        "list_patterns": pattern_conf[info["pattern_type"]][
                            "list_patterns"] if "pattern_type" in info else [],
                        "pub_date_format": u"%m月%d日 %H:%M",
                        "next_list_url_generator": info.get("list_url_gen", default_generate_next_list_url),
                        "header": info.get("header", None)
                        # "log_filename": "./test.log"
                    }
            },
        "transformers": [
            {
                "name": "XX_Crawler.XXProcessors.DetailNewsContentParser" if "parser" not in info else info["parser"],
                "params": {
                    "detail_patterns": pattern_conf[info["pattern_type"]][
                        "news_patterns"] if "pattern_type" in info else []
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
