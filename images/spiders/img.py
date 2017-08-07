# -*- coding: utf-8 -*-
import scrapy
import json
from images.items import ImagesItem
class ImgSpider(scrapy.Spider):
    name = 'img'
    allowed_domains = ['cpai.douyucdn.cn']

    offset = 0
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    start_urls = [url + str(offset)]

    def parse(self, response):
        data = json.loads(response.body)['data']
        for each in data:
            item = ImagesItem()
            item['image_url'] = each['vertical_src']
            yield item

        if self.offset < 200:
            self.offset += 20
        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)