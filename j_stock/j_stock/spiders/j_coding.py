# -*- coding: utf-8 -*-
import scrapy
from j_stock.items import JStockItem
# 表格化数据的解析  应该遍历整个大表格！
class JCodingSpider(scrapy.Spider):
    name = 'j_coding'
    allowed_domains = ['info.finance.yahoo.co.jp']
    start_urls = ['https://info.finance.yahoo.co.jp/ranking/?kd=53&tm=d&vl=a&mk=1&p=1']

    def parse(self, response):
        big_table = response.xpath("//table[@class='rankingTable']/tbody/tr")  #注意表格没有text(),也没有extract()
        for sel in big_table:
            j_item = JStockItem()
            j_item['rank'] = sel.xpath("./td[1]/text()").extract_first()
            j_item['coding'] = sel.xpath("./td[2]/a/text()").extract_first()
            j_item['market'] = sel.xpath("./td[3]/text()").extract_first()
            j_item['name'] = sel.xpath("./td[4]/text()").extract_first()

            yield j_item

        next_page = response.xpath("//ul/a[last()]/@href").extract_first()

        if next_page is not None:

            yield scrapy.Request(next_page,callback=self.parse)






