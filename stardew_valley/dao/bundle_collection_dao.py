from stardew_valley.models import BundleCollectionDomain
from stardew_valley.dao.bundle_dao import BundleDao
from stardew_valley.dao.collection_dao import CollectionDao
from stardew_valley.database import Database

class BundleCollectionDao:
    def create_items(self, items):
        bundles = BundleDao().get_all()
        collections = CollectionDao().get_all()
        db_domains = self.get_all()

        unsaved_collections = []
        for item in items:
            bundle_name = item['bundle_name']
            collection_name = item['collection_name']

            bundle_id = [bundle for bundle in bundles if bundle.name == bundle_name]
            bundle_id = bundle_id[0].id

            collection_id = [collection for collection in collections if collection.name == collection_name]
            if not collection_id:
                unsaved_collections.append(collection_name)
                continue
            collection_id = collection_id[0].id

            found_domain = [db_domain for db_domain in db_domains if db_domain.bundle_id == bundle_id and db_domain.collection_id == collection_id]
            if found_domain:
                continue

            domain = BundleCollectionDomain()
            domain.bundle_id = bundle_id
            domain.collection_id = collection_id
            Database().create(domain)

        print(unsaved_collections)

    def get_all(self):
        return Database().query(BundleCollectionDomain).all()