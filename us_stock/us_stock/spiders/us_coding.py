# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from us_stock.items import UsStockItem


class UsCodingSpider(scrapy.Spider):
    name = 'us_coding'
    allowed_domains = ['xueqiu.com']
    start_urls = ['https://xueqiu.com/hq#exchange=US&firstName=3&secondName=3_0']



    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        for sel in response.xpath("//div[@id='stockList']/div/table/tbody"):
            us_item = UsStockItem()
            us_item['coding'] = sel.xpath("./tr/td[1]/a/text()").extract_first()
            us_item['name'] = sel.xpath("./tr/td[2]/a/text()").extract_first()
            us_item['new_price'] = sel.xpath("./tr/td[3]/span/text()").extract_first()
            us_item['value'] = sel.xpath("./tr/td[8]/span/text()").extract_first()
            yield us_item

        href = response.xpath("//li[@class='next']/a/@href").extract_first()

        if href is not None:
            url = response.urljoin(href)

            yield SplashRequest(url,cargs={'images':0,'timeout':3})