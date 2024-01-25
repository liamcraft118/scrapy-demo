# dao/user_dao.py

from stardew_valley.models import CollectionDomain
from stardew_valley.items import CollectionsItem
from stardew_valley.database import Database

class CollectionDao:
    def save_collection(self, item):
        domain = CollectionDomain()
        domain.zh_name = item["zh_name"]
        domain.en_name = item["en_name"]
        domain.link = item["link"]

        Database().create(domain)

    def check_collections_exist(self):
        session = self.Session()
        has_data = Database().query(CollectionDomain).first() is not None
        session.close()
        return has_data
    
    def get_collections(self):
        domains = Database().query(CollectionDomain)
        items = []
        for domain in domains:
            item = CollectionsItem()
            item["zh_name"] = domain.zh_name
            item["en_name"] = domain.en_name
            item["link"] = domain.link
            items.append(item)
        return items