# -*- coding: utf-8 -*-

from .common import *

conf = {
"domain_name": "证券市场红周刊",
     "pipelines": [
         # {
         #     "name": "市场",
         #     "log_level": "info",
         #     "log_filename": "../log/zqschzk_sc.log",
         #     "crawler":
         #     {
         #         "name": "HZKNewsPipeline_new.HZKNewsCrawler",
         #         "params":
         #         {
         #             "list_url_tpl": "http://news.hongzhoukan.com/article_list.php?id=309",
         #             "data_path": "../data/zqschzk/",
         #             "website_name": "证券市场红周刊",
         #             "b_class": "市场",
         #             "checkpoint_filename": "../ckpt/zqschzk_sc.ckpt",
         #             "checkpoint_saved_days": 20
         #             #"log_filename": "./test.log"
         #         }
         #     },
         #     "transformers": [
         #         {
         #             "name": "HZKNewsPipeline_new.HZKNewsContentParser",
         #             "params": {}
         #         },
         #     #     {
         #     #      "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
         #     #      "params": {
         #     #     }
         #     # },
         #     ],
         #     "uploader": online_mysql_uploader_conf
         # },
         # {
         #     "name": "行业",
         #     "log_level": "info",
         #     "log_filename": "../log/zqschzk_hy.log",
         #     "crawler":
         #     {
         #         "name": "HZKNewsPipeline_new.HZKNewsCrawler",
         #         "params":
         #         {
         #             "list_url_tpl": "http://news.hongzhoukan.com/article_list.php?id=310",
         #             "data_path": "../data/zqschzk/",
         #             "website_name": "证券市场红周刊",
         #             "b_class": "行业",
         #             "checkpoint_filename": "../ckpt/zqschzk_hy.ckpt",
         #             "checkpoint_saved_days": 20
         #             #"log_filename": "./test.log"
         #         }
         #     },
         #     "transformers": [
         #         {
         #             "name": "HZKNewsPipeline_new.HZKNewsContentParser",
         #             "params": {}
         #         },
         #     #     {
         #     #    "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
         #     #    "params": {
         #     #    }
         #     # },
         #     ],
         #     "uploader": online_mysql_uploader_conf
         # },
         # {
         #     "name": "个股",
         #     "log_level": "info",
         #     "log_filename": "../log/zqschzk_geg.log",
         #     "crawler":
         #     {
         #         "name": "HZKNewsPipeline_new.HZKNewsCrawler",
         #         "params":
         #         {
         #             "list_url_tpl": "http://news.hongzhoukan.com/article_list.php?id=156",
         #             "data_path": "../data/zqschzk/",
         #             "website_name": "证券市场红周刊",
         #             "b_class": "个股",
         #             "checkpoint_filename": "../ckpt/zqschzk_geg.ckpt",
         #             "checkpoint_saved_days": 20
         #             #"log_filename": "./test.log"
         #         }
         #     },
         #     "transformers": [
         #         {
         #             "name": "HZKNewsPipeline_new.HZKNewsContentParser",
         #             "params": {}
         #         },
         #     #     {
         #     #    "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
         #     #    "params": {
         #     #    }
         #     # },
         #     ],
         #     "uploader": online_mysql_uploader_conf
         # },
         # {
         #     "name": "要闻",
         #     "log_level": "info",
         #     "log_filename": "../log/zqschzk_yw.log",
         #     "crawler":
         #     {
         #         "name": "HZKNewsPipeline_new.HZKNewsCrawler",
         #         "params":
         #         {
         #             "list_url_tpl": "http://news.hongzhoukan.com/article_list.php?id=336",
         #             "data_path": "../data/zqschzk/",
         #             "website_name": "证券市场红周刊",
         #             "b_class": "要闻",
         #             "checkpoint_filename": "../ckpt/zqschzk_yw.ckpt",
         #             "checkpoint_saved_days": 20
         #             #"log_filename": "./test.log"
         #         }
         #     },
         #     "transformers": [
         #         {
         #             "name": "HZKNewsPipeline_new.HZKNewsContentParser",
         #             "params": {}
         #         },
         #     #     {
         #     #    "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
         #     #    "params": {
         #     #    }
         #     # },
         #     ],
         #     "uploader": online_mysql_uploader_conf
         # },
         # {
         #     "name": "港股",
         #     "log_level": "info",
         #     "log_filename": "../log/zqschzk_gangg.log",
         #     "crawler":
         #     {
         #         "name": "HZKNewsPipeline_new.HZKNewsCrawler",
         #         "params":
         #         {
         #             "list_url_tpl": "http://news.hongzhoukan.com/article_list.php?id=325",
         #             "data_path": "../data/zqschzk/",
         #             "website_name": "证券市场红周刊",
         #             "b_class": "港股",
         #             "checkpoint_filename": "../ckpt/zqschzk_gangg.ckpt",
         #             "checkpoint_saved_days": 20
         #             #"log_filename": "./test.log"
         #         }
         #     },
         #     "transformers": [
         #         {
         #             "name": "HZKNewsPipeline_new.HZKNewsContentParser",
         #             "params": {}
         #         },
         #     #     {
         #     #    "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
         #     #    "params": {
         #     #    }
         #     # },
         #     ],
         #     "uploader": online_mysql_uploader_conf
         # },
         # {
         #     "name": "创业板",
         #     "log_level": "info",
         #     "log_filename": "../log/zqschzk_cyb.log",
         #     "crawler":
         #     {
         #         "name": "HZKNewsPipeline_new.HZKNewsCrawler",
         #         "params":
         #         {
         #             "list_url_tpl": "http://news.hongzhoukan.com/article_list.php?id=335",
         #             "data_path": "../data/zqschzk/",
         #             "website_name": "证券市场红周刊",
         #             "b_class": "创业板",
         #             "checkpoint_filename": "../ckpt/zqschzk_cyb.ckpt",
         #             "checkpoint_saved_days": 20
         #             #"log_filename": "./test.log"
         #         }
         #     },
         #     "transformers": [
         #         {
         #             "name": "HZKNewsPipeline_new.HZKNewsContentParser",
         #             "params": {}
         #         },
         #        #  {
         #        # "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
         #        # "params": {
         #        # }
         #     # },
         #     ],
         #     "uploader": online_mysql_uploader_conf
         # },

         {
             "name": "公司要闻",
             "log_level": "info",
             "log_filename": "../log/zqschzk_gsyw.log",
             "crawler":
                 {
                     "name": "HZKNewsPipeline_new.HZKNewsCrawler",
                     "params":
                         {
                             "list_url_tpl": "http://news.hongzhoukan.com/article_list.php?id=323",
                             "data_path": "../data/zqschzk/",
                             "website_name": "证券市场红周刊",
                             "b_class": "公司要闻",
                             "checkpoint_filename": "../ckpt/zqschzk_gsyw.ckpt",
                             "checkpoint_saved_days": 20
                             # "log_filename": "./test.log"
                         }
                 },
             "transformers": [
                 {
                     "name": "HZKNewsPipeline_new.HZKNewsContentParser",
                     "params": {}
                 },
                 #  {
                 # "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
                 # "params": {
                 # }
                 # },
             ],
             "uploader": online_mysql_uploader_conf
         }
               ]
        }