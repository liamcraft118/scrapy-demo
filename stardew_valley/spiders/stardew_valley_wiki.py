import scrapy
from stardew_valley.items import CollectionsItem
from stardew_valley.database import Database

class StardewValleyWiKiSpider(scrapy.Spider):
    name = "stardew_valley_wiki"
    allowed_domains = ["stardewvalleywiki.com"]
    host = "https://zh.stardewvalleywiki.com"
    start_urls = [f"{host}/%E6%94%B6%E9%9B%86%E5%93%81", f"https://www.stardewvalleywiki.com/Collections"]

    def start_requests(self):
        if Database().check_collections_exist():
            print("collections is existed, don't scrape")
        else:
            print("collections is not existed, start scrape")
            yield scrapy.Request(self.start_urls[0], callback=self.parse_zh)

    def parse_zh(self, response):
        yield scrapy.Request(self.start_urls[1], callback=self.parse_en, meta={"data": response})

    def parse_en(self, en_response):
        zh_response = en_response.meta["data"]
        items_list = self.parse(zh_response, en_response)

        for items in items_list:
            for item in items:
                yield item
        
    def parse(self, zh_response, en_response):
        zh_tables = zh_response.selector.xpath("//table[@class='wikitable']")
        en_tables = en_response.selector.xpath("//table[@class='wikitable']")
        items_shipped = []
        fishes = []
        artifacts = []
        minerals = []

        items_list = []
        for zh_table, en_table in zip(zh_tables, en_tables):
            zh_as = zh_table.xpath(".//a")
            en_as = en_table.xpath(".//a")
            items = self.parse_item(zh_as, en_as)
            items_list.append(items)
        
        items_shipped.extend(items_list[0:3][0])
        fished = items_list[3]
        artifacts = items_list[4]
        minerals = items_list[5]

        return items_list

    # <a href="/%E9%87%8E%E5%B1%B1%E8%91%B5" title="野山葵">野山葵</a>
    def parse_item(self, zh_as, en_as):
        collections = []
        for zh_a, en_a in zip(zh_as, en_as):
            collection = CollectionsItem()
            collection["zh_name"] = zh_a.xpath("./text()").get()
            collection["en_name"] = en_a.xpath("./text()").get()
            collection["link"] = zh_a.xpath("@href").get()
            collections.append(collection)
        return collections
            