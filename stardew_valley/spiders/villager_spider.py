import re
import scrapy
import os
from stardew_valley.items import VilltagerItem

class VillagerSpider(scrapy.Spider):
    name = "villager_spider"
    allowed_domains = ["www.stardewvalleywiki.com"]

    def __init__(self, *args, **kwargs):
        super(VillagerSpider, self).__init__(*args, **kwargs)
        self.curr_path = os.getcwd()
        self.resource_path = f'{self.curr_path}/stardew_valley/resources/villagers'

    def start_requests(self):
        yield scrapy.Request(url="https://www.stardewvalleywiki.com/Parsnip", callback=self.parse)

    def parse(self, response):
        table = response.selector.xpath("//h2[span[@id='Gifting']]/following-sibling::table")[0]
        tags = table.xpath(".//a[img]")
        for tag in tags:
            item = self._parse_item(tag)
            yield item

    def _parse_item(self, tag):
        item = VilltagerItem()
        item['name'] = tag.xpath("@title").get()
        item['link'] = tag.xpath("@href").get()
        item['icon_link'] = tag.xpath("./img/@src").get()
        return item