import scrapy
from stardew_valley.database import Database
from stardew_valley.models import CollectionDomain
from stardew_valley.utils.defines import CollectionType


class CollectionsSpider(scrapy.Spider):
    name = "collections_spider"
    allowed_domains = ["stardewvalleywiki.com"]

    def start_requests(self):
        Database().drop(CollectionDomain)
        yield scrapy.Request(
            "https://www.stardewvalleywiki.com/Collections", callback=self.parse
        )

    def parse(self, response):
        tables = response.selector.xpath("//table[@class='wikitable']")

        for idx, table in enumerate(tables):
            if idx in (0, 1, 2):
                yield from self._parse_item(table, 0)
            else:
                yield from self._parse_item(table, idx - 2)

    def _parse_item(self, table, idx):
        for a in table.xpath(".//a"):
            name = a.xpath("./text()").get()
            link = a.xpath("@href").get()[1:]
            url = f"https://www.stardewvalleywiki.com/{link}"
            type = self._gen_collection_type(idx)
            self._save_to_db(name, link, type)
            yield scrapy.Request( url=url,
                callback=self.parse_link,
                meta={"name": name, "link": link},
                dont_filter=True
            )
            
    def _save_to_db(self, name, link, type):
        domain = CollectionDomain()
        domain.name = name
        domain.link = link
        domain.type = type
        Database().create(domain)

    def parse_link(self, response):
        name = response.meta["name"]
        link = response.meta["link"]

        selector = response.selector
        src = selector.xpath(f"//a[contains(@href, '/File:{link}')]/img/@src").get()
        
        if name == 'Pickles (any)':
            src = '/mediawiki/images/c/c7/Pickles.png'
        if name == 'Egg (brown)':
            src = '/mediawiki/images/0/01/Brown_Egg.png'
        if name == 'Large Egg (brown)':
            src = '/mediawiki/images/9/91/Large_Brown_Egg.png'
        if name == 'Jelly (any)':
            src = '/mediawiki/images/0/05/Jelly.png'
            
        id = Database().get_first(CollectionDomain, {'name': name, 'link': link}).id
        Database().update(CollectionDomain, {'id': id}, icon_link=src)

    def _gen_collection_type(self, idx):
        dict = {
            0: CollectionType.SHIPPED_ITEM,
            1: CollectionType.FISH,
            2: CollectionType.ARTIFACT,
            3: CollectionType.MINERAL,
            4: CollectionType.COOKING,
        }

        return dict[idx]
