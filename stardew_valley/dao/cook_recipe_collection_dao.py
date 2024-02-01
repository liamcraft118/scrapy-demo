from stardew_valley.models import CookRecipeCollectionDomain
from stardew_valley.dao.cook_recipe_dao import CookRecipeDao
from stardew_valley.dao.collection_dao import CollectionDao
from stardew_valley.database import Database

class CookRecipeCollectionDao:
    def create_items(self, items):
        cook_recipes = CookRecipeDao().get_all()
        collections = CollectionDao().get_all()
        db_domains = self.get_all()

        unsaved_collections = set()
        for item in items:
            cook_recipe_name = item['cook_recipe_name']
            collection_name = item['collection_name']

            cook_recipe_id = [cook_recipe for cook_recipe in cook_recipes if cook_recipe.name == cook_recipe_name]
            cook_recipe_id = cook_recipe_id[0].id

            collection_id = [collection for collection in collections if collection.name == collection_name]
            if not collection_id:
                unsaved_collections.add(collection_name)
                continue
            collection_id = collection_id[0].id

            found_domain = [db_domain for db_domain in db_domains if db_domain.cook_recipe_id == cook_recipe_id and db_domain.collection_id == collection_id]
            if found_domain:
                continue

            domain = CookRecipeCollectionDomain()
            domain.cook_recipe_id = cook_recipe_id
            domain.collection_id = collection_id
            Database().create(domain)

        print(unsaved_collections)

    def get_all(self):
        return Database().query(CookRecipeCollectionDomain).all()