# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem

# 这个是爬取科技类新闻

class ScienceSpider(scrapy.Spider):
    name = 'science'
    allowed_domains = ['tech.sina.com.cn']
    start_urls = ['https://tech.sina.com.cn//']

    def parse(self, response):
        href_list = []
        list = response.xpath("//ul[@class='seo_data_list']/li/a/@href").extract()
        for i in range(0, 50, 1):   #要前50条新闻，太多的话，新闻会不是当天的
            href_list.append(list[i])
        for href in href_list:
            yield scrapy.Request(url=href, callback=self.news_parse)

    def news_parse(self, response):
        myitem = TutorialItem()
        myitem['article_title'] = response.xpath("//h1[contains(@class,'main-title') or contains(@id,'artibodyTitle')]/text()").extract()
        myitem['article_content'] = response.xpath("//div[@id='artibody']//p/text()").extract()
        # 这个爬取中将特殊编码进行了替换，不过这应该还没有进行编码，所以这段代码不是放到这个地方
        #for elem in temp_dict:
        #    elem.replace(u'\xa0', u' ')
        #    elem.replace(u'\u3000', u' ')
        # 获取第一张图片，可能无图
        myitem['article_image'] = response.xpath("//div[@class='img_wrapper']//img/@src").extract_first()
        myitem['article_type'] = 'science'
        # 把自己的item抛出给pipeline
        yield myitem


