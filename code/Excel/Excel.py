# !/usr/bin/env python2.7
# -*- coding=utf-8 -*-
from email.mime.application import MIMEApplication

import os
import xlwt
import datetime
import MySQLdb
import time
import smtplib
from email.mime.text import MIMEText
import email.MIMEMultipart
import mimetypes
import sys


def toExcel(title, schemes, data, date):
    col = len(data[0])

    row = len(data)

    wbk = xlwt.Workbook(encoding='utf-8')

    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体

    alignment = xlwt.Alignment()  # 对齐方式

    alignment.horz = xlwt.Alignment.HORZ_CENTER  # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED

    alignment.vert = xlwt.Alignment.VERT_CENTER  # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED

    # font.bold = True  # 黑体

    # font.underline = True  # 下划线

    style.font = font  # 设定样式

    style.alignment = alignment  # 设定样式

    # style.num_format_str = 'M/D/YY'  # 设置日期至单元格

    sheet = wbk.add_sheet('sheet 1')

    # sheet.write(0, 1, 'test text')  # 第0行第一列写入内容

    sheet.col(0).width = 256 * 9  # 设置单元格宽度

    sheet.col(1).width = 256 * 15  # 设置单元格宽度

    sheet.col(2).width = 256 * 12  # 设置单元格宽度

    # sheet.write(0, 2, 'test text', style)  # 第0行第一列写入内容

    sheet.write_merge(0, 0, 0, col, title, style)  # 合并单元格 起始行 影响行 起始列 影响列 写入内容

    for index in range(len(schemes)):
        sheet.write(1, index, schemes[index], style)

    newsCount = 0
    for index in range(len(data)):
        sheet.write(2 + index, 0, index + 1, style)
        newsCount += data[index][1]
        for zindex in range(col):
            sheet.write(2 + index, 1 + zindex, data[index][zindex], style)

    sheet.write(0, col + 1, "总计")
    sheet.write(0, col + 2, newsCount)

    # sheet.write(0, col + 2, xlwt.Formula('SUM(C3:C%d)' %(2+len(data))))

    wbk.save(date + title.decode("utf-8") + '.xls')


def Email(content, filename):
    # 第三方 SMTP 服务
    # mail_host = "smtp.exmail.qq.com"  # 设置服务器
    # mail_user = "rhxc@dongmibang.com"  # 用户名
    # mail_pass = "RHxc2017"  # 口令
    # ------------------ 以上是企业邮箱配置 -------------

    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "174691790@qq.com"  # 用户名
    mail_pass = "nvogqauloeulbicj"  # 口令

    # ------------------ 以上是个人邮箱配置 -------------
    _user = mail_user
    _pwd = mail_pass
    _to = ["lh1250lh@163.com", "279596719@qq.com"]

    msg = email.MIMEMultipart.MIMEMultipart()

    msg_text = MIMEText(content, 'html', 'utf-8')

    msg.attach(msg_text)

    msg["Subject"] = "正式爬虫昨日入库新闻统计"
    msg["From"] = _user

    data = open(filename, 'rb')
    ctype, encoding = mimetypes.guess_type(filename)
    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
    file_msg.set_payload(data.read())
    data.close()
    email.Encoders.encode_base64(file_msg)

    basename = os.path.basename(filename)
    file_msg.add_header('Content-Disposition', 'attachment', filename=basename)  # 修改邮件头
    msg.attach(file_msg)

    try:
        for to_add in _to:
            s = smtplib.SMTP_SSL(mail_host, 465)
            s.login(_user, _pwd)
            msg["To"] = to_add
            s.sendmail(_user, to_add, msg.as_string())
            s.quit()
        print "发送成功"
    except s.smtplib.SMTPException, e:
        print "发送失败"


timestr = time.strftime('%Y-%m-%d', time.localtime(time.time()))

db = MySQLdb.connect("localhost", "crawler", "Crawler#54321", "public_opinion", charset="utf8")
# db = MySQLdb.connect("localhost", "root", "", "yq_test", charset="utf8")

cursor = db.cursor()

cursor.execute(
    "select site ,count(*) as newsCount from li_public_opinion_simple WHERE create_time > '%s 00:00:00' GROUP BY site ORDER BY newsCount DESC " % timestr)

data = cursor.fetchall()

cursor.close()
if len(data) > 0:
    toExcel("NewsCounts", ['排名', '网站标题', '新闻总条数'], data, sys.path[0]+"/"+timestr)
else:
    toExcel("NewsCounts", ['排名', '网站标题', '新闻总条数'], (('mysql get data is null', 0),), sys.path[0]+"/"+timestr)

Email(timestr + " 入库新闻数据统计",sys.path[0]+"/"+timestr + "NewsCounts.xls")
