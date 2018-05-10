#!/bin/sh

pipelines_cnt=`ps aux|grep run_pipelines|wc -l`
if [ $pipelines_cnt -lt 2 ]; then
    python ./SaveMysqlTables.py
else
    echo "error"
    #todo get a sms to admin
fi
