from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

Base = declarative_base()
mysql_url = 'mysql://root:password@localhost:3306/mydatabase'

class Database:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            pymysql.install_as_MySQLdb()
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.engine = create_engine(mysql_url, pool_size=5, max_overflow=10)
            cls._instance.Session = sessionmaker(bind=cls._instance.engine)
            cls._instance.init_database()
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
        session.close()
        return domains
    
    def add(self, domains):
        session = self.Session()
        for domain in domains:
            session.add(domain)
        session.commit()

    def delete(self, item):
        session = self.Session()
        session.delete(item)
        session.commit()

    def get_all(self, model):
        return self.session.query(model).all()

    def drop(self, domain_class):
        domain_class.__table__.drop(self.engine)
        self.init_database()

    def get_id_by_name(self, domain_class, name):
        session = self.Session()
        result = session.query(domain_class).filter(domain_class.name==name).first().id
        session.close()
        return result