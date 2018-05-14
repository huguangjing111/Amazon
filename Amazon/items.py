# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # 产品类型
    title = scrapy.Field()
    # 商品页链接
    type_link = scrapy.Field()
    # 商品详情链接
    good_link = scrapy.Field()
    # 产品所属品牌
    logo = scrapy.Field()
    # 产品价格
    price = scrapy.Field()
    # 星级
    rank = scrapy.Field()
    # 图片链接
    img_url = scrapy.Field()
    # 商品类型
    type = scrapy.Field()
