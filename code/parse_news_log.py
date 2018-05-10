# -*- coding: utf-8 -*-

import os
import re
from datetime import datetime
import json
from XX_Crawler.Mail import send_mail

class LogParser:
    def __init__(self, log_filename):
        self.log_filename = log_filename
        self.log_content = ""
        self.lines = []
        self.log_info = {}
        self.start_time = ""
        self.end_time = ""
        # re patterns
        self.patterns = {
            "task_start": re.compile("INFO==>stat:task:.*start:"),
            "task_end": re.compile("INFO==>stat:task:end:(.*)"),
            "list_fail": re.compile("ERROR==>stat:download:start:failed:(.*)"),
            "download_start": re.compile("INFO==>stat:download:start:(.*)"),
            "download_fail": re.compile("INFO==>stat:download:end:failed:(.*)"),
            "transform_start": re.compile("INFO==>stat:transform:start:"),
            "transform_fail": re.compile("INFO==>stat:transform:end:failed:.*|stat:transform:finish_failed.*")
        }
        # self.task_start_pattern = re.compile("INFO==>stat:task:.*start:")
        # self.task_end_pattern = re.compile("INFO==>stat:task:end:(.*)")
        # self.list_fail_pattern = re.compile("INFO==>stat:download:failed:.*")
        # self.download_start_pattern = re.compile("INFO==>stat:download:start:(.*)")
        # self.download_fail_pattern = re.compile("INFO==>stat:download:end:failed:(.*)")
        # self.transform_start_pattern = re.compile("INFO==>stat:transform:start:")
        # self.transform_fail_pattern = re.compile("INFO==>stat:transform:end:failed:.*|stat:transform:finish_failed.*")

    def last_run_log(self):
        '''
        Get the logs for most recent run,
        which are contents after last "task start"
        and extract some task status info
        '''
        log_content = ""
        with open(self.log_filename, "r") as f:
            for line in f:
                if self.patterns["task_start"].search(line):
                    log_content = line
                    self.start_time = ":".join(line.split(":")[-3:]).strip()
                    self.website_name = line.split(":")[-6]
                    self.b_class = line.split(":")[-5]
                else:
                    log_content += line
                    task_end_info = self.patterns["task_end"].search(line)
                    if task_end_info:
                        end_line = task_end_info.group(1)
                        self.end_time = ":".join(line.split(":")[-3:]).strip()
                        # self.website_name = line.split(":")[-6]
                        # self.b_class = line.split(":")[-5]
        self.log_content = log_content
        if re.search("failed", end_line):
            task_success = False
            time_str = '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{6}'
            fail_info = re.findall("failed:(.*):" + time_str, end_line)[0]
        else:
            task_success = True
        task_cost = datetime.strptime(self.end_time, '%Y-%m-%d %H:%M:%S.%f') - datetime.strptime(self.start_time,
                                                                                                 '%Y-%m-%d %H:%M:%S.%f')
        self.log_info["task"] = {
            "website_name": self.website_name,
            "class_name": self.b_class,
            "task_success": task_success,
            "cost": str(task_cost),
            "start_time": datetime.strptime(self.start_time, '%Y-%m-%d %H:%M:%S.%f')}
        if not task_success:
            self.log_info["task"]["fail_info"] = fail_info
        return log_content

    def get_download_failed_url(self):
        fail_url_list = []
        if not self.lines:
            self.lines = self.log_content.split("\n")
        for line in self.lines:
            if line.strip() == "":
                continue
            download_url_info = self.patterns["download_start"].search(line)
            if download_url_info:
                url = download_url_info.group(1)
            fail_info = self.patterns["download_fail"].search(line)
            if fail_info:
                fail_url_list.append({"url": url, "fail_info": fail_info.group(1)})
        return fail_url_list

    # def get_trans_failed_filename(self):
    #     fail_file_list = []
    #     failed_info = self.patterns["transform_fail"].findall(self.log_content)
    #     return [info.split(":")[-1] for info in failed_info]

    def parse_log(self):
        log_content = self.last_run_log()
        if self.patterns["list_fail"].search(log_content):  # 若未解析出一页list页面，则任务失败
            self.log_info["task"]["task_success"] = False
            self.log_info["task"]["failed_list"] = self.patterns["list_fail"].search(log_content).group(1)
        warnings = re.findall("WARNING==>(.*)", log_content)
        self.log_info["task"]["warnings"] = len(warnings)
        if len(warnings) > 0:
            self.log_info["task"]["warning_info"] = warnings
        # warning_urls = [w.split("url:")[-1].strip().split(" ")[0] for w in warnings]
        # crawler info
        count_download_failed = len(self.patterns["download_fail"].findall(log_content))
        fail_url_list = []
        lose_page = 0
        if count_download_failed > 0:  # list the failed url
            fail_url_list = self.get_download_failed_url()
            for key in fail_url_list:
                if key["fail_info"] == "requests return 404":
                    lose_page += 1
            if (lose_page < len(fail_url_list)):
                self.log_info["task"]["task_success"] = False
        self.log_info["crawler"] = {
            "total_news": len(self.patterns["download_start"].findall(log_content)),
            "failed_news": count_download_failed,
            "failed_url": fail_url_list
        }
        self.log_info["task"]["total_news"] = self.log_info["crawler"]["total_news"]
        # transformers info
        trans_failed_info = self.patterns["transform_fail"].findall(log_content)
        count_trans_failed = len(trans_failed_info)
        fail_file_list = []
        if count_trans_failed > 0:
            self.log_info["task"]["task_success"] = False
            fail_file_list = [info.split(":")[-1] for info in trans_failed_info]
        self.log_info["transformer"] = {
            "total_news": len(self.patterns["transform_start"].findall(log_content)),
            "failed_news": count_trans_failed,
            "failed_file": fail_file_list
        }
        return self.log_info


if __name__ == "__main__":
    if not os.path.exists("../task_info/"):
        os.mkdir("../task_info/")
    now_date = datetime.now()
    transformerFailed = 0
    crawlerFailed = 0
    website = 0
    newsCount = 0
    errorHtml = ''
    for filename in os.listdir('../log'):
        try:
            log_name, extension = os.path.splitext(filename)
            if extension != ".log":
                continue
            parser = LogParser('../log/' + filename)
            log_info = parser.parse_log()
            if (log_info['task']['task_success'] == False):
                errtype = '列表获取异常'
                errCount = log_info['task'].get("failed_list","0")
                if (log_info['transformer']['failed_news'] != 0):
                    errtype = '页面匹配异常'
                    errCount = '错误条数：'+str(log_info['transformer']['failed_news'])
                if (log_info['crawler']['failed_news'] != 0):
                    errtype = '页面下载异常'
                    errCount = '错误条数：'+str(log_info['crawler']['failed_news'])
                errorHtml += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (log_info['task']['website_name'], log_info['task']['class_name'], errtype, errCount)
            t = log_info["task"]["start_time"]
            log_info["task"]["start_time"] = t.strftime("%Y-%m-%d %H:%M:%S")
            log_name = log_name.split("_")[0]
            output_file = "../task_info/" + log_name + "_" + now_date.strftime("%Y%m%d%H%M") + ".json"
            with open(output_file, 'a') as f:
                json.dump(log_info, f)
                f.write("\n")
        except:
            print "failed to parse ", filename
            continue
    if errorHtml != '':
        send_mail( "正式爬虫报警信息",errorHtml )
    # to sms message not sms message to email
    # os.system('python /home/crawler/dysms_python/sms_send.py ' +"TF%dCF%dL%dN%d" %(transformerFailed,crawlerFailed,website,newsCount))
