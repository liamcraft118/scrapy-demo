# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StardewValleyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CollectionsItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()

class CollectionDetailItem(scrapy.Item):
    name = scrapy.Field()
    growth_time = scrapy.Field()

class VilltagerItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    icon_link = scrapy.Field()

class VilltagerCollectionItem(scrapy.Item):
    villager_name = scrapy.Field()
    collection_name = scrapy.Field()
    reaction = scrapy.Field()

class BundleItem(scrapy.Item):
    name = scrapy.Field()
    zh_name = scrapy.Field()
    collection_name = scrapy.Field()
    

    