from sqlalchemy import and_
from stardew_valley.models import VillagerCollectionDomain
from stardew_valley.database import Database
from stardew_valley.dao.villager_dao import VillagerDao
from stardew_valley.dao.collection_dao import CollectionDao

class VillagerCollectionDao:
    def create_items(self, items):
        villagers = VillagerDao().get_all()
        collections = CollectionDao().get_all()
        domains = self.get_all()

        unsaved_col_nm = []
        for item in items:
            villager_name = item['villager_name']
            collection_name = item['collection_name']
            reaction = item['reaction']
            found_villager = [villager for villager in villagers if villager.name == villager_name]
            if not found_villager: 
                print(f"villager {villager_name} not exists")
                continue
            found_villager = found_villager[0]

            found_collection = [collection for collection in collections if collection.name == collection_name]
            if not found_collection:
                unsaved_col_nm.append(collection_name)
                print(f"collection {collection_name} not exists")
                continue
            found_collection = found_collection[0]

            found_domain = [domain for domain in domains if domain.villager_id == found_villager.id and domain.collection_id == found_collection.id]
            if found_domain:
                continue
            
            domain = VillagerCollectionDomain()
            domain.villager_id = found_villager.id
            domain.collection_id = found_collection.id
            domain.reaction = reaction
            Database().create(domain)
        print(f'unsaved_col_nm = {unsaved_col_nm}')

    def get_all(self):
        return Database().query(VillagerCollectionDomain).all()

    def get_by_id(self, villager_id, collection_id):
        return Database().query(VillagerCollectionDomain).filter(and_(VillagerCollectionDomain.villager_id==villager_id, VillagerCollectionDomain.collection_id==collection_id))

    def _get_villager_by_name(self, name):
        return VillagerDao().get_by_name(name)

    def _get_collection_by_name(self, name):
        return CollectionDao().get_by_en_name(name)