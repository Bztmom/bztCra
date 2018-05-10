# -*- coding: utf-8 -*-

############################################
##
# defination of new crawler framework
##
##
#############################################

import logging
import sys
import time
#from XX_ES.XX_ESImporter.ESImporter import ESImporter
from multiprocessing import Process, Pool,Queue
from Utils import *
import traceback
from XXProcessors import *
from .XXCrawlers import *
from conf.common import online_mysql_uploader_conf as db_conf
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#define size of processor pool
MAX_PROC_NUM = 12

#define exception of conf check
class NewsConfException(Exception):
    """Exception for News pipeline configuration
    """
    pass


class NewsPipeline():
    """
    defination of news pipeline
    which is the main class 
    """
    def __init__(self, conf):
        '''
        conf = {"websites":[
          {
            "domain":"money.163.com",
            "pipelines":[
              {
                  "crawler":{"name":"XXNewsCrawler.NewsCralwer","params":{"start_url":"class_name"}},
                  "transformaer":[{"name":"XXNewsCrawler.XX,"params":""}],
                  "uplaoder":{"name":"","params":""}
              },
              {
                  "crawler":{"name":"XXNewsCrawler.NewsCralwer","params":{"start_url":"class_name_B"}},
                  "transformaer":{"name":"XXNewsCrawler.XX,"params":""},
                  "uplaoder":{"name":"","params":""}
              }
            ]
          }
        ]}
        '''
        # check format of configuration file
        if "websites" not in conf:
            raise NewsConfException('No "websites" field in pipeline conf')
        if not isinstance(conf["websites"],list):
            raise NewsConfException('conf["websites"] is no a list')
        for i, domain_info in enumerate(conf["websites"]):
            if "domain_name" not in domain_info:
                raise NewsConfException('No "domain_name" field in No.%d website'%(i+1))
            if "pipelines" not in domain_info:
                raise NewsConfException('No "pipelines" field in website %s'%(domain_info["domain_name"]))
        self.conf = conf

        ###read keywords list from mysql and write it down
        # #download keywords list
        params = db_conf["params"]
        DownloadKWProcessor(**params).process({})
        self.website_counter = 1
        pass

    def run(self):
        '''
        run in multi process
        same domain in the same process
        '''
        p_list = []
        start_time = time.time()
        print "Start crawling ... "
        #pool = Pool(processes =2)
        # logger = InitLog("pipeline.log", logging.getLogger("pipeline.log"), "info")
        task_queue = Queue()
        #put all task to task queue(A task is a crawling task for one website)
        for index, domain_info in enumerate(self.conf["websites"]):
            domain_info["site_cnt"] = len(self.conf["websites"])
            task_queue.put(domain_info)

        print "there are %d tasks"%(task_queue.qsize())
        #construct processor pool
        for proc_i in range(MAX_PROC_NUM):

            nw = NewsWorker(task_queue)
            print "start proc %d"%(proc_i+1)
            nw.start()
            p_list.append(nw)
            #break
        
        #put end of task to task queue
        for i in range(MAX_PROC_NUM):
            task_queue.put( None ) 

        #wait for all processor finished
        for p in p_list:
            p.join()
        print "Crawling finished ... cost %fs "%(time.time() - start_time)


