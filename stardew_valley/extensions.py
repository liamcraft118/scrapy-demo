from scrapy import signals
from stardew_valley.database import Database
import pymysql

class DatabaseExtension:
    @classmethod
    def from_crawler(cls, crawler):
        ext = cls()
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        return ext

    def spider_opened(self, spider):
        pymysql.install_as_MySQLdb()
        database = Database()
        database.remove_all_tables()
        database.init_database()