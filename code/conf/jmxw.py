# -*- coding: utf-8 -*-
from .common import *

website_name = "界面新闻"
website_short_name = "jmxw"
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
            r'(<div class="main-nr">|<div class="lb-nt">)+.*?href="(?P<url>.*?)"\s*title="(?P<title>.*?)"\sclass'
        ],
        "news_patterns": [
            r'<span class="author"><a.*?>(?P<author>.*?)<\/a.*?<span>(?P<pub_date>.*?)<\/span>.*?"article-content".*?>(?P<content>.*?)<\/div',
            r'<span class="author"><a.*?>(?P<author>.*?)<\/a.*?<span class="date">(?P<pub_date>.*?)<a.*?来源：(?P<source>.*?)<\/p.*?"article-content">(?P<content>.*?)<script',
            r'<span class="author"><a.*?>(?P<author>.*?)<\/a.*?<span class="date">(?P<pub_date>.*?)<a.*?"article-content">(?P<content>.*?)<script',
            r'<span class="author">(?P<author>.*?)<\/.*?<span class="date">(?P<pub_date>.*?)<a.*?"article-content">(?P<content>.*?)<script',
        ]
    },
    "article":{
        "list_patterns": [
            r'"news-view.*?<h3><a href="(?P<url>.*?)".*?title="(?P<title>.*?)"'
        ],
        "news_patterns": [
            r'<span class="author"><a.*?>(?P<author>.*?)<\/a.*?<span>(?P<pub_date>.*?)<\/span>.*?"article-content".*?>(?P<content>.*?)<\/div',
            r'<span class="author"><a.*?>(?P<author>.*?)<\/a.*?<span class="date">(?P<pub_date>.*?)<a.*?来源：(?P<source>.*?)<\/p.*?"article-content">(?P<content>.*?)<script',
            r'<span class="author"><a.*?>(?P<author>.*?)<\/a.*?<span class="date">(?P<pub_date>.*?)<a.*?"article-content">(?P<content>.*?)<script',
            r'<span class="author">(?P<author>.*?)<\/.*?<span class="date">(?P<pub_date>.*?)<a.*?"article-content">(?P<content>.*?)<script',
        ]
    }
}


def default_generate_next_list_url(crawler):
    while crawler.page_num < 2:
        if crawler.page_num == 0:
            crawler.page_num += 1
        ret_url = crawler.list_url_tpl % (crawler.page_num)
        yield ret_url

b_class_dict = {
    "商业快讯": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=48&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "sy",
        "pattern_type": "news"
    },
    "股市快讯": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=116&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "gs",
        "pattern_type": "news"
    },
    "消费快讯": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=165&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "xf",
        "pattern_type": "news"
    },
    "金融快讯": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=166&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "jr",
        "pattern_type": "news"
    },
    "工业快讯": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=167&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "gy",
        "pattern_type": "news"
    },
    "交通快讯": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=168&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "jt",
        "pattern_type": "news"
    },
    "宏观快讯": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=177&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "hg",
        "pattern_type": "news"
    },
    "汽车快讯": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=59&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "qc",
        "pattern_type": "news"
    },
    "科技快讯": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=84&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "kj",
        "pattern_type": "news"
    },
    "房产快讯": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=69&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "fc",
        "pattern_type": "news"
    },
    "创投-快报": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=142&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "ct",
        "pattern_type": "news"
    },
    "宏观-财经要闻": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=20&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "hgcjyw",
        "pattern_type": "news"
    },
    "宏观-财经数据": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=175&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "hgcjsj",
        "pattern_type": "news"
    },
    "证券-特写": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=101&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "zqtx",
        "pattern_type": "news"
    },
    "证券-独家": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=113&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "zqdj",
        "pattern_type": "news"
    },
    "证券-调查": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=114&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "zqdc",
        "pattern_type": "news"
    },
    "证券-第一时间": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=115&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "zqdysj",
        "pattern_type": "news"
    },
    "证券-竞争力报告": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=117&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "zqjzlbg",
        "pattern_type": "news"
    },
    "金融-上市公司": {
        "url": "http://www.jiemian.com/tags/4646/%d.html",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "jrssgs",
        "pattern_type": "article",
        "crawler_func":"XX_Crawler.XXNewsETL.NewsCrawler"
    },
    "金融-最新": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=9&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "jrzx",
        "pattern_type": "news"
    },
    "消费-最新报道": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=31&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "xfzxbg",
        "pattern_type": "news"
    },
    "工业-最新报道": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=28&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "xfzxbg",
        "pattern_type": "news"
    },
    "投资-私募": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=88&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "xfzxbg",
        "pattern_type": "news"
    },
    "数据-资本": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=156&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "sjzb",
        "pattern_type": "news"
    },
    "数据-大局": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=155&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "sjdj",
        "pattern_type": "news"
    },
    "数据-万物": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=157&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "sjww",
        "pattern_type": "news"
    },
    "数据-广厦": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=158&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "sjgs",
        "pattern_type": "news"
    },
    "商业-面谈": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=38&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "symt",
        "pattern_type": "news"
    },
    "天下-全球财经": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=46&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "txqqcj",
        "pattern_type": "news"
    },
    "科技-必读": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=6&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "kjbd",
        "pattern_type": "news"
    },
    "科技-产品榜": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=73&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "kjbd",
        "pattern_type": "news"
    },
    "汽车-生意": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=14&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "qcsy",
        "pattern_type": "news"
    },
    "房产-深度": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=7&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "fcsd",
        "pattern_type": "news"
    },
    "房产-市场": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=64&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "fcsc",
        "pattern_type": "news"
    },
    "创投-报道": {
        "url": "https://a.jiemian.com/index.php?m=lists&a=ajaxNews&cid=43&callback=jQuery&page=%d",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "ctbd",
        "pattern_type": "news"
    },
    "创投-初创公司": {
        "url": "http://www.jiemian.com/tags/17089/%d.html",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "ctccgs",
        "pattern_type": "article",
        "crawler_func":"XX_Crawler.XXNewsETL.NewsCrawler"
    },
    "创投-A轮之后": {
        "url": "http://www.jiemian.com/tags/17095/%d.html",
        "pub_date_format": "%Y/%m/%d %H:%M",
        "next_list_url_generator": default_generate_next_list_url,
        "base_url":None,
        "short_name": "ctalzh",
        "pattern_type": "article",
        "crawler_func": "XX_Crawler.XXNewsETL.NewsCrawler"
    },

}

for name, info in b_class_dict.iteritems():
    pipeline_conf = {
        "name": name,
        "log_level": info.get("debug_level", default_log_level),
        "log_filename": "%s/%s_%s.log" % (log_path, website_short_name, info["short_name"]),
        "crawler":
            {
                "name": info.get("crawler","JMXWNewsPipeline.JMXWNewsCrawler" if "crawler_func" not in info else info["crawler_func"]),
                "params":
                    {
                        "list_url_tpl": info["url"],
                        "data_path": "%s/%s/" % (data_path, website_short_name),
                        "base_url": info["base_url"],
                        "website_name": website_name,
                        "b_class": name,
                        "checkpoint_filename": "%s/%s_%s.ckpt" % (ckpt_path, website_short_name, info["short_name"]),
                        "checkpoint_saved_days": info.get("ckpt_days", default_ckpt_days),
                        "list_patterns": pattern_conf[info["pattern_type"]]["list_patterns"],
                        "pub_date_format": info["pub_date_format"],
                        "next_list_url_generator": info.get("list_url_gen", info["next_list_url_generator"]),
                        "header": info.get("header", None)
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


