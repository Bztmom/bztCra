# -*- coding: utf-8 -*-

es_uploader_conf = {
    "name": "XX_Crawler.XXNewsETL.NewsUploader",
    "params": {
        "es_server_list": [
            {'host': '192.168.2.21', 'port': 9200},
            {'host': '192.168.2.22', 'port': 9200},
            {'host': '192.168.2.23', 'port': 9200},
            {'host': '192.168.2.24', 'port': 9200}
        ],
        "index_name": "company_news_result_v1",
        "type_name": "news"
    }
}

mysql_uploader_conf = {
    "name": "XX_Crawler.XXNewsETL.MySQLUploader",
    "params": {
        "db_addr": "59.110.231.53",
        "db_name": "news",
        "table_name": "li_public_opinion_simple",
        "username": "news_user",
        "password": "news_password",
    }
}

es_uploader_processor_conf = {
    "name": "XX_Crawler.XXNewsETL.ESUploadProcessor",
    "params": {
        "es_server_list": [
            {'host': '192.168.2.21', 'port': 9200},
            {'host': '192.168.2.22', 'port': 9200},
            {'host': '192.168.2.23', 'port': 9200},
            {'host': '192.168.2.24', 'port': 9200}
        ],
        "index_name": "company_news_fulltext_v1",
        "type_name": "news"
    }
}

# test_conf = conf = {
#     "websites":
#         [
#             {
#                 "domain_name": "中青网",
#                 "pipelines": [
#                     {
#                         "name": "图解财经",
#                         "log_level": "info",
#                         "log_filename": "../log/zqw_tjcj.log",
#                         "crawler":
#                         {
#                             "name": "ZQWNewsPipeline.ZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.youth.cn/201761tjcj/",
#                                 "data_path": "../data/zqw/",
#                                 "website_name": "中青网",
#                                 "b_class": "图解财经",
#                                 "checkpoint_filename": "../ckpt/zqw_tjcj.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZQWNewsPipeline.ZQWNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     },# end of zqw/tjcj
#                     {
#                         "name": "独家稿件",
#                         "log_level": "info",
#                         "log_filename": "../log/zqw_djgj.log",
#                         "crawler":
#                         {
#                             "name": "ZQWNewsPipeline.ZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.youth.cn/finance_djgj/",
#                                 "data_path": "../data/zqw/",
#                                 "website_name": "中青网",
#                                 "b_class": "独家稿件",
#                                 "checkpoint_filename": "../ckpt/zqw_djgj.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZQWNewsPipeline.ZQWNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     },# end of zqw/djgj
#                     {
#                         "name": "专题策划",
#                         "log_level": "info",
#                         "log_filename": "../log/zqw_ztch.log",
#                         "crawler":
#                         {
#                             "name": "ZQWNewsPipeline.ZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.youth.cn/finance_ztch/",
#                                 "data_path": "../data/zqw/",
#                                 "website_name": "中青网",
#                                 "b_class": "专题策划",
#                                 "checkpoint_filename": "../ckpt/zqw_ztch.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZQWNewsPipeline.ZQWNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     }# end of zqw/ztch
#                 ]
#             }  # end of 中青网
#         ]
# }
# conf = {
#     "websites":
#         [
#             {
#                 "domain_name": "中证网",
#                 "pipelines": [
#                     {
#                         "name": "公司",
#                         "log_level": "debug",
#                         "log_filename": "../log/zzw_ssgs.log",
#                         "crawler":
#                         {
#                             "name": "ZZWNewsPipeline.ZZWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://www.cs.com.cn/ssgs/",
#                                 "data_path": "../data/zzw/",
#                                 "website_name": "中证网",
#                                 "b_class": "公司",
#                                 "checkpoint_filename": "../ckpt/zzw_ssgs.ckpt",
#                                 "checkpoint_saved_days": 20
#                                 #"log_filename": "./test.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZZWNewsPipeline.ZZWNewsContentParser",
#                                 "params": {}
#                             },

