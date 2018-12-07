# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import json
# 主要是连接数据库并写入
import sqlite3
import datetime


class TutorialPipeline(object):
    #def __init__(self, sqlite_file, sqlite_table):
    #    # self.filename = open("myspider.json", "ab")    #打开json文件并写入
    #    self.sqlite_file = sqlite_file
    #    self.sqlite_table = sqlite_table

    #def from_crawler(cls, crawler):
    #    return cls(
    #        sqlite_file=crawler.settings.get('SQLITE_FILE'),  # 从 settings.py 提取
    #        sqlite_table=crawler.settings.get('SQLITE_TABLE', 'items')  # 从settings拿出来的表的名字命名为items
    #    )

    def open_spider(self, spider):
        self.conn = sqlite3.connect('..\mysite\db.sqlite3')   # 连接到数据库文件
        self.cur = self.conn.cursor()       # 游标

    def process_item(self, item, spider):
        # sql操作
        insert_sql = 'insert into play_news (title,article_content,created_time,last_modified_time,article_image,category,status) values ("{}","{}","{}","{}","{}","{}","{}")'.format(item['article_title'], item['article_content'], datetime.datetime.now(), datetime.datetime.now(), item['article_image'], item['article_type'], 'd')
        # 后面format的 item[]里面的内容跟自己的items.py中的值名字一样
        self.cur.execute(insert_sql)
        self.conn.commit()      # 一定不要忘了提交
            #这是以前的将数据转化为json存入文件
            #text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
            #self.filename.write(text.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.conn.close()
        #self.filename.close()
