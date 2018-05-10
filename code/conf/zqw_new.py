# -*- coding: utf-8 -*-
from .common import *

conf = {
    "domain_name": "中国青年网",
    "pipelines": [
        {
            "name": "股市",
            "log_level": "info",
            "log_filename": "../log/zqw_gs.log",
            "crawler":
            {
                "name": "ZQWNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/finance_stock/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "股市",
                    "checkpoint_filename": "../ckpt/zqw_gs.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQWNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of zqw/gs
        {
            "name": "基金",
            "log_level": "info",
            "log_filename": "../log/zqw_jj.log",
            "crawler":
            {
                "name": "ZQWNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/finance_fund/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "基金",
                    "checkpoint_filename": "../ckpt/zqw_jj.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQWNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of zqw/jj
        {
            "name": "理财",
            "log_level": "info",
            "log_filename": "../log/zqw_lc.log",
            "crawler":
            {
                "name": "ZQWNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/finance_money/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "理财",
                    "checkpoint_filename": "../ckpt/zqw_lc.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQWNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of zqw/lc
        {
            "name": "银行",
            "log_level": "info",
            "log_filename": "../log/zqw_yh.log",
            "crawler":
            {
                "name": "ZQWNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/finance_bank/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "银行",
                    "checkpoint_filename": "../ckpt/zqw_yh.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQWNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of zqw/yh
        {
            "name": "保险",
            "log_level": "info",
            "log_filename": "../log/zqw_bx.log",
            "crawler":
            {
                "name": "ZQWNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/finance_insurance/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "保险",
                    "checkpoint_filename": "../ckpt/zqw_bx.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQWNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of zqw/bx
        {
            "name": "图解财经",
            "log_level": "info",
            "log_filename": "../log/zqw_tjcj.log",
            "crawler":
            {
                "name": "ZQWNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/201761tjcj/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "图解财经",
                    "checkpoint_filename": "../ckpt/zqw_tjcj.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQWNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of zqw/tjcj
        {
            "name": "食品",
            "log_level": "info",
            "log_filename": "../log/zqw_sp.log",
            "crawler":
            {
                "name": "ZQWNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/finance_food/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "食品",
                    "checkpoint_filename": "../ckpt/zqw_sp.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQWNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of zqw/sp
        {
            "name": "科技",
            "log_level": "info",
            "log_filename": "../log/zqw_kj.log",
            "crawler":
            {
                "name": "ZQWNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/finance_IT/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "科技",
                    "checkpoint_filename": "../ckpt/zqw_kj.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQWNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of zqw/kj
        {
            "name": "消费",
            "log_level": "info",
            "log_filename": "../log/zqw_xf.log",
            "crawler":
            {
                "name": "ZQWNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/finance_cyxfgsxw/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "消费",
                    "checkpoint_filename": "../ckpt/zqw_xf.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQWNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of zqw/xf
        {
            "name": "房产",
            "log_level": "info",
            "log_filename": "../log/zqw_fc.log",
            "crawler":
            {
                "name": "ZQWNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/finance_house/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "房产",
                    "checkpoint_filename": "../ckpt/zqw_fc.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQWNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of zqw/fc
        {
            "name": "独家稿件",
            "log_level": "info",
            "log_filename": "../log/zqw_djgj.log",
            "crawler":
            {
                "name": "ZQWNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/finance_djgj/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "独家稿件",
                    "checkpoint_filename": "../ckpt/zqw_djgj.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQWNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of zqw/djgj
        {
            "name": "资本市场",
            "log_level": "info",
            "log_filename": "../log/zqw_zbsc.log",
            "crawler":
            {
                "name": "ZQWNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/finance_zqjrrdjj/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "资本市场",
                    "checkpoint_filename": "../ckpt/zqw_zbsc.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQWNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of zqw/zbsc
        {
            "name": "IPO调查",
            "log_level": "info",
            "log_filename": "../log/zqw_ipodc.log",
            "crawler":
            {
                "name": "ZQWNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/finance_ipo/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "IPO调查",
                    "checkpoint_filename": "../ckpt/zqw_ipodc.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQWNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of zqw/ipodc
        {
            "name": "曝光台",
            "log_level": "info",
            "log_filename": "../log/zqw_bgt.log",
            "crawler":
            {
                "name": "ZQWNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/finance_consumption/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "曝光台",
                    "checkpoint_filename": "../ckpt/zqw_bgt.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQWNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of zqw/bgt
        {
            "name": "即时新闻",
            "log_level": "info",
            "log_filename": "../log/zqw_jsxw.log",
            "crawler":
            {
                "name": "ZQWNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/finance_jsxw/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "即时新闻",
                    "checkpoint_filename": "../ckpt/zqw_jsxw.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQWNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of zqw/48xsdj,也就是即时新闻
        {
            "name": "热点推荐,视觉聚焦",
            "log_level": "info",
            "log_filename": "../log/zqw_rdtj.log",
            "crawler":
            {
                "name": "ZQW_RDTJNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/finance_consumption/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "热点推荐，视觉聚焦",
                    "checkpoint_filename": "../ckpt/zqw_rdtj.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQW_RDTJNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of zqw/rdtj,sjjj
        {
            "name": "要闻",
            "log_level": "info",
            "log_filename": "../log/zqw_yw.log",
            "crawler":
            {
                "name": "ZQWNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/finance_yw/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "要闻",
                    "checkpoint_filename": "../ckpt/zqw_yw.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQWNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of zqw/rdtj,sjjj
        {
            "name": "青担当",
            "log_level": "info",
            "log_filename": "../log/zqw_qdd.log",
            "crawler":
            {
                "name": "ZQWNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/csr/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "青担当",
                    "checkpoint_filename": "../ckpt/zqw_qdd.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQWNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of zqw/qdd
        {
            "name": "滚动新闻",
            "log_level": "debug",
            "log_filename": "../log/zqw_gdxw.log",
            "crawler":
            {
                "name": "ZQWNewsPipeline_new.ZQWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.youth.cn/finance_gdxw/",
                    "data_path": "../data/zqw/",
                    "website_name": "中青网",
                    "b_class": "滚动新闻",
                    "checkpoint_filename": "../ckpt/zqw_gdxw.ckpt",
                    "checkpoint_saved_days": 300
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZQWNewsPipeline_new.ZQWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        }# end of zqw/gdxw
    ]  # end of pipelines for a website
}  # end of config of a website