#                         ],
#                         "uploader": mysql_uploader_conf
#                     },
#                     {
#                         "name": "市场",
#                         "log_level": "info",
#                         "log_filename": "../log/zzw_gppd.log",
#                         "crawler":
#                         {
#                             "name": "ZZWNewsPipeline.ZZWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://www.cs.com.cn/gppd/",
#                                 "data_path": "../data/zzw/",
#                                 "website_name": "中证网",
#                                 "b_class": "市场",
#                                 "checkpoint_filename": "../ckpt/zzw_gppd.ckpt",
#                                 "checkpoint_saved_days": 20
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZZWNewsPipeline.ZZWNewsContentParser",
#                                 "params": {}
#                             },

#                         ],
#                         "uploader": mysql_uploader_conf
#                     },
#                     {
#                         "name": "宏观",
#                         "log_level": "info",
#                         "log_filename": "../log/zzw_xwzx.log",
#                         "crawler":
#                         {
#                             "name": "ZZWNewsPipeline.ZZWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://www.cs.com.cn/xwzx/",
#                                 "data_path": "../data/zzw/",
#                                 "website_name": "中证网",
#                                 "b_class": "宏观",
#                                 "checkpoint_filename": "../ckpt/zzw_xwzx.ckpt",
#                                 "checkpoint_saved_days": 20
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZZWNewsPipeline.ZZWNewsContentParser",
#                                 "params": {}
#                             },

#                         ],
#                         "uploader": mysql_uploader_conf
#                     }
#                 ]  # end of pipelines for a website
#             },  # end of config of a website
#             {
#                 "domain_name": "网易财经",
#                 "pipelines": [
#                     {
#                         "name": "首页",
#                         "log_level": "info",
#                         "log_filename": "../log/wy_index.log",
#                         "crawler":
#                         {
#                             "name": "163NewsPipeline.WYNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://money.163.com/special/002557S5/newsdata_idx_index.js?callback=data_callback",
#                                 "data_path": "../data/163/",
#                                 "website_name": "网易财经",
#                                 "b_class": "首页",
#                                 "checkpoint_filename": "../ckpt/wy_index.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "163NewsPipeline.WYNewsContentParser",
#                                 "params": {}
#                             },

#                         ],
#                         "uploader": mysql_uploader_conf
#                     },
#                     {
#                         "name": "股票",
#                         "log_level": "info",
#                         "log_filename": "../log/wy_stock.log",
#                         "crawler":
#                         {
#                             "name": "163NewsPipeline.WYNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://money.163.com/special/002557S5/newsdata_idx_stock.js?callback=data_callback",
#                                 "data_path": "../data/163/",
#                                 "website_name": "网易财经",
#                                 "b_class": "股票",
#                                 "checkpoint_filename": "../ckpt/wy_stock.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "163NewsPipeline.WYNewsContentParser",
#                                 "params": {}
#                             },

#                         ],
#                         "uploader": mysql_uploader_conf
#                     },
#                     {
#                         "name": "商业",
#                         "log_level": "info",
#                         "log_filename": "../log/wy_biz.log",
#                         "crawler":
#                         {
#                             "name": "163NewsPipeline.WYNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://money.163.com/special/002557S5/newsdata_idx_biz.js?callback=data_callback",
#                                 "data_path": "../data/163/",
#                                 "website_name": "网易财经",
#                                 "b_class": "商业",
#                                 "checkpoint_filename": "../ckpt/wy_biz.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "163NewsPipeline.WYNewsContentParser",
#                                 "params": {}
#                             },

