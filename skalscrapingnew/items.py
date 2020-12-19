# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SkalscrapingnewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Product(scrapy.Item):
    _id = scrapy.Field()
    productId = scrapy.Field()
    productNumber = scrapy.Field()
    productNameBold = scrapy.Field()
    productNameThin = scrapy.Field()
    category = scrapy.Field()
    productNumberShort = scrapy.Field()
    producerName = scrapy.Field()
    supplierName = scrapy.Field()
    isKosher = scrapy.Field()
    bottleTextShort = scrapy.Field()
    restrictedParcelQuantity = scrapy.Field()
    isOrganic = scrapy.Field()
    isEthical = scrapy.Field()
    ethicalLabel = scrapy.Field()
    isWebLaunch = scrapy.Field()
    productLaunchDate = scrapy.Field()
    isCompletelyOutOfStock = scrapy.Field()
    isTemporaryOutOfStock = scrapy.Field()
    alcoholPercentage = scrapy.Field()
    volumeText = scrapy.Field()
    volume = scrapy.Field()
    price = scrapy.Field()
    country = scrapy.Field()
    originLevel1 = scrapy.Field()
    originLevel2 = scrapy.Field()
    categoryLevel1 = scrapy.Field()
    categoryLevel2 = scrapy.Field()
    categoryLevel3 = scrapy.Field()
    categoryLevel4 = scrapy.Field()
    customCategoryTitle = scrapy.Field()
    assortmentText = scrapy.Field()
    usage = scrapy.Field()
    taste = scrapy.Field()
    tasteSymbols = scrapy.Field()
    tasteClockGroupBitter = scrapy.Field()
    tasteClockGroupSmokiness = scrapy.Field()
    tasteClockBitter = scrapy.Field()
    tasteClockFruitacid = scrapy.Field()
    tasteClockBody = scrapy.Field()
    tasteClockRoughness = scrapy.Field()
    tasteClockSweetness = scrapy.Field()
    tasteClockSmokiness = scrapy.Field()
    tasteClockCasque = scrapy.Field()
    assortment = scrapy.Field()
    recycleFee = scrapy.Field()
    isManufacturingCountry = scrapy.Field()
    isRegionalRestricted = scrapy.Field()
    packaging = scrapy.Field()
    isNews = scrapy.Field()
    imageUrls = scrapy.Field()
    images = scrapy.Field()
    image_paths = scrapy.Field()
    isDiscontinued = scrapy.Field()
    isSupplierTemporaryNotAvailable = scrapy.Field()
    sugarContent = scrapy.Field()
    seal = scrapy.Field()
    vintage = scrapy.Field()
    grapes = scrapy.Field()
    otherSelections = scrapy.Field()
    color = scrapy.Field()
    scrappedDate = scrapy.Field()
    storeId = scrapy.Field()
    shelf = scrapy.Field()
    stock = scrapy.Field()
