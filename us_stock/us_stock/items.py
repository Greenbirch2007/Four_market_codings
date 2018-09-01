# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UsStockItem(scrapy.Item):
    coding = scrapy.Field()
    name = scrapy.Field()
    new_price = scrapy.Field()
    value = scrapy.Field()

