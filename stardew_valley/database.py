from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
mysql_url = 'mysql://root:password@localhost:3306/mydatabase'

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

    def create(self, domain):
        session = self.Session()
        session.add(domain)
        session.commit()
        session.close()

    def query(self, domain_class):
        session = self.Session()
        domains = session.query(domain_class)
        return domains