# -*- coding: utf-8 -*-
import scrapy


class Systembolaget1Spider(scrapy.Spider):
    name = 'systembolaget1'
    allowed_domains = ['systembolaget.com']
    start_urls = ['http://systembolaget.com/']

    def parse(self, response):
        pass
