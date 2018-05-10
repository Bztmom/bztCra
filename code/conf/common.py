# -*- coding: utf-8 -*-

es_uploader_conf = {
    "name": "XX_Crawler.XXUploaders.NewsUploader",
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


fs_uploader_conf = {
    "name": "XX_Crawler.XXUploaders.FSUploader",
    "params": {
        "data_path": "../data/qjw/"
    }
}

mysql_uploader_conf = {
    "name": "XX_Crawler.XXUploaders.MySQLUploader",
    "params": {
        "db_addr": "59.110.231.53",
        "db_name": "news",
        "table_name": "li_public_opinion_simple",
        "username": "news_user",
        "password": "news_password",
    }
}
'''
online_mysql_uploader_conf = {
    "name": "XX_Crawler.XXUploaders.MySQLUploader",
    "params":{
        "db_addr": "60.205.205.175",
        "db_name": "yq_test",
        "table_name": "li_public_opinion_simple",
        "username": "yq_test",
        "password": "Yq@123456",
    }
}
'''

online_mysql_uploader_conf = {
    "name": "XX_Crawler.XXUploaders.MySQLUploader",
    "params":{
        "db_addr": "127.0.0.1",
        "db_name": "public_opinion",
        "table_name": "li_public_opinion_simple",
        "username": "crawler",
        "password": "Crawler#54321",
    }
}

es_uploader_processor_conf = {
    "name": "XX_Crawler.XXProcessors.ESUploadProcessor",
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
