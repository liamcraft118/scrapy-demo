from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
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

    def update(self, model: DeclarativeMeta, filters: dict, **kwargs):
        session = self.Session()
        session.query(model).filter_by(**filters).update(kwargs)
        session.commit()
        session.close()

    def add(self, domains):
        session = self.Session()
        for domain in domains:
            session.add(domain)
        session.commit()
        session.close()

    def delete(self, item):
        session = self.Session()
        session.delete(item)
        session.commit()
        session.close()

    def get_all(self, model):
        session = self.Session()
        results = session.query(model).all()
        session.close()
        return results


    def drop(self, domain_class):
        domain_class.__table__.drop(self.engine)
        self.init_database()

    def get_id_by_name(self, domain_class, name):
        session = self.Session()
        result = session.query(domain_class).filter(domain_class.name==name).first().id
        session.close()
        return result

    def get_first(self, model: DeclarativeMeta, filters: dict):
        return self.get(model, filters).first()

    def get(self, model: DeclarativeMeta, filters: dict):
        session = self.Session()
        result = session.query(model).filter_by(**filters)
        session.close()
        return result
