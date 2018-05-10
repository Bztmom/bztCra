# -*- coding: utf-8 -*-
from .common import *

website_name = "新浪"
website_short_name = "sina"
data_path = "../data/"
ckpt_path = "../ckpt/"
log_path = "../log/"
default_ckpt_days = 50
default_log_level = "debug"

conf = {
    "domain_name": website_name,
    "pipelines": [
        
    ]  # end of pipelines for a website
}  # end of config of a website
pattern_conf = {"news":{
        "list_patterns" : [
            #r'"url":"(?P<url>.*?)".*?"title":"(?P<title>.*?)"',
            r'<li><a href="(?P<url>http:\/\/finance(.*?))" target="_blank">(?P<title>.*?)<\/a><span>\(.*?\)<\/span><\/li>',
        ],
        "news_patterns" : [
            r'<div class="second-title">(?P<title>.*?)<\/div>.*?<span class="date">(?P<pub_date>.*?)<\/span>.*?class="source ent-source".*?>(?P<source>.*?)(<\/span>)?(<\/a>)?<\/div>.*?<!-- 原始正文begin -->(?P<content>.*?)<!-- 原始正文end -->',
            r'<div class="second-title">(?P<title>.*?)<\/div>.*?<span class="date">(?P<pub_date>.*?)<\/span>.*?class="source ent-source".*?>(?P<source>.*?)(<\/span>)?(<\/a>)?<\/div>.*?<!-- 原始正文start -->(?P<content>.*?)<!-- 原始正文end -->',
            r'<div class="second-title">(?P<title>.*?)<\/div>.*?<span class="date">(?P<pub_date>.*?)<\/span>(<a.*?>)?(?P<source>.*?)(<\/span>)?(<\/a>)?<\/div>.*?<!-- 原始正文begin -->(?P<content>.*?)<!-- 原始正文end -->',
            r'<div class="second-title">(?P<title>.*?)<\/div>.*?<span class="date">(?P<pub_date>.*?)<\/span>(<a.*?>)?(?P<source>.*?)(<\/span>)?(<\/a>)?<\/div>.*?<!-- 原始正文start -->(?P<content>.*?)<!-- 原始正文end -->',
            r'<div class="blkContainerSblk">\s*<h1.*?>(?P<title>.*?)<\/h1>\s*<div class="artInfo">\s*<span.*?>(?P<pub_date>.*?)<\/span>.*?<span.*>作者:(<a.*?>)?(?P<author>.*?)(<\/a>)?<\/span>.*?原始正文.*?-->(?P<content>.*?)<\/div>\s*<script',
            r'class="time-source">(?P<pub_date>.*?)<span.*?id="artibody">(?P<content>.*?)<\/div'
           ]
    },
        "gd":{
        "list_patterns" : [
            r'url : "(.*?)".*?title : "(?P<title>.*?)",url : "(?P<url>.*?)"',
            r'"url":"(?P<url>.*?)".*?"title":"(?P<title>.*?)"',
        ],
        "news_patterns" : [
            r'<span class="date">(?P<pub_date>.*?)<\/span>.*?class="source.*?>(?P<source>.*?)<\/a>.*?<!-- 正文 start -->(?P<content>.*?)<!-- 正文 end -->',
            r'<div class="second-title">(?P<title>.*?)<\/div>.*?<span class="date">(?P<pub_date>.*?)<\/span>.*?class="source ent-source".*?>(?P<source>.*?)(<\/span>)?(<\/a>)?<\/div>.*?<!-- 原始正文begin -->(?P<content>.*?)<!-- 原始正文end -->',
            r'<div class="second-title">(?P<title>.*?)<\/div>.*?<span class="date">(?P<pub_date>.*?)<\/span>.*?class="source ent-source".*?>(?P<source>.*?)(<\/span>)?(<\/a>)?<\/div>.*?<!-- 原始正文start -->(?P<content>.*?)<!-- 原始正文end -->',
            r'<div class="second-title">(?P<title>.*?)<\/div>.*?<span class="date">(?P<pub_date>.*?)<\/span>(<a.*?>)?(?P<source>.*?)(<\/span>)?(<\/a>)?<\/div>.*?<!-- 原始正文begin -->(?P<content>.*?)<!-- 原始正文end -->',
            r'<div class="second-title">(?P<title>.*?)<\/div>.*?<span class="date">(?P<pub_date>.*?)<\/span>(<a.*?>)?(?P<source>.*?)(<\/span>)?(<\/a>)?<\/div>.*?<!-- 原始正文start -->(?P<content>.*?)<!-- 原始正文end -->',
            r'<div class="blkContainerSblk">\s*<h1.*?>(?P<title>.*?)<\/h1>\s*<div class="artInfo">\s*<span.*?>(?P<pub_date>.*?)<\/span>.*?<span.*>作者:(<a.*?>)?(?P<author>.*?)(<\/a>)?<\/span>.*?原始正文.*?-->(?P<content>.*?)<\/div>\s*<script',
            r'class="time-source">(?P<pub_date>.*?)<span.*?id="artibody">(?P<content>.*?)<\/div',
            r'id="pub_date">(?P<pub_date>.*?)<\/span>.*?data-sudaclick="media_name">(?P<source>.*?)<\/a>.*?<!-- 正文内容 begin -->(?P<content>.*?)<!-- 正文页广告 --> ',
            r'id="pub_date">(?P<pub_date>.*?)<\/span>.*?data-sudaclick="media_comment">(?P<source>.*?)<\/a>.*?<!-- 正文内容 begin -->(?P<content>.*?)<!-- 文章关键词 begin -->',
        ]
    },
    "bank":{
        "list_patterns" : [
            r'<li><a href="(?P<url>[^<]*?)" target="_blank">(?P<title>[^<]*?)<\/a><span>',
        ],
        "news_patterns" : [
            r'<div class="second-title">(?P<title>.*?)<\/div>.*?<span class="date">(?P<pub_date>.*?)<\/span>.*?class="source ent-source".*?>(?P<source>.*?)(<\/span>)?(<\/a>)?<\/div>.*?<!-- 原始正文begin -->(?P<content>.*?)<!-- 原始正文end -->',
            r'<div class="second-title">(?P<title>.*?)<\/div>.*?<span class="date">(?P<pub_date>.*?)<\/span>.*?class="source ent-source".*?>(?P<source>.*?)(<\/span>)?(<\/a>)?<\/div>.*?<!-- 原始正文start -->(?P<content>.*?)<!-- 原始正文end -->',
            r'<div class="second-title">(?P<title>.*?)<\/div>.*?<span class="date">(?P<pub_date>.*?)<\/span>(<a.*?>)?(?P<source>.*?)(<\/span>)?(<\/a>)?<\/div>.*?<!-- 原始正文begin -->(?P<content>.*?)<!-- 原始正文end -->',
            r'<div class="second-title">(?P<title>.*?)<\/div>.*?<span class="date">(?P<pub_date>.*?)<\/span>(<a.*?>)?(?P<source>.*?)(<\/span>)?(<\/a>)?<\/div>.*?<!-- 原始正文start -->(?P<content>.*?)<!-- 原始正文end -->',
        ]
    },
        "yanjiu":{
        "list_patterns" : [
            r'<td class="tal f14">.*?<a target="_blank" title="(?P<title>.*?)" href="(?P<url>.*?)">.*?<td>.*?<\/td>.*?<td>(?P<pub_date>.*?)<\/td>.*?<div class="fname05"><span>(?P<source>.*?)<\/span><\/div>.*?<div class="fname"><span>(?P<author>.*?)<\/span><\/div>',
        ],
        "news_patterns" : [
            r'<div class="blk_container">(?P<content>.*?)<\/div>',]
    },
}

