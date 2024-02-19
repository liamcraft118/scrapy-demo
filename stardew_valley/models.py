from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from stardew_valley.database import Base
from stardew_valley.utils.defines import ReactionEnum, CalendarType, CollectionType

EnName = String(50)
ZhName = String(100)
Link = String(100)

class CollectionDomain(Base):
    __tablename__ = 'collection'
    id = Column(Integer, primary_key=True)
    name = Column(EnName)
    link = Column(Link)
    icon_link = Column(Link)
    type = Column(Enum(CollectionType))

class CollectionDetailDomain(Base):
    __tablename__ = 'collection_detail'
    id = Column(Integer, primary_key=True)
    growth_time = Column(Integer)

class VillagerDomain(Base):
    __tablename__ = 'villager'
    id = Column(Integer, primary_key=True)
    name = Column(EnName)
    birthday = Column(Integer)

class VillagerCollectionDomain(Base):
    __tablename__ = 'villager_collection'
    id = Column(Integer, primary_key=True)
    villager_id = Column(Integer)
    collection_id = Column(Integer)
    reaction = Column(Enum(ReactionEnum))

class BundleDomain(Base):
    __tablename__ = 'bundle'
    id = Column(Integer, primary_key=True)
    name = Column(EnName)

class BundleCollectionDomain(Base):
    __tablename__ = 'bundle_collection'
    id = Column(Integer, primary_key=True)
    bundle_id = Column(Integer)
    collection_id = Column(Integer)

class CookRecipeDomain(Base):
    __tablename__ = 'cook_recipe'
    id = Column(Integer, primary_key=True)
    name = Column(EnName)

class CookRecipeCollectionDomain(Base):
    __tablename__ = 'cook_recipe_collection'
    id = Column(Integer, primary_key=True)
    cook_recipe_id = Column(Integer)
    collection_id = Column(Integer)

class PlantableDomain(Base):
    __tablename__ = 'plantable'
    id = Column(Integer, primary_key=True)
    name = Column(EnName)

class SeasonDomain(Base):
    __tablename__ = 'season'
    id = Column(Integer, primary_key=True)
    name = Column(EnName)

class PlantableSeasionDomain(Base):
    __tablename__ = 'plantable_season'
    id = Column(Integer, primary_key=True)
    plantable_id = Column(Integer)
    season_id = Column(Integer)

class CalendarDomain(Base):
    __tablename__ = 'calendar'
    id = Column(Integer, primary_key=True)
    day = Column(Integer)
    name = Column(EnName)
    type = Column(Enum(CalendarType))

class PlantableDetailDomain(Base):
    __tablename__ = 'plantable_detail'
    id = Column(Integer, primary_key=True)
    name = Column(EnName)
    growth_time = Column(String(50))