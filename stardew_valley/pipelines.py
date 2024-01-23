# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from stardew_valley.database import Database


class StardewValleyPipeline:
    def process_item(self, item, spider):
        return item

class DatabasePipeline:
    def process_item(self, item ,spider):
        Database().save_collection(item)
        return item