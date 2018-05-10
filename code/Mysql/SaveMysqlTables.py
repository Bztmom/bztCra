# -*- coding: utf-8 -*-

# save mysql tables name `li_public_option_simple` to name + time

import MySQLdb
import time

timestr = time.strftime('%Y-%m-%d', time.localtime(time.time()))

db = MySQLdb.connect("localhost", "crawler", "Crawler#54321", "public_opinion")

cursor = db.cursor()

cursor.execute("SHOW TABLE STATUS")

data = cursor.fetchall()
for tables in data:
    if tables[0] == "li_public_opinion_simple":
        id = tables[10]
cursor.execute("ALTER  TABLE `li_public_opinion_simple` RENAME TO `li_public_opinion_simple_%s`" % timestr)
sql = """
CREATE TABLE IF NOT EXISTS `li_public_opinion_simple` (
  `yid` int(11) unsigned NOT NULL,
  `url` varchar(255) COLLATE utf8_unicode_ci NOT NULL DEFAULT '' COMMENT '原文地址',
  `author` varchar(255) COLLATE utf8_unicode_ci NOT NULL DEFAULT '' COMMENT '作者',
  `from` varchar(255) COLLATE utf8_unicode_ci DEFAULT '' COMMENT '转载源 [新闻、视频]',
  `domain` varchar(255) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0' COMMENT '域名',
  `view` int(11) DEFAULT '0' COMMENT '点击数 [新闻、论坛、博客、视频]',
  `comment` int(11) DEFAULT '0' COMMENT '评论数 [新闻、论坛、博客、视频]',
  `isnegative` tinyint(4) NOT NULL DEFAULT '0' COMMENT '负面：0 否 1是',
  `isneutral` tinyint(4) NOT NULL DEFAULT '0' COMMENT '中性：0 否 1是',
  `ispositive` tinyint(4) NOT NULL DEFAULT '0' COMMENT '正面：0 否 1是',
  `hot` int(11) DEFAULT '0' COMMENT '文章热度',
  `title` varchar(255) COLLATE utf8_unicode_ci NOT NULL DEFAULT '' COMMENT '原文标题',
  `keywords` varchar(5000) COLLATE utf8_unicode_ci NOT NULL DEFAULT '' COMMENT '关键字',
  `summary` text COLLATE utf8_unicode_ci NOT NULL COMMENT '摘要',
  `content` mediumtext COLLATE utf8_unicode_ci NOT NULL COMMENT '内容',
  `iszd` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否置顶，0 否 1 是',
  `isdel` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否删除，0 否 1 是',
  `site` varchar(50) COLLATE utf8_unicode_ci NOT NULL COMMENT '网站名称',
  `channel` varchar(50) COLLATE utf8_unicode_ci NOT NULL COMMENT '频道',
  `publish_time` timestamp NULL DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB AUTO_INCREMENT=%s DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='舆情小表';
""" % id
cursor.execute(sql)

cursor.execute(
    "ALTER TABLE `li_public_opinion_simple`  ADD PRIMARY KEY (`yid`), ADD KEY `site_channel` (`site`,`channel`) USING HASH")

cursor.execute(
    "ALTER TABLE `li_public_opinion_simple`  MODIFY `yid` int(11) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=%s" % id)

db.close()
