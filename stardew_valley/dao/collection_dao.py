# dao/user_dao.py

from stardew_valley.models import CollectionDomain
from stardew_valley.items import CollectionItem
from stardew_valley.database import Database

class CollectionDao:
    def create_items(self, items):
        db_domains = self.get_all()
        for item in items:
            name = item['name']
            link = item['link']
            found_domain = [db_domain for db_domain in db_domains if db_domain.name == name]
            if found_domain:
                continue

            domain = CollectionDomain()
            domain.name = name
            domain.link = link
            Database().create(domain)

    def check_collections_exist(self):
        has_data = Database().query(CollectionDomain).first() is not None
        return has_data
    
    def get_collections(self):
        domains = Database().query(CollectionDomain)
        items = []
        for domain in domains:
            item = CollectionItem()
            item["name"] = domain.name
            item["link"] = domain.link
            items.append(item)
        return items

    def get_all(self):
        return Database().query(CollectionDomain).all()
    
    def get_by_en_name(self, name):
        return Database().query(CollectionDomain).filter(CollectionDomain.name==name).first()