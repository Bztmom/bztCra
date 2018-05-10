# -*- coding: utf-8 -*-
from .common import *
from XX_Crawler.XXNewsETL import *
from XX_Crawler.Utils import *

website_name = "中国经营网"
website_short_name = "zgjyw"
data_path = "../data/"
ckpt_path = "../ckpt/"
log_path = "../log/"
default_ckpt_days = 50
default_log_level = "info"


def multi_news_page(self, news_info, content):
    page_info_pattern = re.compile(
        r'<div class="page_ch">(?P<page_div>.*?)<\/div>', re.DOTALL)
    page_pattern = re.compile(r'<a href="(?P<url>.*?)">(?P<page_num>\d)<\/a>', re.DOTALL)
    content_pattern = re.compile(r'<div class="contenttext auto">(?P<content>.*?)<div class="page auto">', re.DOTALL)
    page_info_data = page_info_pattern.search(content)
    if page_info_data:
        # print page_info_data.group(1)
        page_div = page_info_data.group("page_div")
        max_page_num = 1
        for m in page_pattern.finditer(page_div):
            cur_page_num = int(m.group("page_num"))
            if cur_page_num > max_page_num:
                max_page_num = cur_page_num
        self.logger.debug(
            "there are %d pages for this news" % (max_page_num))
        cur_url = news_info["url"]
        for page_num in xrange(2, max_page_num+1):
            # next page url is t2017-10-09_32432432.html =>t2017-10-09_32432432_1.html
            next_url = cur_url[:-5] + "_%d" %(page_num) + cur_url[-5:]
            page_content = get(next_url)
            self.logger.debug("got next page %s"%next_url)
            if page_content is not None:
                m = content_pattern.search(page_content)
                if m:
                    self.logger.debug("yield next_page content")
                    yield m.group("content")
    pass


conf = {
    "domain_name": website_name,
    "pipelines": [
        
    ]  # end of pipelines for a website
}  # end of config of a website
pattern_conf = {"news":{
        "list_patterns" : [
            r'<dt>.*?<a href="(?P<url>.*?)">(?P<title>.*?)<\/a.*?jjbotdate">(?P<pub_date>.*?)<',
            r'<div class="listleftimg auto">.*?<a href="(?P<url>.*?)" target="_blank" title="(?P<title>.*?)".*?<span>(?P<pub_date>.*?)<\/span>',
        ],
        "news_patterns" : [
            r'<div class="contentmes auto">.*?<span>来源：(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="contenttext auto">(?P<content>.*?)<div class="page auto">',
            r'<div class="contentmes auto">.*?<span>来源：(<a.*?>)?(?P<source>.*?)(<\/a>)?<\/span>.*?<div class="contenttext auto">(?P<content>.*?)<div class="contenttips auto">',
            r'<!--left 第一板块开始-->(?P<content>.*?)<!--left 第二板块结束-->'
           ]
    },

}

def default_generate_next_list_url(crawler):
    while crawler.page_num < 1:
        if crawler.page_num == 0:
            ret_url=crawler.list_url_tpl
            crawler.page_num+=1
            crawler.list_url_tpl = crawler.list_url_tpl+"%d.html"
            yield ret_url
        else:
            ret_url = crawler.list_url_tpl % (crawler.page_num)
            yield ret_url

b_class_dict = {
    "经济-宏观经济": {"url":"http://www.cb.com.cn/economy/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"hgjj", "pattern_type":"news"},
    "经济-产业经济": {"url":"http://www.cb.com.cn/chanyejingji/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"cyjj", "pattern_type":"news"},
    "经济-区域经济": {"url":"http://www.cb.com.cn/difangjingji/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"qyjj", "pattern_type":"news"},
    "经济-热点事件": {"url":"http://www.cb.com.cn/guojijingji/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"rdsj", "pattern_type":"news"},
    "公司-科技": {"url":"http://www.cb.com.cn/companies/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"kj", "pattern_type":"news"},
    "公司-汽车": {"url":"http://www.cb.com.cn/xinqiche/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"qc", "pattern_type":"news"},
    "公司-房地产": {"url":"http://www.cb.com.cn/fangdichan/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"fdc", "pattern_type":"news"},
    "公司-it家电": {"url":"http://www.cb.com.cn/itjiadian/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"itjd", "pattern_type":"news"},
    "公司-案例": {"url":"http://www.cb.com.cn/gongyeyucaikuang/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"al", "pattern_type":"news"},
    "公司-航空运输": {"url":"http://www.cb.com.cn/hangkongyuyunshu/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"hkys", "pattern_type":"news"},
    "公司-消费": {"url":"http://www.cb.com.cn/lingshouyuxiaofeipin/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"xf", "pattern_type":"news"},
    "公司-文化体育": {"url":"http://www.cb.com.cn/wenhuayuyule/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"whty", "pattern_type":"news"},
    "金融-银行": {"url":"http://www.cb.com.cn/finance/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"yh", "pattern_type":"news"},
    "金融-股市": {"url":"http://www.cb.com.cn/gushi/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"gs", "pattern_type":"news"},
    "金融-证券基金": {"url":"http://www.cb.com.cn/zhengquanjijin/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"zqjj", "pattern_type":"news"},
    "金融-信托保险": {"url":"http://www.cb.com.cn/xintuobaoxian/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"xtbx", "pattern_type":"news"},
    "金融-投资理财": {"url":"http://www.cb.com.cn/touzilicai/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"tzlc", "pattern_type":"news"},
    "金融-互联网金融": {"url":"http://www.cb.com.cn/hulianwangjinrong/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"hlwjr", "pattern_type":"news"},
    "与老板对话": {"url":"http://www.cb.com.cn/toboss/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"ylbdh", "pattern_type":"news"},
    "中经时事报": {"url":"http://www.cb.com.cn/zjssb/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"zjssb", "pattern_type":"news"},
    "新商帮": {"url":"http://www.cb.com.cn/xinshangbang/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"xsb", "pattern_type":"news"},
    "滚动播报": {"url":"http://www.cb.com.cn/gdbb/","pub_date_format":"%Y-%m-%d","next_list_url_generator":default_generate_next_list_url,"short_name":"gdbb", "pattern_type":"news"},
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
                "base_url":"http://www.cb.com.cn/",
                "data_path": "%s/%s/"%(data_path, website_short_name),
                "website_name": website_name,
                "b_class": name,
                "checkpoint_filename": "%s/%s_%s.ckpt"%(ckpt_path, website_short_name, info["short_name"]),
                "checkpoint_saved_days": info.get("ckpt_days",default_ckpt_days) ,
                "list_patterns": pattern_conf[info["pattern_type"]]["list_patterns"],
                "pub_date_format":info["pub_date_format"],
                "next_list_url_generator":info.get("list_url_gen",info["next_list_url_generator"]),
                "header":info.get("header", None),
                #"log_filename": "./test.log"
                # "start_page_num" : 1
            }
        },
        "transformers": [
            {
                "name": "XX_Crawler.XXProcessors.DetailNewsContentParser"  if "parser" not in info else info["parser"],
                "params": {
                    "detail_patterns": pattern_conf[info["pattern_type"]]["news_patterns"],
                    "multi_news_page_func": multi_news_page,
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


