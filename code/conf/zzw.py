# -*- coding: utf-8 -*-
from .common import *

conf = {
    "domain_name": "中证网",
    "pipelines": [
        {
            "name": "公司",
            "log_level": "info",
            "log_filename": "../log/zzw_ssgs.log",
            "crawler":
            {
                "name": "ZZWNewsPipeline.ZZWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://www.cs.com.cn/ssgs/",
                    "data_path": "../data/zzw/",
                    "website_name": "中证网",
                    "b_class": "公司",
                    "checkpoint_filename": "../ckpt/zzw_ssgs.ckpt",
                    "checkpoint_saved_days": 20
                    #"log_filename": "./test.log"
                }
            },
            "transformers": [
                {
                    "name": "ZZWNewsPipeline.ZZWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },

            ],
            "uploader": online_mysql_uploader_conf
        },
        {
            "name": "中证快讯",
            "log_level": "info",
            "log_filename": "../log/zzw_zzkx.log",
            "crawler":
            {
                "name": "ZZWNewsPipeline.ZZWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://www.cs.com.cn/sylm/jsbd/",
                    "data_path": "../data/zzw/",
                    "website_name": "中证网",
                    "b_class": "中证快讯",
                    "checkpoint_filename": "../ckpt/zzw_zzkx.ckpt",
                    "checkpoint_saved_days": 20
                    #"log_filename": "./test.log"
                }
            },
            "transformers": [
                {
                    "name": "ZZWNewsPipeline.ZZWNewsContentParser",
                    "params": {}
                },
            #     {
            #     "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
            #     "params": {
            #     }
            # },

            ],
            "uploader": online_mysql_uploader_conf
        },
        {
            "name": "首页公司",
            "log_level": "info",
            "log_filename": "../log/zzw_sygs.log",
            "crawler":
            {
                "name": "ZZWNewsPipeline.ZZWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://www.cs.com.cn/ssgs/gsxw/",
                    "data_path": "../data/zzw/",
                    "website_name": "中证网",
                    "b_class": "首页公司",
                    "checkpoint_filename": "../ckpt/zzw_sygs.ckpt",
                    "checkpoint_saved_days": 20
                    #"log_filename": "./test.log"
                }
            },
            "transformers": [
                {
                    "name": "ZZWNewsPipeline.ZZWNewsContentParser",
                    "params": {}
                },
                # {
                # "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                # "params": {
                # }
            # },

            ],
            "uploader": online_mysql_uploader_conf
        },
        {
            "name": "港股-公司新闻",
            "log_level": "info",
            "log_filename": "../log/zzw_gggsxw.log",
            "crawler":
            {
                "name": "ZZWNewsPipeline.ZZWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://www.cs.com.cn/gg/gsxw/",
                    "data_path": "../data/zzw/",
                    "website_name": "中证网",
                    "b_class": "港股-公司新闻",
                    "checkpoint_filename": "../ckpt/zzw_gggsxw.ckpt",
                    "checkpoint_saved_days": 20
                    #"log_filename": "./test.log"
                }
            },
            "transformers": [
                {
                    "name": "ZZWNewsPipeline.ZZWNewsContentParser",
                    "params": {}
                },
                # {
                # "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                # "params": {
                # }
            # },

            ],
            "uploader": online_mysql_uploader_conf
        },
        {
            "name": "公司行业",
            "log_level": "info",
            "log_filename": "../log/zzw_ssgs_hyzx.log",
            "crawler":
            {
                "name": "ZZWNewsPipeline.ZZWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://www.cs.com.cn/ssgs/hyzx/",
                    "data_path": "../data/zzw/",
                    "website_name": "中证网",
                    "b_class": "公司行业",
                    "checkpoint_filename": "../ckpt/zzw_ssgs_hyzx.ckpt",
                    "checkpoint_saved_days": 20
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZZWNewsPipeline.ZZWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },

            ],
            "uploader": online_mysql_uploader_conf
        },
        {
            "name": "公司房产",
            "log_level": "info",
            "log_filename": "../log/zzw_ssgs_fcgs.log",
            "crawler":
            {
                "name": "ZZWNewsPipeline.ZZWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://www.cs.com.cn/ssgs/fcgs/",
                    "data_path": "../data/zzw/",
                    "website_name": "中证网",
                    "b_class": "公司房产",
                    "checkpoint_filename": "../ckpt/zzw_ssgs_fcgs.ckpt",
                    "checkpoint_saved_days": 20
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZZWNewsPipeline.ZZWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },

            ],
            "uploader": online_mysql_uploader_conf
        },
        {
            "name": "公司新三板",
            "log_level": "info",
            "log_filename": "../log/zzw_ssgs_ssb.log",
            "crawler":
            {
                "name": "ZZWNewsPipeline.ZZWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://www.cs.com.cn/ssgs/ssb/",
                    "data_path": "../data/zzw/",
                    "website_name": "中证网",
                    "b_class": "公司新三板",
                    "checkpoint_filename": "../ckpt/zzw_ssgs_ssb.ckpt",
                    "checkpoint_saved_days": 20
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZZWNewsPipeline.ZZWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },

            ],
            "uploader": online_mysql_uploader_conf
        },
        {
            "name": "市场",
            "log_level": "info",
            "log_filename": "../log/zzw_gppd.log",
            "crawler":
            {
                "name": "ZZWNewsPipeline.ZZWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://www.cs.com.cn/gppd/",
                    "data_path": "../data/zzw/",
                    "website_name": "中证网",
                    "b_class": "市场",
                    "checkpoint_filename": "../ckpt/zzw_gppd.ckpt",
                    "checkpoint_saved_days": 20
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZZWNewsPipeline.ZZWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },

            ],
            "uploader": online_mysql_uploader_conf
        },
        {
            "name": "市场期市",
            "log_level": "info",
            "log_filename": "../log/zzw_zzqh.log",
            "crawler":
            {
                "name": "ZZWNewsPipeline.ZZWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://www.cs.com.cn/zzqh/",
                    "data_path": "../data/zzw/",
                    "website_name": "中证网",
                    "b_class": "市场期市",
                    "checkpoint_filename": "../ckpt/zzw_zzqh.ckpt",
                    "checkpoint_saved_days": 20
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZZWNewsPipeline.ZZWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },

            ],
            "uploader": online_mysql_uploader_conf
        },
        {
            "name": "市场债市",
            "log_level": "info",
            "log_filename": "../log/zzw_zqxw.log",
            "crawler":
            {
                "name": "ZZWNewsPipeline.ZZWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://www.cs.com.cn/zqxw/",
                    "data_path": "../data/zzw/",
                    "website_name": "中证网",
                    "b_class": "市场债市",
                    "checkpoint_filename": "../ckpt/zzw_zqxw.ckpt",
                    "checkpoint_saved_days": 20
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZZWNewsPipeline.ZZWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },

            ],
            "uploader": online_mysql_uploader_conf
        },
        {
            "name": "市场研报",
            "log_level": "info",
            "log_filename": "../log/zzw_gppd_jnqs.log",
            "crawler":
            {
                "name": "ZZWNewsPipeline.ZZWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://www.cs.com.cn/gppd/jnqs/",
                    "data_path": "../data/zzw/",
                    "website_name": "中证网",
                    "b_class": "市场研报",
                    "checkpoint_filename": "../ckpt/zzw_gppd_jnqs.ckpt",
                    "checkpoint_saved_days": 20
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZZWNewsPipeline.ZZWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },

            ],
            "uploader": online_mysql_uploader_conf
        },
        {
            "name": "宏观",
            "log_level": "info",
            "log_filename": "../log/zzw_xwzx.log",
            "crawler":
            {
                "name": "ZZWNewsPipeline.ZZWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://www.cs.com.cn/xwzx/",
                    "data_path": "../data/zzw/",
                    "website_name": "中证网",
                    "b_class": "宏观",
                    "checkpoint_filename": "../ckpt/zzw_xwzx.ckpt",
                    "checkpoint_saved_days": 20
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZZWNewsPipeline.ZZWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },

            ],
            "uploader": online_mysql_uploader_conf
        },
        {
            "name": "宏观海外",
            "log_level": "info",
            "log_filename": "../log/zzw_xwzx_hwxx.log",
            "crawler":
            {
                "name": "ZZWNewsPipeline.ZZWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://www.cs.com.cn/xwzx/hwxx/",
                    "data_path": "../data/zzw/",
                    "website_name": "中证网",
                    "b_class": "宏观海外",
                    "checkpoint_filename": "../ckpt/zzw_xwzx_hwxx.ckpt",
                    "checkpoint_saved_days": 20
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZZWNewsPipeline.ZZWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },

            ],
            "uploader": online_mysql_uploader_conf
        },
        {
            "name": "宏观基金",
            "log_level": "info",
            "log_filename": "../log/zzw_tzjj.log",
            "crawler":
            {
                "name": "ZZWNewsPipeline.ZZWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://www.cs.com.cn/tzjj/",
                    "data_path": "../data/zzw/",
                    "website_name": "中证网",
                    "b_class": "宏观基金",
                    "checkpoint_filename": "../ckpt/zzw_tzjj.ckpt",
                    "checkpoint_saved_days": 20
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZZWNewsPipeline.ZZWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },

            ],
            "uploader": online_mysql_uploader_conf
        },
        {
            "name": "宏观港股",
            "log_level": "info",
            "log_filename": "../log/zzw_gg.log",
            "crawler":
            {
                "name": "ZZWNewsPipeline.ZZWNewsCrawler",
                "params":
                {
                    "list_url_tpl": "http://www.cs.com.cn/gg/",
                    "data_path": "../data/zzw/",
                    "website_name": "中证网",
                    "b_class": "宏观港股",
                    "checkpoint_filename": "../ckpt/gg.ckpt",
                    "checkpoint_saved_days": 20
                    #"log_filename": "./test1.log"
                }
            },
            "transformers": [
                {
                    "name": "ZZWNewsPipeline.ZZWNewsContentParser",
                    "params": {}
                },
                {
                "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                "params": {
                }
            },

            ],
            "uploader": online_mysql_uploader_conf
        },
    ]  # end of pipelines for a website
}  # end of config of a website
