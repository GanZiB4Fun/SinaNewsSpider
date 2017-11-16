# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    article_id = scrapy.Field()
    title = scrapy.Field()
    keywords = scrapy.Field()
    content = scrapy.Field()
    link = scrapy.Field()
    source = scrapy.Field()
    author = scrapy.Field()
    publish_time = scrapy.Field()
