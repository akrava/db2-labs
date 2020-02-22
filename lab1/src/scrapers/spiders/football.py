# -*- coding: utf-8 -*-
from scrapy.http.response import Response
import scrapy


class FootballSpider(scrapy.Spider):
    name = 'football'
    allowed_domains = ['football.ua']
    start_urls = ['https://football.ua/']

    def parse(self, response: Response):
        all_images = response.xpath("//img/@src")
        all_text = response.xpath("//p/text()")
        yield {
            'url': response.url,
            'payload': [{'type': 'text', 'data': text.get()} for text in all_text] +
                       [{'type': 'image', 'data': image.get()} for image in all_images]
        }
        if response.url == self.start_urls[0]:
            all_links = response.xpath(
                "//a/@href[starts-with(., '%s')][substring(., string-length() - 4) = '.html']" % self.start_urls[0])
            filtered_links = [link.get() for link in all_links][:19]
            for link in filtered_links:
                yield scrapy.Request(link, self.parse)
