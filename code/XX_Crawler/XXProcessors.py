# -*- coding: utf-8 -*-

############################################
##
# defination of new crawler framework
##
##
#############################################

import re
import json
import MySQLdb
import logging
from datetime import datetime
from .XXUploaders import NewsUploader
from types import MethodType
from collections import defaultdict
from .XXCrawlers import NewsCrawler

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class NewsProcessor():
    '''
    base news process
    main logic in process function which take
    news_info and doc as parameters
    '''

    def __init__(self, logger):
        if logger is None:
            self.logger = logging.getLogger()
        else:
            self.logger = logger
        pass

    def process(self, news_info):
        return True

    def process_finish(self):
        pass

    class ProcessorException(Exception):
        """Exception for processors
        """
        pass


class AssembleNewsProcessor(NewsProcessor):
    '''
    assemble news processor which is used for
    assemble news meta data and parsed content
    '''

    def __init__(self, logger=None):
        NewsProcessor.__init__(self, logger)
        pass

    def generate_news_id(self, news_info):
        try:
            news_id = news_info["filename"].split("/")[-1].split(".")[0]
            return news_id
        except:
            # todo print warning
            return None

    def process(self, news_info):
        news_info["_id"] = self.generate_news_id(news_info)
        return True


class AssembleMySQLNewsProcessor(NewsProcessor):
    '''
    assemble news processor which is used for
    assemble news meta data and parsed content
    '''

    def __init__(self, logger=None):
        NewsProcessor.__init__(self, logger)
        self.domain_pattern = re.compile(
            r'(https?:\/\/|^)(?P<domain_name>.*?)(\/|$)')
        pass

    def generate_news_id(self, news_info):
        try:
            news_id = news_info["filename"].split("/")[-1].split(".")[0]
            return news_id
        except:
            # todo print warning
            return None

    def process(self, news_info):
        news_info["_id"] = self.generate_news_id(news_info)
        for key, value in news_info.iteritems():
            if isinstance(value, list):
                value = ",".join(value)
            elif isinstance(value, dict):
                value = json.dumps(value)
            elif isinstance(value, datetime):
                value = datetime.strftime(value, "%Y-%m-%d %H:%M:%S")
            elif isinstance(value, basestring) or isinstance(value, unicode):
                value = value.strip("\n ")
            elif isinstance(value, NewsCrawler):
                continue
            elif value is None:
                # if value is None
                self.logger.debug(key + " is None")
                continue
            else:
                # if value type is not known
                self.logger.debug(key + " is a " + str(type(value)))
                continue
            value = MySQLdb.escape_string(value)
            news_info[key] = value
        for feature in ["comment_cnt", "view", "hot"]:
            if feature not in news_info:
                news_info[feature] = 0
        for feature in ["summary", "source", "author"]:
            if feature not in news_info:
                news_info[feature] = ''

        # extract domain info
        news_info["domain"] = "unknown"
        matched = self.domain_pattern.match(news_info["url"])
        if matched:
            news_info["domain"] = matched.group("domain_name")

        return True


class ESUploadProcessor(AssembleNewsProcessor, NewsUploader):
    '''upload doc to es
    '''

    def __init__(self, logger, es_server_list, index_name, type_name):
        NewsProcessor.__init__(self, logger)
        NewsUploader.__init__(self, es_server_list,
                              index_name, type_name, logger)
        self.es_server_list = es_server_list
        self.index_name = index_name
        self.type_name = type_name

        pass

    def process(self, news_info):
        try:
            ret_dict = {}
            ret_dict["_id"] = self.generate_news_id(
                news_info, news_info["content"])
            ret_dict["content"] = doc
            ret_dict["meta"] = news_info
            self.upload(ret_dict)
            return doc
        except Exception as e:
            raise NewsProcessor.ProcessorException(
                "Failed to upload to es :" + e.message)
        pass

    def process_finish(self):
        try:
            self.commit()
        except Exception as e:
            raise NewsProcessor.ProcessorException(
                "Failed to commit :" + e.message)
        pass


