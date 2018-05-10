# -*- coding: utf-8 -*-
from .common import *

conf = {
    "domain_name": "环球财经",
    "pipelines": [
        {
            "name": "中国",
            "log_level": "info",
            "log_filename": "../log/hqcj_zg.log",
            "crawler":
            {
                "name": "HQCJNewsPipeline_new.HQCJNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.huanqiu.com/china/",
                    "data_path": "../data/hqcj/",
                    "website_name": "环球财经",
                    "b_class": "中国",
                    "checkpoint_filename": "../ckpt/hqcj_zg.ckpt",
                    "checkpoint_saved_days": 1000
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "HQCJNewsPipeline_new.HQCJNewsContentParser",
                    "params": {}
                },
               {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of hqcj/zg
        {
            "name": "国际",
            "log_level": "info",
            "log_filename": "../log/hqcj_gj.log",
            "crawler":
            {
                "name": "HQCJNewsPipeline_new.HQCJNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.huanqiu.com/world/",
                    "data_path": "../data/hqcj/",
                    "website_name": "环球财经",
                    "b_class": "国际",
                    "checkpoint_filename": "../ckpt/hqcj_gj.ckpt",
                    "checkpoint_saved_days": 1000
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "HQCJNewsPipeline_new.HQCJNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of hqcj/gj
        {
            "name": "独家",
            "log_level": "info",
            "log_filename": "../log/hqcj_dj.log",
            "crawler":
            {
                "name": "HQCJNewsPipeline_new.HQCJNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.huanqiu.com/view/",
                    "data_path": "../data/hqcj/",
                    "website_name": "环球财经",
                    "b_class": "独家",
                    "checkpoint_filename": "../ckpt/hqcj_dj.ckpt",
                    "checkpoint_saved_days": 1000
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "HQCJNewsPipeline_new.HQCJNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of hqcj/dj
        {
            "name": "人物",
            "log_level": "info",
            "log_filename": "../log/hqcj_rw.log",
            "crawler":
            {
                "name": "HQCJNewsPipeline_new.HQCJNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.huanqiu.com/people/",
                    "data_path": "../data/hqcj/",
                    "website_name": "环球财经",
                    "b_class": "人物",
                    "checkpoint_filename": "../ckpt/hqcj_rw.ckpt",
                    "checkpoint_saved_days": 1000
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "HQCJNewsPipeline_new.HQCJNewsContentParser",
                    "params": {}
                },
            #     {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of hqcj/rw
        {
            "name": "外电",
            "log_level": "info",
            "log_filename": "../log/hqcj_wd.log",
            "crawler":
            {
                "name": "HQCJNewsPipeline_new.HQCJNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.huanqiu.com/media/",
                    "data_path": "../data/hqcj/",
                    "website_name": "环球财经",
                    "b_class": "外电",
                    "checkpoint_filename": "../ckpt/hqcj_wd.ckpt",
                    "checkpoint_saved_days": 1000
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "HQCJNewsPipeline_new.HQCJNewsContentParser",
                    "params": {}
                },
            #     {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of hqcj/wd
        {
            "name": "评论",
            "log_level": "info",
            "log_filename": "../log/hqcj_pl.log",
            "crawler":
            {
                "name": "HQCJNewsPipeline_new.HQCJNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.huanqiu.com/comment/",
                    "data_path": "../data/hqcj/",
                    "website_name": "环球财经",
                    "b_class": "评论",
                    "checkpoint_filename": "../ckpt/hqcj_pl.ckpt",
                    "checkpoint_saved_days": 1000
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "HQCJNewsPipeline_new.HQCJNewsContentParser",
                    "params": {}
                },
            #     {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of hqcj/pl
        {
            "name": "公司",
            "log_level": "info",
            "log_filename": "../log/hqcj_gs.log",
            "crawler":
            {
                "name": "HQCJNewsPipeline_new.HQCJNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.huanqiu.com/industry/",
                    "data_path": "../data/hqcj/",
                    "website_name": "环球财经",
                    "b_class": "公司",
                    "checkpoint_filename": "../ckpt/hqcj_gs.ckpt",
                    "checkpoint_saved_days": 10
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "HQCJNewsPipeline_new.HQCJNewsContentParser",
                    "params": {}
                },
            #     {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of hqcj/gs
        {
            "name": "证券",
            "log_level": "info",
            "log_filename": "../log/hqcj_zq.log",
            "crawler":
            {
                "name": "HQCJNewsPipeline_new.HQCJNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.huanqiu.com/sto/",
                    "data_path": "../data/hqcj/",
                    "website_name": "环球财经",
                    "b_class": "证券",
                    "checkpoint_filename": "../ckpt/hqcj_zq.ckpt",
                    "checkpoint_saved_days": 1000
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "HQCJNewsPipeline_new.HQCJNewsContentParser",
                    "params": {}
                },
            #     {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of hqcj/zq
        {
            "name": "房产",
            "log_level": "info",
            "log_filename": "../log/hqcj_fc.log",
            "crawler":
            {
                "name": "HQCJNewsPipeline_new.HQCJNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.huanqiu.com/house/",
                    "data_path": "../data/hqcj/",
                    "website_name": "环球财经",
                    "b_class": "房产",
                    "checkpoint_filename": "../ckpt/hqcj_fc.ckpt",
                    "checkpoint_saved_days": 10
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "HQCJNewsPipeline_new.HQCJNewsContentParser",
                    "params": {}
                },
            #     {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of hqcj/fc
        {
            "name": "理财",
            "log_level": "info",
            "log_filename": "../log/hqcj_lc.log",
            "crawler":
            {
                "name": "HQCJNewsPipeline_new.HQCJNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.huanqiu.com/money/",
                    "data_path": "../data/hqcj/",
                    "website_name": "环球财经",
                    "b_class": "理财",
                    "checkpoint_filename": "../ckpt/hqcj_lc.ckpt",
                    "checkpoint_saved_days": 10
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "HQCJNewsPipeline_new.HQCJNewsContentParser",
                    "params": {}
                },
            #     {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of hqcj/lc
        {
            "name": "职场",
            "log_level": "info",
            "log_filename": "../log/hqcj_zc.log",
            "crawler":
            {
                "name": "HQCJNewsPipeline_new.HQCJNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.huanqiu.com/career/",
                    "data_path": "../data/hqcj/",
                    "website_name": "环球财经",
                    "b_class": "职场",
                    "checkpoint_filename": "../ckpt/hqcj_zc.ckpt",
                    "checkpoint_saved_days": 10
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "HQCJNewsPipeline_new.HQCJNewsContentParser",
                    "params": {}
                },
            #     {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of hqcj/zc
        {
            "name": "商学院",
            "log_level": "info",
            "log_filename": "../log/hqcj_sxy.log",
            "crawler":
            {
                "name": "HQCJNewsPipeline_new.HQCJNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.huanqiu.com/mba/",
                    "data_path": "../data/hqcj/",
                    "website_name": "环球财经",
                    "b_class": "商学院",
                    "checkpoint_filename": "../ckpt/hqcj_sxy.ckpt",
                    "checkpoint_saved_days": 10
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "HQCJNewsPipeline_new.HQCJNewsContentParser",
                    "params": {}
                },
            #     {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of hqcj/sxy
        {
            "name": "图库",
            "log_level": "info",
            "log_filename": "../log/hqcj_tk.log",
            "crawler":
            {
                "name": "HQCJNewsPipeline_new.HQCJNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.huanqiu.com/pictures/",
                    "data_path": "../data/hqcj/",
                    "website_name": "环球财经",
                    "b_class": "图库",
                    "checkpoint_filename": "../ckpt/hqcj_tk.ckpt",
                    "checkpoint_saved_days": 10
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "HQCJNewsPipeline_new.HQCJNewsContentParser",
                    "params": {}
                },
            #     {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of hqcj/tk
        {
            "name": "滚动",
            "log_level": "info",
            "log_filename": "../log/hqcj_gd.log",
            "crawler":
            {
                "name": "HQCJNewsPipeline_new.HQCJNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.huanqiu.com/roll/",
                    "data_path": "../data/hqcj/",
                    "website_name": "环球财经",
                    "b_class": "滚动",
                    "checkpoint_filename": "../ckpt/hqcj_gd.ckpt",
                    "checkpoint_saved_days": 10
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "HQCJNewsPipeline_new.HQCJNewsContentParser",
                    "params": {}
                },
            #     {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of hqcj/gd
        {
            "name": "能源",
            "log_level": "info",
            "log_filename": "../log/hqcj_ny.log",
            "crawler":
            {
                "name": "HQCJNewsPipeline_new.HQCJNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.huanqiu.com/nengy/",
                    "data_path": "../data/hqcj/",
                    "website_name": "环球财经",
                    "b_class": "能源",
                    "checkpoint_filename": "../ckpt/hqcj_ny.ckpt",
                    "checkpoint_saved_days": 10
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "HQCJNewsPipeline_new.HQCJNewsContentParser",
                    "params": {}
                },
            #     {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of hqcj/ny
        {
            "name": "新三板",
            "log_level": "info",
            "log_filename": "../log/hqcj_xsb.log",
            "crawler":
            {
                "name": "HQCJNewsPipeline_new.HQCJNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.huanqiu.com/xinsanb/",
                    "data_path": "../data/hqcj/",
                    "website_name": "环球财经",
                    "b_class": "新三板",
                    "checkpoint_filename": "../ckpt/hqcj_xsb.ckpt",
                    "checkpoint_saved_days": 10
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "HQCJNewsPipeline_new.HQCJNewsContentParser",
                    "params": {}
                },
            #     {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of hqcj/xsb
        {
            "name": "国际财讯",
            "log_level": "info",
            "log_filename": "../log/hqcj_gjcx.log",
            "crawler":
            {
                "name": "HQCJNewsPipeline_new.HQCJNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.huanqiu.com/gjcx/",
                    "data_path": "../data/hqcj/",
                    "website_name": "环球财经",
                    "b_class": "国际财讯",
                    "checkpoint_filename": "../ckpt/hqcj_gjcx.ckpt",
                    "checkpoint_saved_days": 10
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "HQCJNewsPipeline_new.HQCJNewsContentParser",
                    "params": {}
                },
            #     {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of hqcj/gjcx
        {
            "name": "环球沙龙",
            "log_level": "info",
            "log_filename": "../log/hqcj_hqsl.log",
            "crawler":
            {
                "name": "HQCJNewsPipeline_new.HQCJNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://finance.huanqiu.com/hqsl/",
                    "data_path": "../data/hqcj/",
                    "website_name": "环球财经",
                    "b_class": "环球沙龙",
                    "checkpoint_filename": "../ckpt/hqcj_hqsl.ckpt",
                    "checkpoint_saved_days": 10
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "HQCJNewsPipeline_new.HQCJNewsContentParser",
                    "params": {}
                },
            #     {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },
            ],
            "uploader": online_mysql_uploader_conf
        },# end of hqcj/hqsl
    ]  # end of pipelines for a website
}  # end of config of a website
