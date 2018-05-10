#!/bin/bash

dir="/home/zhangxiang/news_crawler/backup/"

find $dir -mtime +7 -name "news.*" | xargs rm -f

sleep 5

find $dir -mtime +7 -name "log_info.*" | xargs rm -f
