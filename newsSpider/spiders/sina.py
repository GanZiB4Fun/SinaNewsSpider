# -*- coding: utf-8 -*-

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from newsSpider.items import NewsspiderItem


class SinaSpider(CrawlSpider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn']

    rules = (
        Rule(LinkExtractor(allow=('.*?/[0-9]{4}.[0-9]{2}.[0-9]{2}.doc-.*?shtml')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = NewsspiderItem()
        i['title'] = response.xpath("/html/head/meta[@property='og:title']/@content").extract()
        i['keywords'] = response.xpath("/html/head/meta[@name='keywords']/@content").extract()
        content = response.xpath("//div[@id='artibody']").extract()
        i['content'] = str(content[0])
        i['link'] = response.url
        i['source'] = 'sina.com.cn'
        i['author'] = response.xpath("//p[@class='article-editor']/text()").extract()
        i['publish_time'] = response.xpath("//meta[@property='article:published_time']/@content").extract()
        return i
