# -*- coding: utf-8 -*-

from .common import *

conf = {
"domain_name": "证券市场周刊",
     "pipelines": [
         {
             "name": "要闻",
             "log_level": "info",
             "log_filename": "../log/zqwlzk_yw.log",
             "crawler":
             {
                 "name": "LZKNewsPipeline_new.LZKNewsCrawler",
                 "params":
                 {
                     "list_url_tpl": "http://www.capitalweek.com.cn/important_news?",
                     "data_path": "../data/zqwlzk/",
                     "website_name": "证券网蓝刊",
                     "b_class": "要闻",
                     "checkpoint_filename": "../ckpt/zqwlzk_yw.ckpt",
                     "checkpoint_saved_days": 20
                     #"log_filename": "./test.log"
                 }
             },
             "transformers": [
                 {
                     "name": "LZKNewsPipeline_new.LZKNewsContentParser",
                     "params": {}
                 },
             #     {
             #    "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
             #    "params": {
             #    }
             # },
             ],
             "uploader": online_mysql_uploader_conf
         },
         {
             "name": "宏观",
             "log_level": "info",
             "log_filename": "../log/zqwlzk_hg.log",
             "crawler":
             {
                 "name": "LZKNewsPipeline_new.LZKNewsCrawler",
                 "params":
                 {
                     "list_url_tpl": "http://www.capitalweek.com.cn/small_article_list/1?",
                     "data_path": "../data/zqwlzk/",
                     "website_name": "证券网蓝刊",
                     "b_class": "宏观",
                     "checkpoint_filename": "../ckpt/zqwlzk_hg.ckpt",
                     "checkpoint_saved_days": 20
                     #"log_filename": "./test.log"
                 }
             },
             "transformers": [
                 {
                     "name": "LZKNewsPipeline_new.LZKNewsContentParser",
                     "params": {}
                 },
             #     {
             #    "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
             #    "params": {
             #    }
             # },

             ],
             "uploader": online_mysql_uploader_conf
         },
         {
             "name": "金融",
             "log_level": "info",
             "log_filename": "../log/zqwlzk_jr.log",
             "crawler":
             {
                 "name": "LZKNewsPipeline_new.LZKNewsCrawler",
                 "params":
                 {
                     "list_url_tpl": "http://www.capitalweek.com.cn/small_article_list/2?",
                     "data_path": "../data/zqwlzk/",
                     "website_name": "证券网蓝刊",
                     "b_class": "金融",
                     "checkpoint_filename": "../ckpt/zqwlzk_jr.ckpt",
                     "checkpoint_saved_days": 20
                     #"log_filename": "./test.log"
                 }
             },
             "transformers": [
                 {
                     "name": "LZKNewsPipeline_new.LZKNewsContentParser",
                     "params": {}
                 },
             #     {
             #    "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
             #    "params": {
             #    }
             # },
             ],
             "uploader": online_mysql_uploader_conf
         },
         {
             "name": "行业",
             "log_level": "info",
             "log_filename": "../log/zqwlzk_hy.log",
             "crawler":
             {
                 "name": "LZKNewsPipeline_new.LZKNewsCrawler",
                 "params":
                 {
                     "list_url_tpl": "http://www.capitalweek.com.cn/small_article_list/3?",
                     "data_path": "../data/zqwlzk/",
                     "website_name": "证券网蓝刊",
                     "b_class": "行业",
                     "checkpoint_filename": "../ckpt/zqwlzk_hy.ckpt",
                     "checkpoint_saved_days": 20
                     #"log_filename": "./test.log"
                 }
             },
             "transformers": [
                 {
                     "name": "LZKNewsPipeline_new.LZKNewsContentParser",
                     "params": {}
                 },
             #     {
             #    "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
             #    "params": {
             #    }
             # },
             ],
             "uploader": online_mysql_uploader_conf
         },
         {
             "name": "公司",
             "log_level": "info",
             "log_filename": "../log/zqwlzk_gs.log",
             "crawler":
             {
                 "name": "LZKNewsPipeline_new.LZKNewsCrawler",
                 "params":
                 {
                     "list_url_tpl": "http://www.capitalweek.com.cn/small_article_list/4?",
                     "data_path": "../data/zqwlzk/",
                     "website_name": "证券网蓝刊",
                     "b_class": "公司",
                     "checkpoint_filename": "../ckpt/zqwlzk_gs.ckpt",
                     "checkpoint_saved_days": 20
                     #"log_filename": "./test.log"
                 }
             },
             "transformers": [
                 {
                     "name": "LZKNewsPipeline_new.LZKNewsContentParser",
                     "params": {}
                 },
             #     {
             #    "name": "XX_Crawler.XXProcessors.HTMLTagFilter",
             #    "params": {
             #    }
             # },
             ],
             "uploader": online_mysql_uploader_conf
         },
         
               ]
        }