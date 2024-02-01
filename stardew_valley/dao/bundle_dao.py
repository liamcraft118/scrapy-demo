from stardew_valley.models import BundleDomain
from stardew_valley.database import Database

class BundleDao:
    def create_items(self, items):
        db_domains = self.get_all()
        for item in items:
            name = item['name']
            found_domain = [db_domain for db_domain in db_domains if db_domain.name == name]
            if found_domain:
                continue

            domain = BundleDomain()
            domain.name = name
            Database().create(domain)

    def get_all(self):
        return Database().query(BundleDomain).all()