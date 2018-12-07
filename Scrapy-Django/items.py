# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# 定义自己的爬取数据的容器

import scrapy


class TutorialItem(scrapy.Item):
    article_title = scrapy.Field()
    article_content = scrapy.Field()
    article_image = scrapy.Field()
    article_type = scrapy.Field()
    pass



