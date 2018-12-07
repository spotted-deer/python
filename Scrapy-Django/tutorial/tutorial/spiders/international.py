# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem

# 这个是爬取的国际新闻

class InternationalSpider(scrapy.Spider):
    name = 'international'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['https://news.sina.com.cn/world//']

    def parse(self, response):

        list = response.xpath("//div[@id='subShowContent1_static']//div[@class='news-item  img-news-item']/h2/a/@href").extract()  # 获取剩下的href
        list.append(response.xpath("//div[@id='subShowContent1_static']//div[@class='news-item first-news-item img-news-item']/h2/a/@href").extract())  # 获取第一个href
        for href in list:
            yield scrapy.Request(url=href, callback=self.news_parse)

    def news_parse(self, response):
        myitem = TutorialItem()
        myitem['article_title'] = response.xpath("//h1[@class='main-title']/text()").extract()
        myitem['article_content'] = response.xpath("//div[@class='article']//p/text()").extract()
        # 获取第一张图片，可能无图
        myitem['article_image'] = response.xpath("//div[@class='img_wrapper']//img/@src").extract_first()
        myitem['article_type'] = 'international'
        # 把自己的item抛出给pipeline
        yield myitem