#                         ],
#                         "uploader": mysql_uploader_conf
#                     },
#                 ]
#             },  # end of wangyi 163
#             {
#                 "domain_name": "证券时报网",
#                 "pipelines": [
#                     {
#                         "name": "快讯",
#                         "log_level": "debug",
#                         "log_filename": "../log/zqsb_kuaixun.log",
#                         "crawler":
#                         {
#                             "name": "STCNNewsPipeline.STCNNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://kuaixun.stcn.com/",
#                                 "data_path": "../data/zqsb/",
#                                 "website_name": "证券时报网",
#                                 "b_class": "快讯",
#                                 "checkpoint_filename": "../ckpt/zqsb_kuaixun.ckpt",
#                                 "checkpoint_saved_days": 2  # 需要检查周末的情况
#                                 # "log_filename": "./zqsb_kuaixun.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "STCNNewsPipeline.STCNNewsContentParser",
#                                 "params": {}
#                             },

#                         ],
#                         "uploader": mysql_uploader_conf
#                     },  # end of pipline: stcn_kuaixun
#                     {
#                         "name": "股市-大盘",
#                         "log_level": "debug",
#                         "log_filename": "../log/zqsb_stock_dapan.log",
#                         "crawler":
#                         {
#                             "name": "STCNNewsPipeline.STCNNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://stock.stcn.com/dapan/",
#                                 "data_path": "../data/zqsb/",
#                                 "website_name": "证券时报网",
#                                 "b_class": "股市",
#                                 "checkpoint_filename": "../ckpt/zqsb_stock_dapan.ckpt",
#                                 "checkpoint_saved_days": 30
#                                 # "log_filename": "./zqsb_stock_dapan.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "STCNNewsPipeline.STCNNewsContentParser",
#                                 "params": {}
#                             },

#                         ],
#                         "uploader": mysql_uploader_conf
#                     },  # end of pipline: stcn_stock_dapan
#                     {
#                         "name": "股市-板块个股",
#                         "log_level": "debug",
#                         "log_filename": "../log/zqsb_stock_bankuai.log",
#                         "crawler":
#                         {
#                             "name": "STCNNewsPipeline.STCNNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://stock.stcn.com/bankuai/",
#                                 "data_path": "../data/zqsb/",
#                                 "website_name": "证券时报网",
#                                 "b_class": "股市",
#                                 "checkpoint_filename": "../ckpt/zqsb_stock_bankuai.ckpt",
#                                 "checkpoint_saved_days": 30
#                                 # "log_filename": "./zqsb_stock_bankuai.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "STCNNewsPipeline.STCNNewsContentParser",
#                                 "params": {}
#                             },

#                         ],
#                         "uploader": mysql_uploader_conf
#                     },  # end of pipline: stcn_stock_bankuai
#                     {
#                         "name": "股市-主力资金",
#                         "log_level": "debug",
#                         "log_filename": "../log/zqsb_stock_zhuli.log",
#                         "crawler":
#                         {
#                             "name": "STCNNewsPipeline.STCNNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://stock.stcn.com/zhuli/",
#                                 "data_path": "../data/zqsb/",
#                                 "website_name": "证券时报网",
#                                 "b_class": "股市",
#                                 "checkpoint_filename": "../ckpt/zqsb_stock_zhuli.ckpt",
#                                 # "log_filename": "./zqsb_stock_zhuli.log"
#                                 "checkpoint_saved_days": 30
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "STCNNewsPipeline.STCNNewsContentParser",
#                                 "params": {}
#                             },

#                         ],
#                         "uploader": mysql_uploader_conf
#                     },  # end of pipline: stcn_stock_zhuli
#                     {
#                         "name": "公司-新闻",
#                         "log_level": "debug",
#                         "log_filename": "../log/zqsb_company_gsxw.log",
#                         "crawler":
#                         {
#                             "name": "STCNNewsPipeline.STCNNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://company.stcn.com/gsxw/",
#                                 "data_path": "../data/zqsb/",
#                                 "website_name": "证券时报网",
#                                 "b_class": "公司",
#                                 "checkpoint_filename": "../ckpt/zqsb_company_gsxw.ckpt",
#                                 "checkpoint_saved_days": 14
#                                 # "log_filename": "./zqsb_company_gsxw.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "STCNNewsPipeline.STCNNewsContentParser",
#                                 "params": {}
#                             },

