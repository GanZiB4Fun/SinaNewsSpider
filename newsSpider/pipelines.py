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
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        title = str(item['title'][0])
        keywords = str(item['keywords'][0])
        content = item['content']
        content = str(content).replace('\n', '')
        link = str(item['link'])
        source = str(item['source'])
        author = ''
        if len(item['author']) > 0:
            author = str(item['author'][0])
        publish_time_str = item['publish_time'][0]
        publish_time_str = str(publish_time_str)[:-6].replace('T', ' ')
        publish_time = time.strptime(publish_time_str, "%Y-%m-%d %H:%M:%S")
        publish_time = str(time.mktime(publish_time))
        m = hashlib.sha1()
        m.update(str(link).encode('utf8'))
        article_id = str(m.hexdigest())
        flag = self.cursor.execute(
            'INSERT INTO article (article_id,title,keywords,content,link,source,author,publish_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
            (article_id, title, keywords, content, link, source, author, publish_time))
        self.conn.commit()
        if flag == 1:
            print('文章---' + title + '保存成功！')
            print(str(article_id) + '-----' + str(publish_time))
        else:
            print('文章---' + title + '保存失败！')
        return item

    def close_spider(self, spider):
        self.conn.close()
