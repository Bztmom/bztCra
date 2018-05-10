# -*- coding: utf-8 -*-

############################################
##
# run all pipelines in conf file
##
##
#############################################


from XX_Crawler.XXNewsETL import *
from XX_Crawler.Utils import *
from conf import *
import sys
#from NewsPipelineConf import test_conf as conf

conf = {"websites": []}
##register website conf which is wanted
# registered_website = ['hzk_new', 'sina', 'dycj', 'cjw', 'zqw_new', 'ymcj', 'jrtzw', 'zwwcj', 'zgwcj', 'zcw',  'lzk_new', 'qjw', '21jjw', 'zzw', 'zqzx', 'hxcj', 'thsjj', 'gmw_new', 'hqcj_new', 'liejin99', 'zgqyxww', 'fhwcj', 'hxw', 'rmwcj', 'ecncj', 'swcj', 'zgjjw', 'zgjyw', 'sohu', 'yswcj', 'cjsb', 'dywcj', 'ljw', 'jrj', 'zgggb_new', 'nfcfw', 'dfcj', 'hgcj', 'ccwcj', 'jjgcw', 'ytcj', 'lhlc', 'zjzx', 'mrjjxw', 'xhcj_new', 'zqrb', 'dzwcj', '163_new', 'zgzqw', 'txcj', 'zqsb', 'jcwjr', 'cxw', 'yszq']
registered_website = ['cjw']
for website_name in registered_website:
    website_name = "conf.%s"%(website_name)
    if website_name not in sys.modules:
        #print sys.modules
        print >> sys.stderr, website_name+" is not found in conf directory"
        exit(1)
    conf["websites"].append(sys.modules[website_name].conf)

if __name__ == "__main__":
    try:
        npl = NewsPipeline(conf)
        npl.run()
    except Exception as e:
        import traceback
        traceback.print_exc()
        print >> sys.stderr, e.message