class DetailNewsContentParser(NewsProcessor):
    '''
    this processor parse the news detail according to 
    the regex patterns in the conf
    '''

    def __init__(self, detail_patterns, logger=None, multi_news_page_func=None):
        NewsProcessor.__init__(self, logger)
        self.detail_patterns = [re.compile(
            detail_pattern, re.DOTALL) for detail_pattern in detail_patterns]
        if multi_news_page_func is not None:
            self.multi_news_page = MethodType(multi_news_page_func, self)
        pass

    # check if there are multi page in news
    def multi_news_page(self, news_info, content):
        '''check if there are multi page in news
        if yes, yield next url, otherwise nothing
        '''
        yield None

    def process(self, news_info):
        try:
            self.logger.debug("start news detail process")
            ori_content = news_info['content']
            matched = ""
            for detail_pattern in self.detail_patterns:
                matched_once = detail_pattern.search(news_info["content"])
                if matched_once:
                    matched = matched_once
                    break
                pure_page_content = None
            if matched:
                self.logger.debug("content matched")
                for key, value in matched.groupdict().iteritems():
                    if key == "pub_date":
                        # trim pub_date field
                        value = value.replace("&nbsp;", " ")
                        value = value.replace("\xc2\xa0", "")
                        value = value.replace("\n", " ")
                        value = value.strip()
                        self.logger.debug(
                            "pub_date value:" + value + "end")
                        if isinstance( news_info["crawler"].pub_date_format , list):
                            for val in news_info["crawler"].pub_date_format:
                                try:
                                    value = datetime.strptime(value, val)
                                except:
                                    self.logger.debug("pub_date re abnormal")
                        else:
                            value = datetime.strptime(value, news_info["crawler"].pub_date_format)
                    news_info[key] = value
                    # self.logger.debug(key+"==="+ value)
                self.logger.debug("finish assigning field")
                # todo: multi page check and content concat
                for content in self.multi_news_page(news_info, ori_content):
                    if content is None:
                        break
                    news_info["content"] += content
                # check and combine part key
                part_key_dict = defaultdict(int)
                for key in news_info.keys():
                    if key.startswith("part_"):
                        items = key.split("_")
                        if len(items) < 4:
                            continue
                        order = int(items[1])
                        real_key = "_".join(items[2:])
                        if order > part_key_dict[real_key]:
                            part_key_dict[real_key] = order
                # combine the part_patten defination
                for key, max_order in part_key_dict.iteritems():
                    for order in range(1, max_order + 1):
                        act_key = "part_%d_%s" % (order, key)
                        if act_key in news_info:
                            news_info[key] = news_info.get(
                                key, "") + news_info[act_key]
                            del news_info[act_key]
                    if key == "pub_date":
                        value = news_info[key]
                        value = value.replace("&nbsp;", " ")
                        value = value.replace("\xc2\xa0", "")
                        value = value.replace("\n", " ")
                        value = value.strip(" ")
                        # print value
                        if isinstance( news_info["crawler"].pub_date_format , list):
                            for val in news_info["crawler"].pub_date_format:
                                try:
                                    value = datetime.strptime(value, val)
                                except:
                                    self.logger.debug("pub_date re abnormal")
                        else:
                            value = datetime.strptime(value, news_info["crawler"].pub_date_format)
                        news_info[key] = value
                # deal with pub_date

            else:
                raise NewsProcessor.ProcessorException(
                    "No detail template matched")
            self.logger.debug("end news detail process")

        except Exception as e:
            # import traceback
            # traceback.print_exc()
            if isinstance(e, NewsProcessor.ProcessorException):
                raise e
            else:
                raise NewsProcessor.ProcessorException(
                    "Fail to parse url: %s: " % (news_info["url"]) + e.message)
            return None
            pass


###
##
# find out keywords of news
##
###
class KWNewsProcessor(NewsProcessor):
    '''
    the processor figure out the keywords in news detail
    '''

    def __init__(self, logger=None):
        NewsProcessor.__init__(self, logger)
        self.keywords_list = []

    def init_keywords(self, keyword_file='../data/keywords.list'):
        self.keywords_list = []
        # with open(keyword_file, 'r') as fin:
        #     for line in fin:
        #         if line.strip()[0] == "#":
        #             continue
        #         self.keywords_list.append(line.strip("\n"))

    def process(self, news_info):

        content = news_info["content"]
        if not self.keywords_list:
            self.init_keywords()
        counter = 0
        if "keywords" not in news_info:
            news_info["keywords"] = []
        for key in self.keywords_list:
            # self.logger.debug("keyword ==> "+key.decode("utf-8"))
            # test_content = content.decode("utf-8")
            if key in content:
                counter += 1
                news_info["keywords"].append(key)
        self.logger.debug("found %d keywords" % counter)
        return True


