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
from stardew_valley.items import CollectionsItem, CollectionDetailItem, VilltagerItem, VilltagerCollectionItem


class StardewValleyPipeline:
    def process_item(self, item, spider):
        return item

class DatabasePipeline:
    def __init__(self):
        self.collection_items = []
        self.villager_collection_items = []
        self.collection_detail_items = []

    def process_item(self, item ,spider):
        if isinstance(item, CollectionsItem):
            self.collection_items.append(item)
        if isinstance(item, CollectionDetailItem):
            self.collection_detail_items.append(item)
        if isinstance(item, VilltagerItem):
            VillagerDao().create(item)
        if isinstance(item, VilltagerCollectionItem):
            self.villager_collection_items.append(item)
        return item

    def close_spider(self, spider):
        if self.collection_items:
            CollectionDao().create_items(self.collection_items)
        if self.villager_collection_items:
            VillagerCollectionDao().create_items(self.villager_collection_items)
        if self.collection_detail_items:
            CollectionDetailDao().create_items(self.collection_detail_items)

class DownloadPipeline:
    def process_item(self, item ,spider):
        return item