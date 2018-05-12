# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter


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

    def process_item(self, item, spider):
        # 每次写入一个item数据
        self.csv_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        # 结束csv文件读写
        self.csv_exporter.finish_exporting()
        # 关闭文件
        self.f.close()
