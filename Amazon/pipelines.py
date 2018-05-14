# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import pymongo
import scrapy
from scrapy.exporters import CsvItemExporter
from scrapy.pipelines.images import ImagesPipeline

from Amazon.settings import IMAGES_STORE


class AmazonPipeline(object):
    def process_item(self, item, spider):
        return item

class AmazonCsvPipeline(object):
    def open_spider(self, spider):
        # 保存csv数据的文件对象
        self.f = open("Amazon_goods_crawl.csv", "w")
        # 创建csv文件读写对象
        self.csv_exporter = CsvItemExporter(self.f)
        # 开始进行csv文件读写
        self.csv_exporter.start_exporting()
        # 根据商品标题进行去重处理
        self.add_title = set()

    def process_item(self, item, spider):
        if item['title'] in self.add_title:
            print u'[EEROR] 数据已保存，勿重复%s'% item['title']
        else:
            self.add_title.add(item['title'])
            # 每次写入一个item数据
            # print u'[INFO] 正在写入csv文件中%s'% item['title']
            self.csv_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        # 结束csv文件读写
        # print u'[INFO] 写入csv文件已完成'
        self.csv_exporter.finish_exporting()
        # 关闭文件
        self.f.close()

class AmazonImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img_url'])

    def item_completed(self, results, item, info):
        # 原来的保存路径
        path_old = IMAGES_STORE + [x['path'] for ok,x in results][0]
        # 更新保存路径并以字段名字更名，去掉空格，/和
        name = item['title'].replace('/','').replace('-','').replace(' ','').replace(',','')
        # 现在要保存的路径
        path_now = IMAGES_STORE + 'images/' +name + path_old[-4:]
        try:
            os.rename(
                path_old,
                path_now
            )
        except Exception as e:
            print e
            print u'[ERROR] 更名失败获取数据已经保存，勿重复保存: %s'% item['title']

        return item

class AmazonMongoDBPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='127.0.0.1',port=27017)
        self.db = self.client['Amazon']
        self.collection = self.db['amazon']
        # 根据商品标题进行去重处理
        self.add_title = set()

    def process_item(self, item, spider):
        if item['title'] in self.add_title:
            print u'[ERROR] 数据已保存，勿重复:  %s'% item['title']
        else:
            self.add_title.add(item['title'])
            print u'[INFO] 正在存储到数据中%s' % item['title']
            self.collection.insert(dict(item))
        return item