#                         ],
#                         "uploader": mysql_uploader_conf
#                     },  # end of pipline: stcn_company_gsxw
#                     {
#                         "name": "公司-产经",
#                         "log_level": "debug",
#                         "log_filename": "../log/zqsb_company_cjnews.log",
#                         "crawler":
#                         {
#                             "name": "STCNNewsPipeline.STCNNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://company.stcn.com/cjnews/",
#                                 "data_path": "../data/zqsb/",
#                                 "website_name": "证券时报网",
#                                 "b_class": "公司",
#                                 "checkpoint_filename": "../ckpt/zqsb_company_cjnews.ckpt",
#                                 "checkpoint_saved_days": 30
#                                 # "log_filename": "./zqsb_company_cjnews.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "STCNNewsPipeline.STCNNewsContentParser",
#                                 "params": {}
#                             },

#                         ],
#                         "uploader": mysql_uploader_conf
#                     }  # , # end of pipline: stcn_company_cjnews
#                 ]  # end of all pipelines of 证券时报网
#             },  # end of domain: 证券时报网
#             {
#                 "domain_name": "中国证券网",
#                 "pipelines": [
#                     {
#                         "name": "公司聚焦",
#                         "log_level": "debug",
#                         "log_filename": "../log/zgzqw_gsxw.log",
#                         "crawler":
#                         {
#                             "name": "ZGZQWNewsPipeline.ZGZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://company.cnstock.com/company/scp_gsxw/",
#                                 "data_path": "../data/zgzqw/",
#                                 "website_name": "中国证券网",
#                                 "b_class": "公司聚焦",
#                                 "checkpoint_filename": "../ckpt/zgzqw_gsxw.ckpt",
#                                 "checkpoint_saved_days": 7
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZGZQWNewsPipeline.ZGZQWNewsContentParser",
#                                 "params": {}
#                             },

#                         ],
#                         "uploader": mysql_uploader_conf
#                     },  # end of cnstock/gsxw
#                     {
#                         "name": "要闻",
#                         "log_level": "debug",
#                         "log_filename": "../log/zgzqw_yw.log",
#                         "crawler":
#                         {
#                             "name": "ZGZQWNewsPipeline.ZGZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://news.cnstock.com/news/sns_yw/",
#                                 "data_path": "../data/zgzqw/",
#                                 "website_name": "中国证券网",
#                                 "b_class": "要闻",
#                                 "checkpoint_filename": "../ckpt/zgzqw_yw.ckpt",
#                                 "checkpoint_saved_days": 7
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZGZQWNewsPipeline.ZGZQWNewsContentParser",
#                                 "params": {}
#                             },

