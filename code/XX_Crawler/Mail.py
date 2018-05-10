# !/usr/bin/env python2.7
# -*- coding=utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import sys
from email.header import Header

# 第三方 SMTP 服务

# mail_host = "smtp.exmail.qq.com"  # 设置服务器
# mail_user = "rhxc@dongmibang.com"  # 用户名
# mail_pass = "RHxc2017"  # 口令

# ------------------ 以上是企业邮箱配置 -------------

mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "174691790@qq.com"  # 用户名
mail_pass = "nvogqauloeulbicj"  # 口令

_user = mail_user
_pwd = mail_pass
_to = ["lh1250lh@163.com"]

content = """
<table>
<tr>
<th>网站</th>
<th>频道</th>
<th>错误类型</th>
<th>错误条数</th>
</tr>
%s
</table>"""


def send_mail(title, con):
    msg = MIMEText(content % con, 'html', 'utf-8')
    msg["Subject"] = title
    msg["From"] = _user

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
