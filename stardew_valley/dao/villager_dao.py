from stardew_valley.models import VillagerDomain
from stardew_valley.database import Database

class VillagerDao:
    def create(self, item):
        name = item['name']
        domains = self.get_all()
        found_domain = [domain for domain in domains if domain.name == name]
        if found_domain:
            return

        domain = VillagerDomain()
        domain.name = item["name"]
        domain.link = item["link"]
        domain.icon_link = item['icon_link']
        Database().create(domain)

    def get_all(self):
        return Database().query(VillagerDomain).all()

    def get_by_name(self, name):
        return Database().query(VillagerDomain).filter(VillagerDomain.name==name).first()
        # return Database().query(VillagerDomain).