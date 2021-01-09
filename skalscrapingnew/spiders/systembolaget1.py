# -*- coding: utf-8 -*-
import logging

from scrapy import item
from skalscrapingnew.items import Product
import scrapy
import json
import datetime
from scrapy.http import headers
from urllib.parse import parse_qs, urlparse


class Systembolaget1Spider(scrapy.Spider):
    name = 'systembolaget1'
    stores = []
    headers= {"authority":"api-extern.systembolaget.se",
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

    def start_requests(self):
        for store in self.stores:
            yield scrapy.Request(
                url=f'https://api-extern.systembolaget.se/sb-api-ecommerce/v1/productsearch/search?size=30&page=1&isEcoFriendlyPackage=false&isInDepotStockForFastDelivery=false&storeId={store}&isInStoreAssortmentSearch=true',
                headers=self.headers,
                callback=self.parse
            )

    def parse(self, response):
        json_resp = json.loads(response.body)
        products = json_resp.get('products')
        store = parse_qs(urlparse(str(response.request.url)).query)['storeId'][0]
        now = datetime.datetime.now()
        for product in products:
            Item = Product()
            Item['productId'] = product.get('productId')
            productId = product.get('productId')
            Item['productNumber'] = product.get('productNumber')
            Item['productNameBold'] = product.get('productNameBold')
            Item['productNameThin'] = product.get('productNameThin')
            Item['category'] = product.get('category')
            Item['productNumberShort'] = product.get('productNumberShort')
            Item['producerName'] = product.get('producerName')
            Item['supplierName'] = product.get('supplierName')
            Item['isKosher'] = product.get('isKosher')
            Item['bottleTextShort'] = product.get('bottleTextShort')
            Item['restrictedParcelQuantity'] = product.get('restrictedParcelQuantity')
            Item['isOrganic'] = product.get('isOrganic')
            Item['isEthical'] = product.get('isEthical')
            Item['ethicalLabel'] = product.get('ethicalLabel')
            Item['isWebLaunch'] = product.get('isWebLaunch')
            Item['productLaunchDate'] = product.get('productLaunchDate')
            Item['isCompletelyOutOfStock'] = product.get('isCompletelyOutOfStock')
            Item['isTemporaryOutOfStock'] = product.get('isTemporaryOutOfStock')
            Item['alcoholPercentage'] = product.get('alcoholPercentage')
            Item['volumeText'] = product.get('volumeText')
            Item['volume'] = product.get('volume')
            Item['price'] = product.get('price')
            Item['country'] = product.get('country')
            Item['originLevel1'] = product.get('originLevel1')
            Item['originLevel2'] = product.get('originLevel2')
            Item['categoryLevel1'] = product.get('categoryLevel1')
            Item['categoryLevel2'] = product.get('categoryLevel2')
            Item['categoryLevel3'] = product.get('categoryLevel3')
            Item['categoryLevel4'] = product.get('categoryLevel4')
            Item['customCategoryTitle'] = product.get('customCategoryTitle')
            Item['assortmentText'] = product.get('assortmentText')
            Item['usage'] = product.get('usage')
            Item['taste'] = product.get('taste')
            Item['tasteSymbols'] = product.get('tasteSymbols')
            Item['tasteClockGroupBitter'] = product.get('tasteClockGroupBitter')
            Item['tasteClockGroupSmokiness'] = product.get('tasteClockGroupSmokiness')
            Item['tasteClockBitter'] = product.get('tasteClockBitter')
            Item['tasteClockFruitacid'] = product.get('tasteClockFruitacid')
            Item['tasteClockBody'] = product.get('tasteClockBody')
            Item['tasteClockRoughness'] = product.get('tasteClockRoughness')
            Item['tasteClockSweetness'] = product.get('tasteClockSweetness')
            Item['tasteClockSmokiness'] = product.get('tasteClockSmokiness')
            Item['tasteClockCasque'] = product.get('tasteClockCasque')
            Item['assortment'] = product.get('assortment')
            Item['recycleFee'] = product.get('recycleFee')
            Item['isManufacturingCountry'] = product.get('isManufacturingCountry')
            Item['isRegionalRestricted'] = product.get('isRegionalRestricted')
            Item['packaging'] = product.get('packaging')
            Item['isNews'] = product.get('isNews')
            try:
                Item['imageUrls'] = [product.get('images')[0]['imageUrl']+'_400.png']
            except:
                Item['imageUrls'] = None
            Item['isDiscontinued'] = product.get('isDiscontinued')
            Item['isSupplierTemporaryNotAvailable'] = product.get('isSupplierTemporaryNotAvailable')
            Item['sugarContent'] = product.get('sugarContent')
            Item['seal'] = product.get('seal')
            Item['vintage'] = product.get('vintage')
            Item['grapes'] = product.get('grapes')
            Item['otherSelections'] = product.get('otherSelections')
            Item['color'] = product.get('color')
            Item['scrappedDate'] = now.strftime("%Y-%m-%d %H:%M:%S")
            Item['storeId'] = store
            # yield Item
            yield scrapy.Request(url=f'https://api-extern.systembolaget.se/sb-api-ecommerce/v1/stockbalance/store?ProductId={productId}&StoreId={store}',
            headers=self.headers,
            callback=self.stock_details,
            meta={'item': Item}
            )
        next_page = json_resp.get('metadata').get('nextPage')
        # logging.info("Next Page"+str(next_page))
        if next_page != -1:
            yield scrapy.Request(
                url=f'https://api-extern.systembolaget.se/sb-api-ecommerce/v1/productsearch/search?size=30&page={next_page}&isEcoFriendlyPackage=false&isInDepotStockForFastDelivery=false&storeId={store}&isInStoreAssortmentSearch=true',
                headers=self.headers,
                callback=self.parse
            )
    def stock_details(self, response):
        Item = response.meta['item']
        try:
            json_resp = json.loads(response.body)[0]
            # logging.error(json_resp)
            Item['shelf'] = json_resp.get('shelf')
            Item['stock'] = json_resp.get('stock')
            yield Item
        except:
            yield Item