class NewsWorker(Process):
    """
    Pipeline worker, every worker would run one website
    """
    def __init__(self, queue):
        super(NewsWorker, self).__init__()
        self.queue = queue
        # todo: check conf format
        

    def check_conf(self, conf):
        # if not isinstance(conf,list):
        #     raise NewsConfException('conf["pipelines"] for website %s is not a list'%(domain_name))
        pipeline_fields = ["name","log_level","log_filename","crawler","transformers","uploader"]
        
        for i, pipeline_conf in enumerate(conf["pipelines"]):
        	#check if all required fields are in conf
            for pfield in pipeline_fields:
                if pfield not in pipeline_conf:
                    raise NewsConfException('Key "%s" not in No.%d pipeline of website %s'%(pfield,i+1,domain_name))
            #check data type
            if not isinstance(pipeline_conf["transformers"],list):
                raise NewsConfException('transformers of pipeline %s in website %s is not a list'%(pipeline_conf["name"],domain_name))
            pipeline_workers = ["crawler","uploader"]
            for pworker in pipeline_workers:
                if "name" not in pipeline_conf[pworker]:
                    raise NewsConfException('No "name" in %s of pipeline %s of website %s'%(pworker,pipeline_conf["name"],domain_name))
                if "params" not in pipeline_conf[pworker]:
                    raise NewsConfException('No "params" in %s of pipeline %s of website %s'%(pworker,pipeline_conf["name"],domain_name))
            for j,pworker in enumerate(pipeline_conf["transformers"]):
                if "name" not in pworker:
                    raise NewsConfException('No "name" in No.%d transformer of pipeline %s of website %s'%(j+1,pipeline_conf["name"],domain_name))
                if "params" not in pworker:
                    raise NewsConfException('No "params" in No.%d transformer of pipeline %s of website %s'%(j+1,pipeline_conf["name"],domain_name))
        self.conf = conf
        self.domain_name = conf["domain_name"]
        # todo: check conf format

    def run(self):
        '''
        '''
        for conf in iter( self.queue.get, None ): 
            self.check_conf(conf)
            self.run_pipelines()

    def run_pipelines(self):
        '''run multi pipelines for the same domain in same process
        '''
        print "start pipeline for ", self.domain_name, self.conf["site_cnt"] - self.queue.qsize() + MAX_PROC_NUM
        start_time = time.time()
        #iterate all pipelines(channels)
        for pipeline_conf in self.conf["pipelines"]:
            # self.base_logger.info("stat:task:%s:%s:start:" % (
            #         self.domain_name, pipeline_conf["name"]) + str(datetime.now()))
            try:
                # init logging module
                log_level = pipeline_conf["log_level"]
                log_filename = pipeline_conf["log_filename"]
                #init log file
                logger = InitLog(log_filename, logging.getLogger(
                    log_filename), log_level)
                logger.info("stat:task:%s:%s:start:" % (
                    self.domain_name, pipeline_conf["name"]) + str(datetime.now()))
                #set logger for crawler and uploader
                pipeline_conf["crawler"]["params"]["logger"] = logger
                pipeline_conf["uploader"]["params"]["logger"] = logger
                # assemble pipeline
                crawler = import_object(
                    pipeline_conf["crawler"]["name"], pipeline_conf["crawler"]["params"])
                transformers = []
                # init transformer list
                for transformer_info in pipeline_conf["transformers"]:
                    transformer_info["params"]["logger"] = logger
                    transformers.append(import_object(
                        transformer_info["name"], transformer_info["params"]))
                # add kw processor and assembleMysqlprocessor to the list
                transformers.append(KWNewsProcessor(logger=logger))
                transformers.append(AssembleMySQLNewsProcessor(logger=logger))
                #init uploader
                uploader = import_object(
                    pipeline_conf["uploader"]["name"], pipeline_conf["uploader"]["params"])

                #run the pipeline
                for news_info in crawler.run():
                    if news_info is None:
                        continue
                    logger.info("stat:transform:start:" + str(datetime.now()))
                    transform_error = False
                    for index, transformer in enumerate(transformers):
                        try:
                            # with open("../data/temp_%d.txt"%index,"wb") as fd:
                            #     news_info["pub_date"] = ""
                            #     fd.write(json.dumps(news_info,ensure_ascii=False))
                            transformer.process(news_info)
                        except NewsProcessor.ProcessorException as pe:
                            logger.info(
                                "stat:transform:end:failed:" + pe.message +":"+news_info['filename'])
                            transform_error = True
                            break
                    if transform_error:
                        continue
                    logger.info("stat:transform:end:success:" +
                                str(datetime.now()))
                    try:
                        logger.info("stat:upload:start:" + str(datetime.now()))
                        uploader.upload(news_info)
                    except NewsUploader.UploadException as ue:
                        logger.info(
                                "stat:upload:end:failed:" + ue.message +":"+news_info['filename'])
                uploader.commit()
                for transformer in reversed(transformers):
                    try:
                        transformer.process_finish()
                    except NewsProcessor.ProcessorException as e:
                        logger.warning("stat:transform:finish_failed"+":"+news_info['filename'])
                logger.info("stat:task:end:success:" + str(datetime.now()))
                # self.base_logger.info("stat:task:end:" + str(datetime.now()))
                #break
            except Exception as e:
                import traceback
                traceback.print_exc()
                crawler.dump_checkpoint()
                logger.info("stat:task:end:failed:" + e.message + ":" + str(datetime.now()) )
                traceback.print_exc()

        print self.domain_name + " finished cost %fs"%(time.time() - start_time)