headers = {
    "newsPageHeaders": {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'Keep-Alive',
        'Host': 'feed.mix.sina.com.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    },
}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 3:
        if crawler.page_num == 0:
            crawler.page_num+=1
        ret_url = crawler.list_url_tpl % (crawler.page_num)
        yield ret_url


b_class_dict = {
    "财经新闻": {"url":"", "pub_date_format":["%Y年%m月%d日 %H:%M","%Y年%m月%d日%H:%M"], "next_list_url_generator":None,"short_name":"zq", "pattern_type":"news" ,"crawler_func":"SinaNewsPipeline.SinaNewsCrawler"},
    "滚动新闻": {"url":"http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=89&num=60&page=%d", "next_list_url_generator":default_generate_next_list_url,"pub_date_format":u"%Y年%m月%d日 %H:%M", "short_name":"gdxw", "pattern_type":"gd"},
    # "产经": {"url":"http://feed.mix.sina.com.cn/api/roll/get?pageid=164&lid=1693&num=10&page=%d", "next_list_url_generator":default_generate_next_list_url,"pub_date_format":u"%Y年%m月%d日 %H:%M", "short_name":"cj", "pattern_type":"gd"},
    # "消费记录": {"url":"http://feed.mix.sina.com.cn/api/roll/get?pageid=164&lid=1693&num=10&page=%d", "next_list_url_generator":default_generate_next_list_url,"pub_date_format":u"%Y年%m月%d日 %H:%M", "short_name":"xfjl", "pattern_type":"gd"},
    # "互联网": {"url":"http://feed.mix.sina.com.cn/api/roll/get?pageid=204&lid=22&num=30&versionNumber=1.2.8&page=%d&encode=utf-8", "next_list_url_generator":default_generate_next_list_url,"pub_date_format":u"%Y年%m月%d日 %H:%M", "short_name":"hlw", "pattern_type":"gd"},
    # "创世纪": {"url":"http://feed.mix.sina.com.cn/api/roll/get?pageid=402&lid=2559&num=30&versionNumber=1.2.8&page=%d&encode=utf-8", "next_list_url_generator":default_generate_next_list_url,"pub_date_format":u"%Y-%m-%d %H:%M:%S", "short_name":"csj", "pattern_type":"gd"},
    # "电信": {"url":"http://feed.mix.sina.com.cn/api/roll/get?pageid=223&lid=23&num=30&versionNumber=1.2.8&page=%d&encode=utf-8", "next_list_url_generator":default_generate_next_list_url,"pub_date_format":["%Y-%m-%d %H:%M:%S","%Y年%m月%d日 %H:%M","%Y年%m月%d日%H:%M"], "short_name":"dx", "pattern_type":"gd"},
    # "家电": {"url":"http://feed.mix.sina.com.cn/api/roll/get?pageid=57&lid=37&num=30&versionNumber=1.2.8&page=%d&encode=utf-8", "next_list_url_generator":default_generate_next_list_url,"pub_date_format":["%Y-%m-%d %H:%M:%S","%Y年%m月%d日 %H:%M","%Y年%m月%d日%H:%M"], "short_name":"jd", "pattern_type":"gd","header":headers['newsPageHeaders']},


    #"滚动新闻": {"url":"http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=43&num=60&page=%d", "next_list_url_generator":default_generate_next_list_url,"pub_date_format":u"%Y年%m月%d日 %H:%M", "short_name":"gdxw", "pattern_type":"gd"},
    #"银行-公司动态": {"url":"http://roll.finance.sina.com.cn/finance/yh/gsdt/index_%d.shtml", "next_list_url_generator":default_generate_next_list_url,"pub_date_format":u"%Y年%m月%d日 %H:%M", "short_name":"yh-gsdt", "pattern_type":"bank"},
    #"银行-央行法规": {"url":"http://roll.finance.sina.com.cn/finance/yh/yhsy_yxfg/index_%d.shtml", "next_list_url_generator":default_generate_next_list_url,"pub_date_format":u"%Y年%m月%d日 %H:%M", "short_name":"yh-yhfg", "pattern_type":"bank"},
    #"研究": {"url":"http://vip.stock.finance.sina.com.cn/q/go.php/vReport_List/kind/lastest/index.phtml?p=%d", "next_list_url_generator":default_generate_next_list_url,"pub_date_format":"%Y-%m-%d", "short_name":"yj", "pattern_type":"yanjiu"},
    #"上市公司": {"url":"http://roll.finance.sina.com.cn/finance/zq1/ssgs/index_%d.shtml", "pub_date_format":u"%Y年%m月%d日 %H:%M", "next_list_url_generator":None,"short_name":"ssgs", "pattern_type":"news"},
    
    # "新股滚动新闻": {"url":"http://feed.mix.sina.com.cn/api/roll/get?pageid=205&lid=1789&num=10&page=%d", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"xggdxw", "pattern_type":"news"},
    # "新股最新动态": {"url":"http://feed.mix.sina.com.cn/api/roll/get?pageid=205&lid=1790&num=10&page=%d", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"xgzxdt", "pattern_type":"news"},
    # "新股评论": {"url":"http://feed.mix.sina.com.cn/api/roll/get?pageid=205&lid=1791&num=10&page=%d", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"xgpl", "pattern_type":"news"},
    # "新股IPO中介": {"url":"http://feed.mix.sina.com.cn/api/roll/get?pageid=205&lid=1793&num=10&page=%d", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"xgipozj", "pattern_type":"news"},
    # "新股PE动态": {"url":"http://feed.mix.sina.com.cn/api/roll/get?pageid=205&lid=1792&num=10&page=%d", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"xgpedt", "pattern_type":"news"},
    # "上市公司": {"url":"http://roll.finance.sina.com.cn/finance/zq1/ssgs/index_%d.shtml", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"ssgs", "pattern_type":"news"},
    # "产经滚动新闻": {"url":"http://feed.mix.sina.com.cn/api/roll/get?pageid=164&lid=1693&num=10&page=%d", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"cjgdxw", "pattern_type":"news"},
    # "产经公司新闻": {"url":"http://feed.mix.sina.com.cn/api/roll/get?pageid=164&lid=1694&num=10&page=%d", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"cjgsxw", "pattern_type":"news"},
    # "产经产业新闻": {"url":"http://feed.mix.sina.com.cn/api/roll/get?pageid=164&lid=1695&num=10&page=%d", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"cjcyxw", "pattern_type":"news"},
    # "产经深度报道": {"url":"http://feed.mix.sina.com.cn/api/roll/get?pageid=164&lid=1696&num=10&page=%d", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"cjsdbd", "pattern_type":"news"},
    # "产经人事变动": {"url":"http://feed.mix.sina.com.cn/api/roll/get?pageid=164&lid=1697&num=10&page=%d", "pub_date_format":"%Y-%m-%d %H:%M:%S", "short_name":"cjrsbd", "pattern_type":"news"},
}


for name, info in b_class_dict.iteritems():
    pipeline_conf = {
        "name": name,
        "log_level": info.get("debug_level",default_log_level),
        "log_filename": "%s/%s_%s.log"%(log_path, website_short_name, info["short_name"]),
        "crawler":
        {
            # "name": info.get("crawler","SinaNewsPipeline.SinaNewsCrawler"),
            "name": info.get("crawler", "XX_Crawler.XXNewsETL.NewsCrawler" if "crawler_func" not in info else info[
                "crawler_func"]),
            "params":
            {
                "list_url_tpl": info["url"],
                "data_path": "%s/%s/"%(data_path, website_short_name),
                "website_name": website_name,
                "b_class": name,
                "checkpoint_filename": "%s/%s_%s.ckpt"%(ckpt_path, website_short_name, info["short_name"]),
                "checkpoint_saved_days": info.get("ckpt_days",default_ckpt_days) ,
                "list_patterns": pattern_conf[info["pattern_type"]]["list_patterns"] if "pattern_type" in info else [],
                "pub_date_format":info["pub_date_format"],
                "next_list_url_generator":info.get("list_url_gen", info["next_list_url_generator"]) ,
                "header":info.get("header", None),
                "start_page_num":1,
                "max_itered_page_num":5,
                #"log_filename": "./test.log"
            }
        },
        "transformers": [
            {
                "name": "XX_Crawler.XXProcessors.DetailNewsContentParser"  if "parser" not in info else info["parser"],
                "params": {
                    "detail_patterns": pattern_conf[info["pattern_type"]]["news_patterns"]  if "pattern_type" in info else []
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