class HTMLTagFilter(NewsProcessor):
    '''
    this processor filter the tags of html
    '''
    def __init__(self, logger=None):
        NewsProcessor.__init__(self, logger)
        # todo: assemble re pattern
        self.keep_all_pattern = re.compile(
            r"<(?P<tag_name>p|span|table|tr|th|td|td|img|br|h1|h2|h3|section)(>| .*?>).*?<\/(?P=tag_name)>", re.DOTALL | re.IGNORECASE)

    def process(self, news_info):
        content = news_info["content"]
        new_content = ""
        for m in self.keep_all_pattern.finditer(content):
            new_content += m.group(0)
            new_content += "\n"
        news_info["content"] = new_content


class DownloadKWProcessor(NewsProcessor):
    '''
    this processor download the keyword list from db
    and write to file
    '''
    def __init__(self, db_addr, db_name, table_name, username, password, logger=None, keyword_file='../data/keywords.list'):
        NewsProcessor.__init__(self, logger)
        self.sql = """select keyword from li_default_keywords
                      union all
                      select keywords as keyword from li_user_keywords
                    """
        print db_addr,username,password,db_name
        self.db = MySQLdb.connect(
            db_addr, username, password, db_name, charset="utf8")
        self.table_name = table_name
        self.filename = keyword_file

    def process(self, news_info):
        try:
            self.cursor = self.db.cursor()
            # 执行sql语句
            # doc["title"] = doc["title"].decode("utf-8")
            n = self.cursor.execute(self.sql)
            keywords = []
            for row in self.cursor.fetchall():
                keywords.append(row[0].encode("utf-8"))
            # 提交到数据库执行
            self.db.commit()
            self.db.close()
            with open(self.filename, "wb") as fd:
                for kw in keywords:
                    fd.write(kw + "\n")
        except Exception as e:
            self.logger.debug(e.message)
            self.db.rollback()


