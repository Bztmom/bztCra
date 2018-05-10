#!/bin/sh

pipelines_cnt=`ps aux|grep run_pipelines|wc -l`
if [ $pipelines_cnt -lt 2 ]; then
    cd /home/zhangxiang/Crawler/code
    python -u run_pipelines.py > ../log/pipelines.`date +"%Y-%m-%d %H:%M"`.log
    python -u parse_news_log.py > ../log/task_log.`date +"%Y-%m-%d %H:%M"`.log
else
    echo "last task is not finished" > ../log/pipelines.`date +"%Y-%m-%d %H:%M"`.log

fi
