from stardew_valley.dao.collection_dao import CollectionDao
from stardew_valley.dto.stardew_valley_dto import StardewValleyDTO

class StardewValleyService:
    def findAllCollections(self):
        domains = CollectionDao().get_all()
        dtos = list(map(lambda x: StardewValleyDTO.model_validate(x.__dict__), domains))
        return dtos
