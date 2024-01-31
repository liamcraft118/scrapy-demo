import scrapy
import os
from stardew_valley.items import VilltagerCollectionItem
from stardew_valley.utils.defines import ReactionEnum

class VillagerCollectionSpider(scrapy.Spider):
    name = "villager_collection_spider"
    allowed_domains = ["www.stardewvalleywiki.com"]

    def start_requests(self):
        url = f"https://www.stardewvalleywiki.com/List_of_All_Gifts"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        trs = response.selector.xpath("//tbody/tr")
        for tr in trs[2:]:
            villager_name = tr.xpath("./td[1]/a[2]/text()").get()
            love_collection_names = tr.xpath("./td[3]//a/text()").extract()
            yield from self._create_items(villager_name, love_collection_names, ReactionEnum.LOVE)

    def _create_items(self, villager_name, collection_names, reaction):
        items = []
        for collection_name in collection_names:
            item = VilltagerCollectionItem()
            item["villager_name"] = villager_name
            item["collection_name"] = collection_name
            item["reaction"] = reaction
            items.append(item)
        return items