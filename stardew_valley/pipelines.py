# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy import signals
from stardew_valley.dao.collection_dao import CollectionDao
from stardew_valley.dao.collection_detail_dao import CollectionDetailDao
from stardew_valley.dao.villager_dao import VillagerDao
from stardew_valley.dao.villager_collection_dao import VillagerCollectionDao
from stardew_valley.dao.bundle_dao import BundleDao
from stardew_valley.dao.bundle_collection_dao import BundleCollectionDao
from stardew_valley.dao.cook_recipe_dao import CookRecipeDao
from stardew_valley.dao.cook_recipe_collection_dao import CookRecipeCollectionDao
from stardew_valley import items as Item


class StardewValleyPipeline:
    def process_item(self, item, spider):
        return item

class DatabasePipeline:
    def __init__(self):
        self.collection_items = []
        self.villager_collection_items = []
        self.collection_detail_items = []
        self.bundle_items = []
        self.bundle_collection_items = []
        self.cook_recipe_items = []
        self.cook_recipe_collection_items = []

    def process_item(self, item ,spider):
        if isinstance(item, Item.CollectionItem):
            self.collection_items.append(item)
        if isinstance(item, Item.CollectionDetailItem):
            self.collection_detail_items.append(item)
        if isinstance(item, Item.VilltagerItem):
            VillagerDao().create(item)
        if isinstance(item, Item.VilltagerCollectionItem):
            self.villager_collection_items.append(item)
        if isinstance(item, Item.BundleItem):
            self.bundle_items.append(item)
        if isinstance(item, Item.BundleCollectionItem):
            self.bundle_collection_items.append(item)
        if isinstance(item, Item.CookRecipeItem):
            self.cook_recipe_items.append(item)
        if isinstance(item, Item.CookRecipeCollectionItem):
            self.cook_recipe_collection_items.append(item)
        return item

    def close_spider(self, spider):
        if self.collection_items:
            CollectionDao().create_items(self.collection_items)
        if self.villager_collection_items:
            VillagerCollectionDao().create_items(self.villager_collection_items)
        if self.collection_detail_items:
            CollectionDetailDao().create_items(self.collection_detail_items)
        if self.bundle_items:
            BundleDao().create_items(self.bundle_items)
        if self.bundle_collection_items:
            BundleCollectionDao().create_items(self.bundle_collection_items)
        if self.cook_recipe_items:
            CookRecipeDao().create_items(self.cook_recipe_items)
        if self.cook_recipe_collection_items:
            CookRecipeCollectionDao().create_items(self.cook_recipe_collection_items)

class DownloadPipeline:
    def process_item(self, item ,spider):
        return item