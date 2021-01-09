# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
from skalscrapingnew.items import Product,StoreDetails
from skalscrapingnew.spiders.systembolaget1 import Systembolaget1Spider
from skalscrapingnew.spiders.systembolagetstore import SystembolagetstoreSpider
import pymongo
import scrapy.exceptions
from scrapy.pipelines.images import ImagesPipeline

class SkalscrapingnewPipeline:
    SCRAPPING_STORES = 'scrapping_stores'
    SCRAPPED_PRODCUTS = 'scrapped_products'
    SCRAPPED_STORES = 'scrapped_stores'
    ID_FOR_STORES_MONGO = 1
    def open_spider(self,spider):
        self.client = pymongo.MongoClient("mongodb://hello:hello@127.0.0.1:27017/?authSource=admin&authMechanism=SCRAM-SHA-256")
        self.db = self.client['systembolaget']
        if spider.name in ['systembolaget1']:
            # Deleting the Store Products collection
            self.db[self.SCRAPPED_PRODCUTS].drop()
            # Getting the Stores to be scrapped
            stores = self.db[self.SCRAPPING_STORES].find_one({"_id": self.ID_FOR_STORES_MONGO})
            Systembolaget1Spider.stores = stores['stores']
            if len(Systembolaget1Spider.stores) == 0:
                raise scrapy.exceptions.CloseSpider('No Store Found To Scrap') 

        if spider.name in ['systembolagetstore']:
            # Deleting the Store Details collection
            self.db[self.SCRAPPED_STORES].drop()
            # Getting the Stores to be scrapped
            stores = self.db[self.SCRAPPING_STORES].find_one({"_id": self.ID_FOR_STORES_MONGO})
            SystembolagetstoreSpider.stores = stores['stores']
            if len(SystembolagetstoreSpider.stores) == 0:
                raise scrapy.exceptions.CloseSpider('No Store Found To Scrap')

    def process_item(self, item, spider):
        if isinstance(item,Product):
            self.db[self.SCRAPPED_PRODCUTS].insert(item)
        if isinstance(item,StoreDetails):
            self.db[self.SCRAPPED_STORES].insert(item)
        return item


class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if isinstance(item,Product):
            try:
                for image_url in item['imageUrls']:
                    logging.error(image_url)
                    yield scrapy.Request(image_url)
            except ValueError:
                logging.info("Exception of Value Error happened in Image pipeline")
            except KeyError:
                logging.info("Exception of Key Error happened in Image pipeline")

    def item_completed(self, results, item, info):
        if isinstance(item,Product):
            image_paths = [x['path'] for ok, x in results if ok]
            item['image_paths'] = image_paths
        return item
