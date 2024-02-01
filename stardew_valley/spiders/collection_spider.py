import scrapy
from stardew_valley.items import CollectionsItem
from stardew_valley.dao.collection_dao import CollectionDao
from stardew_valley.utils.defines import Utils

class CollectionSpider(scrapy.Spider):
    name = "collection_spider"
    allowed_domains = ["stardewvalleywiki.com"]

    def start_requests(self):
        yield scrapy.Request("https://www.stardewvalleywiki.com/Collections", callback=self.parse)

    def parse(self, response):
        tables = response.selector.xpath("//table[@class='wikitable']")

        items_list = []
        for table in tables:
            en_as = table.xpath(".//a")
            items = self._parse_item(en_as)
            items_list.extend(items)

        extra_list = self._gen_extra_list()
        items_list.extend(extra_list)
        for item in items_list:
            yield item

    # <a href="/%E9%87%8E%E5%B1%B1%E8%91%B5" title="野山葵">野山葵</a>
    def _parse_item(self, en_as):
        items = []
        for en_a in en_as:
            item = CollectionsItem()
            item["name"] = en_a.xpath("./text()").get()
            item['link'] = en_a.xpath("@href").get()[1:]
            items.append(item)
        return items
            
    def _gen_extra_list(self):
        names = ['Coffee', 'Pickles', 'Wine', 'Omni Geode', 'Piña Colada']
        name_1 = ['Wheat Flour', 'Sugar', 'Oil', 'Rice', 'Vinegar']
        names.extend(name_1)
        
        items = []
        for name in names:
            item  = CollectionsItem()
            item["name"] = name
            item['link'] = name
            items.append(item)
            
        # any fish
        item = CollectionsItem()
        item['name'] = 'Any Fish'
        item['link'] = None
        items.append(item)

        return items
