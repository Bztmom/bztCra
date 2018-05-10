# -*- coding: utf-8 -*-

############################################
##
# defination of new crawler framework
##
##
#############################################

import logging
import MySQLdb
import json
from datetime import datetime
from .XXCrawlers import NewsCrawler

class NewsUploader():

    # , es_server_list, index_name, type_name):
    def __init__(self, es_server_list, index_name, type_name, logger=None):
        es_server_list = es_server_list
        index_name = index_name
        type_name = type_name
        #self.db_importer = ESImporter(es_server_list, index_name, type_name)
        if logger is None:
            self.logger = logging.getLogger()
        else:
            self.logger = logger
        pass

    def convert_to_string(self, doc):
        for k, v in doc.iteritems():
            if isinstance(v, datetime):
                doc[k] = datetime.strftime(v, "%y-%m-%d %H:%M:%S")
            elif isinstance(v, unicode):
                doc[k] = v.encode("utf-8")
            elif isinstance(v, dict):
                self.convert_to_string(v)
            elif isinstance(v, NewsCrawler):
                del doc[k]

    def upload(self, doc):
        # process doc convert datetime to str
        self.convert_to_string(doc)
        filename = doc["meta"]["filename"] + ".final"
        with open(filename, "w") as fd:
            fd.write(json.dumps(doc,ensure_ascii=False,indent=2)+"\n")
        #self.db_importer.insert_to_es(doc)
        pass

    def commit(self):
        #self.db_importer.commit_to_es()
        pass

    class UploadException(Exception):
        pass

class FSUploader(NewsUploader):
    '''
    write down data to local filesystem
    '''
    def __init__(self, data_path, logger):
        self.datapath = data_path
        self.logger = logger

    def upload(self, doc):
        self.convert_to_string(doc)
        filename = doc["filename"]+".parsed"
        #print >>sys.stderr,doc
        with open(filename, "wb") as fd:
            fd.write(json.dumps(doc,ensure_ascii=False))

class MySQLUploader(NewsUploader):
    '''
    upload data to mysql db
    '''

    def __init__(self, db_addr, db_name, table_name, username, password, logger = None):
        #connect to db
        self.db = MySQLdb.connect(db_addr,username,password,db_name, charset="utf8")
        self.table_name = table_name
        if logger is None:
            self.logger = logging.getLogger()
        else:
            self.logger = logger

    def upload(self, doc):
        #data type check
        if not isinstance(doc, dict):
            return False
        doc["table_name"] = self.table_name

        self.cursor = self.db.cursor()
        try:
            self.logger.debug("===>"+doc["pub_date"])
            sql_tpl = """INSERT INTO {table_name}(url,
             author, `from`, domain,site,channel, view, comment, isnegative, isneutral, ispositive,hot,title,summary,content, publish_time, keywords)
             VALUES ('{url}','{author}','{source}','{domain}','{website_name}','{b_class}','{view}','{comment_cnt}',-1,-1,-1,'{hot}','{title}','{summary}','{content}', '{pub_date}','{keywords}')"""
        except  Exception as e:
            raise NewsUploader.UploadException("field error : "+e.message)
        try:
            # 执行sql语句
            #doc["title"] = doc["title"].decode("utf-8")
            self.cursor.execute(sql_tpl.format(**doc))
            # 提交到数据库执行
            self.db.commit()
        except Exception as e:
            # Rollback in case there is any error
            # self.logger.debug(doc["table_name"])
            self.logger.debug(sql_tpl.format(**doc))
            self.logger.debug(e.message)
            self.db.rollback()
            raise NewsUploader.UploadException("mysql insert failed")

    def commit(self):
        # 关闭数据库连接
        self.db.close()