if __name__ == "__main__":
    import re

    content = '''<style type="text/css">.TRS_Editor P{line-height:1.5;font-family:;font-size:15pt;}.TRS_Editor DIV{line-height:1.5;font-family:;font-size:15pt;}.TRS_Editor TD{line-height:1.5;font-family:;font-size:15pt;}.TRS_Editor TH{line-height:1.5;font-family:;font-size:15pt;}.TRS_Editor SPAN{line-height:1.5;font-family:;font-size:15pt;}.TRS_Editor FONT{line-height:1.5;font-family:;font-size:15pt;}.TRS_Editor UL{line-height:1.5;font-family:;font-size:15pt;}.TRS_Editor LI{line-height:1.5;font-family:;font-size:15pt;}.TRS_Editor A{line-height:1.5;font-family:;font-size:15pt;}</style><style type="text/css">

.TRS_Editor P{line-height:1.5;font-family:;font-size:15pt;}.TRS_Editor DIV{line-height:1.5;font-family:;font-size:15pt;}.TRS_Editor TD{line-height:1.5;font-family:;font-size:15pt;}.TRS_Editor TH{line-height:1.5;font-family:;font-size:15pt;}.TRS_Editor SPAN{line-height:1.5;font-family:;font-size:15pt;}.TRS_Editor FONT{line-height:1.5;font-family:;font-size:15pt;}.TRS_Editor UL{line-height:1.5;font-family:;font-size:15pt;}.TRS_Editor LI{line-height:1.5;font-family:;font-size:15pt;}.TRS_Editor A{line-height:1.5;font-family:;font-size:15pt;}</style>
<p><strong>　　大势猜想：市场并未形成真正支撑</strong></p>
<p>　　今日(11月17日)，沪深两市小幅低开，延续弱势格局。沪指报3382.91点，下跌0.48%；深证成指报11292.93点，跌2.12%；创业板指报1833.90点，跌2.36%。从盘面上看，仅银行、保险、民航板块逆市走强，两市下跌股票接近3000只，近百股跌停。</p>
<p>　　天信投顾指出，虽然今日盘中存在银行、保险、券商等金融板块的上涨，但是市场却继续出现下跌，说明市场并未真正的形成支撑，目前沪指刚好处在60日均线支撑这个位置，能否支撑还需要观察，另外，沪指在3350点位置的支撑也要特别关注。</p>
<p><strong>　　资金猜想：短期股指依然承压</strong></p>
<p>　　今日，央行进行100亿元7天逆回购操作、100亿元14天期逆回购操作、100亿元63天期逆回购操作，有400亿元逆回购到期。</p>
<p>　　分析人士指出，低超储率环境下，流动性易紧难松，尤其是临近年底，机构对中长期资金需求增多，容易引发、阶段性资金供求紧张。不过，年底通常是财政投放高峰期，配合央行削峰填谷的操作，预计市场资金面不会持续大幅偏离紧平衡的状态。</p>
<p>　　和信投顾认为，从周K线的角度来看，短期股指依然承压，除非反弹过程中能够出现配合较佳的量能，由于量能指标的存量博弈性质，这种反弹或较为艰难。</p>
<p>　　<strong>热点猜想：逢低介入科技股</strong></p>
<p>　　从消息面上看，11月10日，工业和信息化部原材料工业司、国家发展改革委产业协调司有关人员赴中国钢铁工业协会进行了三方会商，与会三方就2017年钢铁行业开展的主要工作及2018年重点工作安排交换了意见。</p>
<p>　　北京博星证券指出，操作上唯有顺势而为，抓大放小，建议控制好整体仓位，等待A股利空消化后的再次突破机会，目前卖高买低的逆向思维依然适用，逢低把握科技、消费类白马的介入机会，关注年末机构调仓换股的投资路线。</p>
       <div class="blank10"></div>
        <!-- 附件列表 -->
         <div class="list_fj">
             <ul>
                  
             </ul>
        </div>  
      <!-- 翻页 -->
        <div class="page"> <SCRIPT LANGUAGE="JavaScript">
var currentPage = 0;//所在页从0开始
var prevPage = currentPage-1//上一页
var nextPage = currentPage+1//下一页
var countPage = 1//共多少页

//设置上一页代码
if(countPage>1&&currentPage!=0&&currentPage!=1)
    document.write("<a href=\"t20171117_5577604"+"_" + prevPage + "."+"html\" target='_self'>上一页</a>");//加首页<a href=\"t20171117_5577604.html\" target='_self'>首页</a>
else if(countPage>1&&currentPage!=0&&currentPage==1)
    document.write("<a href=\"t20171117_5577604.html\" target='_self'>上一页</a>");
else
    document.write("");
//循环

var num = 20;
for(var i=0+(currentPage-1-(currentPage-1)%num) ; i<=(num+(currentPage-1-(currentPage-1)%num))&&(i<countPage) ; i++){
    if(currentPage==i&&countPage==1)
             document.write("");

    else if(currentPage==i)
        document.write("<span class=z_page_now>"+(i+1)+"</span>");
    else{
              if(i==0)
                   document.write("<a href=\"t20171117_5577604" + "."+"html\" target='_self'>"+(i+1)+"</a>");
                    else
               document.write("<a href=\"t20171117_5577604"+"_" + i + "."+"html\" target='_self'>"+(i+1)+"</a>");
             }
}

//设置下一页代码 
if(countPage>1&&currentPage!=(countPage-1))
    document.write("<a href=\"t20171117_5577604"+"_" + nextPage + "."+"html\" target='_self'>下一页</a>");//加尾页<a href=\"t20171117_5577604_" + (countPage-1) + ".html\" target='_self'>尾页</a>
else
    document.write("");

</SCRIPT></div>
    '''
    # tags_conf = {
    #     "keep_all":["p"],
    #     "keep_content":["div"]
    # }
    # import HTMLParser
    # html_parser = HTMLParser.HTMLParser()
    # content = html_parser.unescape(content)
    # processor = HTMLTagFilter(tags_conf)
    # processor.process({"content":content})
    params = {
        "db_addr": "60.205.205.175",
        "db_name": "yq_test",
        "table_name": "li_public_opinion_simple",
        "username": "yq_test",
        "password": "Yq@123456",
    }
    DownloadKWProcessor(**params).process({})
