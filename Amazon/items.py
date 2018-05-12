# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    index = scrapy.Field()
    type_link = scrapy.Field()
    good_link = scrapy.Field()
    logo = scrapy.Field()
    price = scrapy.Field()
    rank = scrapy.Field()
