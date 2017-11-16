# -*- coding: utf-8 -*-
import hashlib
import time

import pymysql


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NewsspiderPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", user="root", passwd="superdream", db="news_spider")

    def process_item(self, item, spider):
        title = item['title'][0]
        keywords = item['keywords'][0]
        content = item['content']
        content = str(content).replace('\\n','')
        link = item['link']
        source = item['source']
        author = ''
        if len(item['author']) > 0:
            author = item['author'][0]
        publish_time_str = item['publish_time'][0]
        publish_time_str = str(publish_time_str)[:-6].replace('T', ' ')
        publish_time = time.strptime(publish_time_str, "%Y-%m-%d %H:%M:%S")
        publish_time = time.mktime(publish_time)
        m = hashlib.sha1()
        m.update(str(link).encode('utf8'))
        article_id = m.hexdigest()
        sql = 'INSERT INTO article (article_id,title,keywords,content,link,source,author,publish_time) VALUES ("' + str(article_id) + '","' + str(title) + '","' + str(keywords) + '","' + str(content) + '","' + str(link) + '","' + str(source) + '","' + str(author) + '","' + str(publish_time) + '")'
        flag = self.conn.query(sql)
        self.conn.commit()
        if flag == 1:
            print('文章---' + title + '保存成功！')
            print(str(article_id) + '-----' + str(publish_time))
        else:
            print('文章---' + title + '保存失败！')
        return item

    def close_spider(self, spider):
        self.conn.close()