#                         ],
#                         "uploader": mysql_uploader_conf
#                     }  # end of cnstock/yw
#                 ]  # end of piplines of 中国证券网
#             },  # end of domain: 中国证券网
#          {"domain_name": "证券市场红周刊",
#                  "pipelines": [
#                      {
#                          "name": "市场",
#                          "log_level": "debug",
#                          "log_filename": "../log/zqschzk_sc.log",
#                          "crawler":
#                          {
#                              "name": "HZKNewsPipeline.HZKNewsCrawler",
#                              "params":
#                              {
#                                  "list_url_tpl": "http://news.hongzhoukan.com/article_list.php?id=309",
#                                  "data_path": "../data/zqschzk/",
#                                  "website_name": "证券市场红周刊",
#                                  "b_class": "市场",
#                                  "checkpoint_filename": "../ckpt/zqschzk_sc.ckpt",
#                                  "checkpoint_saved_days": 20
#                                  #"log_filename": "./test.log"
#                              }
#                          },
#                          "transformers": [
#                              {
#                                  "name": "HZKNewsPipeline.HZKNewsContentParser",
#                                  "params": {}
#                              }
#                          ],
#                          "uploader": mysql_uploader_conf
#                      },
#                      {
#                          "name": "行业",
#                          "log_level": "debug",
#                          "log_filename": "../log/zqschzk_hy.log",
#                          "crawler":
#                          {
#                              "name": "HZKNewsPipeline.HZKNewsCrawler",
#                              "params":
#                              {
#                                  "list_url_tpl": "http://news.hongzhoukan.com/article_list.php?id=310",
#                                  "data_path": "../data/zqschzk/",
#                                  "website_name": "证券市场红周刊",
#                                  "b_class": "行业",
#                                  "checkpoint_filename": "../ckpt/zqschzk_hy.ckpt",
#                                  "checkpoint_saved_days": 20
#                                  #"log_filename": "./test.log"
#                              }
#                          },
#                          "transformers": [
#                              {
#                                  "name": "HZKNewsPipeline.HZKNewsContentParser",
#                                  "params": {}
#                              },
#                              es_uploader_processor_conf,
#                          ],
#                          "uploader": es_uploader_conf
#                      },
#                      {
#                          "name": "个股",
#                          "log_level": "debug",
#                          "log_filename": "../log/zqschzk_geg.log",
#                          "crawler":
#                          {
#                              "name": "HZKNewsPipeline.HZKNewsCrawler",
#                              "params":
#                              {
#                                  "list_url_tpl": "http://news.hongzhoukan.com/article_list.php?id=156",
#                                  "data_path": "../data/zqschzk/",
#                                  "website_name": "证券市场红周刊",
#                                  "b_class": "个股",
#                                  "checkpoint_filename": "../ckpt/zqschzk_geg.ckpt",
#                                  "checkpoint_saved_days": 20
#                                  #"log_filename": "./test.log"
#                              }
#                          },
#                          "transformers": [
#                              {
#                                  "name": "HZKNewsPipeline.HZKNewsContentParser",
#                                  "params": {}
#                              },
#                              es_uploader_processor_conf,
#                          ],
#                          "uploader": es_uploader_conf
#                      },
#                      {
#                          "name": "要闻",
#                          "log_level": "debug",
#                          "log_filename": "../log/zqschzk_yw.log",
#                          "crawler":
#                          {
#                              "name": "HZKNewsPipeline.HZKNewsCrawler",
#                              "params":
#                              {
#                                  "list_url_tpl": "http://news.hongzhoukan.com/article_list.php?id=336",
#                                  "data_path": "../data/zqschzk/",
#                                  "website_name": "证券市场红周刊",
#                                  "b_class": "要闻",
#                                  "checkpoint_filename": "../ckpt/zqschzk_yw.ckpt",
#                                  "checkpoint_saved_days": 20
#                                  #"log_filename": "./test.log"
#                              }
#                          },
#                          "transformers": [
#                              {
#                                  "name": "HZKNewsPipeline.HZKNewsContentParser",
#                                  "params": {}
#                              }
#                          ],
#                          "uploader": mysql_uploader_conf
#                      },
#                      {
#                          "name": "港股",
#                          "log_level": "debug",
#                          "log_filename": "../log/zqschzk_gangg.log",
#                          "crawler":
#                          {
#                              "name": "HZKNewsPipeline.HZKNewsCrawler",
#                              "params":
#                              {
#                                  "list_url_tpl": "http://news.hongzhoukan.com/article_list.php?id=325",
#                                  "data_path": "../data/zqschzk/",
#                                  "website_name": "证券市场红周刊",
#                                  "b_class": "要闻",
#                                  "checkpoint_filename": "../ckpt/zqschzk_gangg.ckpt",
#                                  "checkpoint_saved_days": 20
#                                  #"log_filename": "./test.log"
#                              }
#                          },
#                          "transformers": [
#                              {
#                                  "name": "HZKNewsPipeline.HZKNewsContentParser",
#                                  "params": {}
#                              }
#                          ],
#                          "uploader": mysql_uploader_conf
#                      },
#                      {
#                          "name": "港股",
#                          "log_level": "debug",
#                          "log_filename": "../log/zqschzk_gangg.log",
#                          "crawler":
#                          {
#                              "name": "HZKNewsPipeline.HZKNewsCrawler",
#                              "params":
#                              {
#                                  "list_url_tpl": "http://news.hongzhoukan.com/article_list.php?id=325",
#                                  "data_path": "../data/zqschzk/",
#                                  "website_name": "证券市场红周刊",
#                                  "b_class": "要闻",
#                                  "checkpoint_filename": "../ckpt/zqschzk_gangg.ckpt",
#                                  "checkpoint_saved_days": 20
#                                  #"log_filename": "./test.log"
#                              }
#                          },
#                          "transformers": [
#                              {
#                                  "name": "HZKNewsPipeline.HZKNewsContentParser",
#                                  "params": {}
#                              }
#                          ],
#                          "uploader": mysql_uploader_conf
#                      },
#                      {
#                          "name": "创业板",
#                          "log_level": "debug",
#                          "log_filename": "../log/zqschzk_cyb.log",
#                          "crawler":
#                          {
#                              "name": "HZKNewsPipeline.HZKNewsCrawler",
#                              "params":
#                              {
#                                  "list_url_tpl": "http://news.hongzhoukan.com/article_list.php?id=335",
#                                  "data_path": "../data/zqschzk/",
#                                  "website_name": "证券市场红周刊",
#                                  "b_class": "要闻",
#                                  "checkpoint_filename": "../ckpt/zqschzk_cyb.ckpt",
#                                  "checkpoint_saved_days": 20
#                                  #"log_filename": "./test.log"
#                              }
#                          },
#                          "transformers": [
#                              {
#                                  "name": "HZKNewsPipeline.HZKNewsContentParser",
#                                  "params": {}
#                              }
#                          ],
#                          "uploader": mysql_uploader_conf
#                      }
#                                ]
#             },
#             {
#                 "domain_name": "东方财经",
#                 "pipelines": [
#                     {
#                         "name": "市场零距离",
#                         "log_level": "info",
#                         "log_filename": "../log/dfcj_scljl.log",
#                         "crawler":
#                         {
#                             "name": "DFCJ_SCLJLNewsPipeline.DFCJNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.eastday.com/n998118/",
#                                 "data_path": "../data/dfcj/",
#                                 "website_name": "东方财经",
#                                 "b_class": "市场零距离",
#                                 "checkpoint_filename": "../ckpt/dfcj_scljl.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "DFCJ_SCLJLNewsPipeline.DFCJNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     },# end of finance/scljl
#                     {
#                         "name": "滚动",
#                         "log_level": "info",
#                         "log_filename": "../log/dfcj_gd.log",
#                         "crawler":
#                         {
#                             "name": "DFCJ_GDNewsPipeline.DFCJNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://news.eastday.com/eastday/13news/auto/news/finance/index_K47.html",
#                                 "data_path": "../data/dfcj/",
#                                 "website_name": "东方财经",
#                                 "b_class": "滚动",
#                                 "checkpoint_filename": "../ckpt/dfcj_gd.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "DFCJ_GDNewsPipeline.DFCJNewsContentParser",
#                                 "params": {}
#                             },
#                              # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     }# end of finance/gd
#                 ]
#             },
#             {
#                 "domain_name": "中青网",
#                 "pipelines": [
#                     {
#                         "name": "股市",
#                         "log_level": "info",
#                         "log_filename": "../log/zqw_gs.log",
#                         "crawler":
#                         {
#                             "name": "ZQWNewsPipeline.ZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.youth.cn/finance_stock/",
#                                 "data_path": "../data/zqw/",
#                                 "website_name": "中青网",
#                                 "b_class": "股市",
#                                 "checkpoint_filename": "../ckpt/zqw_gs.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZQWNewsPipeline.ZQWNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     },# end of zqw/gs
#                     {
#                         "name": "基金",
#                         "log_level": "info",
#                         "log_filename": "../log/zqw_jj.log",
#                         "crawler":
#                         {
#                             "name": "ZQWNewsPipeline.ZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.youth.cn/finance_fund/",
#                                 "data_path": "../data/zqw/",
#                                 "website_name": "中青网",
#                                 "b_class": "基金",
#                                 "checkpoint_filename": "../ckpt/zqw_jj.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZQWNewsPipeline.ZQWNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     },# end of zqw/jj
#                     {
#                         "name": "理财",
#                         "log_level": "info",
#                         "log_filename": "../log/zqw_lc.log",
#                         "crawler":
#                         {
#                             "name": "ZQWNewsPipeline.ZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.youth.cn/finance_money/",
#                                 "data_path": "../data/zqw/",
#                                 "website_name": "中青网",
#                                 "b_class": "理财",
#                                 "checkpoint_filename": "../ckpt/zqw_lc.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZQWNewsPipeline.ZQWNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     },# end of zqw/lc
#                     {
#                         "name": "银行",
#                         "log_level": "info",
#                         "log_filename": "../log/zqw_yh.log",
#                         "crawler":
#                         {
#                             "name": "ZQWNewsPipeline.ZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.youth.cn/finance_bank/",
#                                 "data_path": "../data/zqw/",
#                                 "website_name": "中青网",
#                                 "b_class": "银行",
#                                 "checkpoint_filename": "../ckpt/zqw_yh.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZQWNewsPipeline.ZQWNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     },# end of zqw/yh
#                     {
#                         "name": "保险",
#                         "log_level": "info",
#                         "log_filename": "../log/zqw_bx.log",
#                         "crawler":
#                         {
#                             "name": "ZQWNewsPipeline.ZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.youth.cn/finance_insurance/",
#                                 "data_path": "../data/zqw/",
#                                 "website_name": "中青网",
#                                 "b_class": "保险",
#                                 "checkpoint_filename": "../ckpt/zqw_bx.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZQWNewsPipeline.ZQWNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     },# end of zqw/bx
#                     {
#                         "name": "图解财经",
#                         "log_level": "info",
#                         "log_filename": "../log/zqw_tjcj.log",
#                         "crawler":
#                         {
#                             "name": "ZQWNewsPipeline.ZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.youth.cn/201761tjcj/",
#                                 "data_path": "../data/zqw/",
#                                 "website_name": "中青网",
#                                 "b_class": "图解财经",
#                                 "checkpoint_filename": "../ckpt/zqw_tjcj.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZQWNewsPipeline.ZQWNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     },# end of zqw/tjcj
#                     {
#                         "name": "食品",
#                         "log_level": "info",
#                         "log_filename": "../log/zqw_sp.log",
#                         "crawler":
#                         {
#                             "name": "ZQWNewsPipeline.ZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.youth.cn/finance_food/",
#                                 "data_path": "../data/zqw/",
#                                 "website_name": "中青网",
#                                 "b_class": "食品",
#                                 "checkpoint_filename": "../ckpt/zqw_sp.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZQWNewsPipeline.ZQWNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     },# end of zqw/sp
#                     {
#                         "name": "科技",
#                         "log_level": "info",
#                         "log_filename": "../log/zqw_kj.log",
#                         "crawler":
#                         {
#                             "name": "ZQWNewsPipeline.ZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.youth.cn/finance_IT/",
#                                 "data_path": "../data/zqw/",
#                                 "website_name": "中青网",
#                                 "b_class": "科技",
#                                 "checkpoint_filename": "../ckpt/zqw_kj.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZQWNewsPipeline.ZQWNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     },# end of zqw/kj
#                     {
#                         "name": "消费",
#                         "log_level": "info",
#                         "log_filename": "../log/zqw_xf.log",
#                         "crawler":
#                         {
#                             "name": "ZQWNewsPipeline.ZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.youth.cn/finance_cyxfgsxw/",
#                                 "data_path": "../data/zqw/",
#                                 "website_name": "中青网",
#                                 "b_class": "消费",
#                                 "checkpoint_filename": "../ckpt/zqw_xf.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZQWNewsPipeline.ZQWNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     },# end of zqw/xf
#                     {
#                         "name": "房产",
#                         "log_level": "info",
#                         "log_filename": "../log/zqw_fc.log",
#                         "crawler":
#                         {
#                             "name": "ZQWNewsPipeline.ZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.youth.cn/finance_house/",
#                                 "data_path": "../data/zqw/",
#                                 "website_name": "中青网",
#                                 "b_class": "房产",
#                                 "checkpoint_filename": "../ckpt/zqw_fc.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZQWNewsPipeline.ZQWNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     },# end of zqw/fc
#                     {
#                         "name": "独家稿件",
#                         "log_level": "info",
#                         "log_filename": "../log/zqw_djgj.log",
#                         "crawler":
#                         {
#                             "name": "ZQWNewsPipeline.ZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.youth.cn/finance_djgj/",
#                                 "data_path": "../data/zqw/",
#                                 "website_name": "中青网",
#                                 "b_class": "独家稿件",
#                                 "checkpoint_filename": "../ckpt/zqw_djgj.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZQWNewsPipeline.ZQWNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     },# end of zqw/djgj
#                     {
#                         "name": "专题策划",
#                         "log_level": "info",
#                         "log_filename": "../log/zqw_ztch.log",
#                         "crawler":
#                         {
#                             "name": "ZQWNewsPipeline.ZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.youth.cn/finance_ztch/",
#                                 "data_path": "../data/zqw/",
#                                 "website_name": "中青网",
#                                 "b_class": "专题策划",
#                                 "checkpoint_filename": "../ckpt/zqw_ztch.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZQWNewsPipeline.ZQWNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     },# end of zqw/ztch
#                     {
#                         "name": "资本市场",
#                         "log_level": "info",
#                         "log_filename": "../log/zqw_zbsc.log",
#                         "crawler":
#                         {
#                             "name": "ZQWNewsPipeline.ZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.youth.cn/finance_zqjrrdjj/",
#                                 "data_path": "../data/zqw/",
#                                 "website_name": "中青网",
#                                 "b_class": "资本市场",
#                                 "checkpoint_filename": "../ckpt/zqw_zbsc.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZQWNewsPipeline.ZQWNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     },# end of zqw/zbsc
#                     {
#                         "name": "IPO调查",
#                         "log_level": "info",
#                         "log_filename": "../log/zqw_ipodc.log",
#                         "crawler":
#                         {
#                             "name": "ZQWNewsPipeline.ZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.youth.cn/finance_ipo/",
#                                 "data_path": "../data/zqw/",
#                                 "website_name": "中青网",
#                                 "b_class": "IPO调查",
#                                 "checkpoint_filename": "../ckpt/zqw_ipodc.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZQWNewsPipeline.ZQWNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     },# end of zqw/ipodc
#                     {
#                         "name": "曝光台",
#                         "log_level": "info",
#                         "log_filename": "../log/zqw_bgt.log",
#                         "crawler":
#                         {
#                             "name": "ZQWNewsPipeline.ZQWNewsCrawler",
#                             "params":
#                             {
#                                 "list_url_tpl": "http://finance.youth.cn/finance_consumption/",
#                                 "data_path": "../data/zqw/",
#                                 "website_name": "中青网",
#                                 "b_class": "曝光台",
#                                 "checkpoint_filename": "../ckpt/zqw_bgt.ckpt",
#                                 "checkpoint_saved_days": 10
#                                 #"log_filename": "./test1.log"
#                             }
#                         },
#                         "transformers": [
#                             {
#                                 "name": "ZQWNewsPipeline.ZQWNewsContentParser",
#                                 "params": {}
#                             },
#                             # mysql_uploader_processor_conf,
#                         ],
#                         "uploader": mysql_uploader_conf
#                     }# end of zqw/bgt
#                 ]
#             }  # end of 中青网
#         ]  # end of the list of websites
# }
