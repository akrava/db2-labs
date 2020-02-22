# -*- coding: utf-8 -*-
from scrapy.http.response import Response
import scrapy


class MoyoSpider(scrapy.Spider):
    name = 'moyo'
    allowed_domains = ['www.moyo.ua']
    start_urls = ['https://www.moyo.ua/telecommunication/smart/']

    def parse(self, response: Response):
        products = response.xpath("//section[contains(@class, 'product-tile_product')]")[:20]
        for product in products:
            yield {
                'description': product.xpath("./@data-name").get(),
                'price': product.xpath("./@data-price").get(),
                'img': product.xpath("./@data-img").get()
            }
