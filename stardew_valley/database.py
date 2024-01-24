from sqlalchemy import create_engine, Column, String, Text, Integer, ForeignKey, MetaData, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from stardew_valley.items import CollectionsItem

Base = declarative_base()
mysql_url = 'mysql://root:password@localhost:3306/mydatabase'

class CollectionDomain(Base):
    __tablename__ = 'collection'
    id = Column(Integer, primary_key=True)
    zh_name = Column(String(100))
    en_name = Column(String(50))
    link = Column(String(100))

class Database:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.engine = create_engine(mysql_url)
            cls._instance.Session = sessionmaker(bind=cls._instance.engine)
        return cls._instance

    def init_database(self):
        Base.metadata.create_all(self.engine)

    def remove_all_tables(self):
        Base.metadata.drop_all(self.engine)

    def save_collection(self, item):
        domain = CollectionDomain()
        domain.zh_name = item["zh_name"]
        domain.en_name = item["en_name"]
        domain.link = item["link"]

        session = self.Session()
        session.add(domain)
        session.commit()
        session.close()

    def check_collections_exist(self):
        session = self.Session()
        has_data = session.query(CollectionDomain).first() is not None
        session.close()
        return has_data
    
    def get_collections(self):
        session = self.Session()
        domains = session.query(CollectionDomain)
        items = []
        for domain in domains:
            item = CollectionsItem()
            item["zh_name"] = domain.zh_name
            item["en_name"] = domain.en_name
            item["link"] = domain.link
            items.append(item)
        return items