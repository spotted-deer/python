# -*- coding: utf-8 -*-
# 这个是爬取国内的新闻

import scrapy
from tutorial.items import TutorialItem

'''
 一开始我的news_parse的xpath匹配是这样的：
 也就是第二个xpath中p之前是/而不是//，这就体现了，/与//的区别了：
    原先看到的说明：
        //表示文档里的任何位置的节点
        /表示文档里根下的那些节点
    /是匹配到div[@class='article']的下一个，而不是全部子代（一层），所以它触及不到p的text，进而我爬取不到任何内容
    而//就不一样了，它是全部后代（多层），也就是<div id="div1"><div id="div2"><p>hello</p></div></div>,即使用xpath("//div[@id='div1']//p/text()").extract()
    结果是"hello" 而使用xpath("//div[@id='div1']/p/text()").extract()就什么也匹配不到
 myitem['article_title'] = response.xpath("//h1[@class='main-title']/text()").extract()
 myitem['article_content'] = response.xpath("//div[@class='article']/p/text()").extract()
 myitem['article_image'] = response.xpath("//div[@class='img_wrapper']/img/@src").extract_first()
 '''

class MyspiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'myspider'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['https://news.sina.com.cn/china//']

    def parse(self, response):
        # 这里要限制一下爬取的href的个数，因为后边的都不是当天的新闻
        href_list = []
        list = response.xpath("//div[@style='display:none;']//li/a/@href").extract()    # 获取href
        for i in range(0, 50, 1):   # 留下前50条数据
            href_list.append(list[i])
        for href in href_list:
            yield scrapy.Request(url=href, callback=self.news_parse)


    def news_parse(self, response):
        myitem = TutorialItem()
        myitem['article_title'] = response.xpath("//h1[@class='main-title']/text()").extract()
        myitem['article_content'] = response.xpath("//div[@class='article']//p/text()").extract()
        # 获取第一张图片，可能无图
        myitem['article_image'] = response.xpath("//div[@class='img_wrapper']//img/@src").extract_first()
        myitem['article_type'] = 'china'
        # 把自己的item抛出给pipeline
        yield myitem
