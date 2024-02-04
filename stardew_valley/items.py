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
    birthday = scrapy.Field()

class VilltagerCollectionItem(scrapy.Item):
    villager_name = scrapy.Field()
    collection_name = scrapy.Field()
    reaction = scrapy.Field()

class BundleItem(scrapy.Item):
    name = scrapy.Field()

class BundleCollectionItem(scrapy.Item):
    bundle_name = scrapy.Field()
    collection_name = scrapy.Field()

class CookRecipeItem(scrapy.Item):
    name = scrapy.Field()

class CookRecipeCollectionItem(scrapy.Item):
    cook_recipe_name = scrapy.Field()
    collection_name = scrapy.Field()

# class PlantableItem(scrapy.Item):
#     name = scrapy.Field()

# class SeasonItem(scrapy.Item):
#     name = scrapy.Field()

# class PlantableSeasionItem(scrapy.Field):
#     plantable_name = scrapy.Field()
#     season_name = scrapy.Field()

# class CalendarItem(scrapy.Field):
#     day = scrapy.Field()
#     name = scrapy.Field()
#     type = scrapy.Field()