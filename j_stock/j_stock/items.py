# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JStockItem(scrapy.Item):
    rank = scrapy.Field()
    coding = scrapy.Field()
    market = scrapy.Field()
    name = scrapy.Field()
