import scrapy
import sys
from rns.items import FortuneItem


class FortuneSpider(scrapy.Spider):
    name = 'fortune'
    allowed_domains = ['fortune.com']
    start_urls = ['https://fortune.com/']

    def parse(self, response):
        for col in response.xpath('/html/body/div/div/main/div/div/div/div/ul/li'):
            item = FortuneItem()
            # item['category']
            print(col.xpath('div/a').data)
            #print(col.xpath('/div/a/div/text()')) # 제목
