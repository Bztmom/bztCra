#!/bin/sh

#####
#
#This shell would pack news in data directory to backup
#
#####
cd /home/zhangxiang/Crawler/code
tar czf ../backup/news.`date +"%Y-%m-%d"`.tar.gz ../data/* --remove-files
tar czf ../backup/news.log.`date +"%Y-%m-%d"`.tar.gz ../log/* --remove-files
tar czf ../backup/log_info.`date +"%Y-%m-%d"`.tar.gz ../task_info/* --remove-files
echo "packing done"
