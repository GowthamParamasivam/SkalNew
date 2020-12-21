# -*- coding: utf-8 -*-
from skalscrapingnew.items import StoreDetails
import scrapy
import json


class SystembolagetstoreSpider(scrapy.Spider):
    name = 'systembolagetstore'
    headers= {  "authority":"api-extern.systembolaget.se",
                "pragma":"no-cache",
                "cache-control":"no-cache",
                "sec-ch-ua":"\"Chromium\";v=\"86\", \"\"Not\A;Brand\";v=\"99\", \"Google Chrome\";v=\"86\"",
                "accept":"application/json, text/plain, */*",
                "sec-ch-ua-mobile":"?0",
                "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                "ocp-apim-subscription-key":"874f1ddde97d43f79d8a1b161a77ad31",
                "origin":"https://www.systembolaget.se",
                "sec-fetch-site":"same-site",
                "sec-fetch-mode":"cors",
                "sec-fetch-dest":"empty",
                "referer":"https://www.systembolaget.se/"}
    stores = []


    def start_requests(self):
        for store in self.stores:
            yield scrapy.Request(
                url=f'https://api-extern.systembolaget.se/sb-api-ecommerce/v1/site/store/{store}',
                headers=self.headers,
                callback=self.parse
            )

    def parse(self, response):
        json_resp = json.loads(response.body)
        Item = StoreDetails() 
        Item['siteId'] = json_resp.get('siteId')
        Item['depotStockId'] = json_resp.get('depotStockId')
        Item['alias'] = json_resp.get('alias')
        Item['isDepot'] = json_resp.get('isDepot')
        Item['isStore'] = json_resp.get('isStore')
        Item['isActive'] = json_resp.get('isActive')
        Item['isBlocked'] = json_resp.get('isBlocked')
        Item['isOpen'] = json_resp.get('isOpen')
        Item['isFullAssortmentOrderStore'] = json_resp.get('isFullAssortmentOrderStore')
        Item['isTastingStore'] = json_resp.get('isTastingStore')
        Item['address'] = json_resp.get('address')
        Item['postalCode'] = json_resp.get('postalCode')
        Item['city'] = json_resp.get('city')
        Item['phone'] = json_resp.get('phone')
        Item['county'] = json_resp.get('county')
        Item['openingHours'] = json_resp.get('openingHours')
        Item['parentSiteId'] = json_resp.get('parentSiteId')
        Item['searchArea'] = json_resp.get('searchArea')
        Item['position'] = json_resp.get('position')
        Item['deliveryTimeDays'] = json_resp.get('deliveryTimeDays')
        yield Item
