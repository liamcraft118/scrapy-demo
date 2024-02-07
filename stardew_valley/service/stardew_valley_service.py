from stardew_valley.dao.collection_dao import CollectionDao
from stardew_valley.dto.stardew_valley_dto import CalendarDTO, PlantableDetailDTO, StardewValleyDTO
from stardew_valley.database import Database
from stardew_valley.models import CalendarDomain, PlantableDetailDomain

class StardewValleyService:
    def findAllCollections(self):
        domains = CollectionDao().get_all()
        dtos = list(map(lambda x: StardewValleyDTO.model_validate(x.__dict__), domains))
        return dtos

    def find_calendar(self):
        domains = Database().get_all(CalendarDomain)
        dtos = list(map(lambda x: CalendarDTO.model_validate(x.__dict__), domains))
        dtos.sort(key=lambda x: x.day)
        return dtos

    def find_plantable(self):
        domains = Database().get_all(PlantableDetailDomain)
        dtos = list(map(lambda x: PlantableDetailDTO.model_validate(x.__dict__), domains))
        return dtos