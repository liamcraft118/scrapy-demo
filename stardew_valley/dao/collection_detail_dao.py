from stardew_valley.models import CollectionDetailDomain
from stardew_valley.database import Database
from stardew_valley.dao.collection_dao import CollectionDao

class CollectionDetailDao:
    def create_items(self, items):
        for item in items:
            name = item["name"]
            collections = CollectionDao().get_all()
            found_collection = [collection for collection in collections if collection.name == name]
            if not found_collection: 
                return

            domain = CollectionDetailDomain()
            domain.id = found_collection[0].id
            domain.growth_time = item["growth_time"]
            Database().create(domain)