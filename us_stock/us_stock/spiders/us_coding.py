# -*- coding: utf-8 -*-
import scrapy
# from us_stock.us_stock.items import UsStockItem

class UsCodingSpider(scrapy.Spider):
    name = 'us_coding'
    allowed_domains = ['xueqiu.com']
    start_urls = ['https://xueqiu.com/hq#exchange=US&firstName=%E7%BE%8E%E5%9B%BD%E8%82%A1%E5%B8%82&secondName=%E7%BE%8E%E8%82%A1%E4%B8%80%E8%A7%88&order=desc&orderby=volume']

    def parse(self, response):
        print(response.text)
