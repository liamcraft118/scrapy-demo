from pydantic import BaseModel
from stardew_valley.utils.defines import CalendarType, CollectionType

class StardewValleyDTO(BaseModel):
    name: str

class CalendarDTO(BaseModel):
    day: int
    name: str
    type: CalendarType

class PlantableDetailDTO(BaseModel):
    name: str
    growth_time: str

class CollectionDTO(BaseModel):
    name: str
    link: str
    icon_link: str
    type: CollectionType
