from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PythonEnum
from stardew_valley.database import Base

EnName = String(50)
ZhName = String(100)

class ReactionEnum(PythonEnum):
    LOVE = "love"
    LIKE = "like"
    DISLIKE = "dislike"

class CollectionDomain(Base):
    __tablename__ = 'collection'
    id = Column(Integer, primary_key=True)
    zh_name = Column(ZhName)
    en_name = Column(EnName)
    link = Column(String(100))
    detail = relationship("CollectionDetailDomain", back_populates="collection")

class CollectionDetailDomain(Base):
    __tablename__ = 'collection_detail'
    id = Column(Integer, ForeignKey('collection.id'), primary_key=True)
    growth_time = Column(Integer)
    collection = relationship("CollectionDomain", back_populates="detail")

class VillagerDomain(Base):
    __tablename__ = 'villager'
    id = Column(Integer, primary_key=True)
    name = Column(EnName)
    zh_name = Column(ZhName)
    icon_link = Column(String(255))

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
    zh_name = Column(ZhName)

class BundleCollectionDomain(Base):
    __tablename__ = 'bundle_collectin'
    id = Column(Integer, primary_key=True)
    bundle_id = Column(Integer)
    collection_id = Column(Integer)

class RecipeDomain(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    name = Column(EnName)
    zh_name = Column(ZhName)

class RecipeCollectionDomain(Base):
    __tablename__ = 'recipe_collection'
    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer)
    collection_id = Column(Integer)