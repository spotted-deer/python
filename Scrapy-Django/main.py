import time     #time没用到，其实可以定义一个循环时间每24小时执行一次爬取操作
import os
# 三个爬虫在一个命令下执行，但他们不是多线程执行

os.system("scrapy crawl myspider")
os.system("scrapy crawl international")
os.system("scrapy crawl science")
