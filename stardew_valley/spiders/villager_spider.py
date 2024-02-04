import scrapy
from stardew_valley.items import VilltagerItem
from stardew_valley.utils.defines import Utils

class VillagerSpider(scrapy.Spider):
    name = "villager_spider"
    allowed_domains = ["www.stardewvalleywiki.com"]
    url_path = 'others/Calendar'

    def start_requests(self):
        url = Utils.find_url(self.url_path)
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        Utils.save_html(self.url_path, response.text)
        selector = response.selector
        tables = selector.xpath("//h3[span[text()='Birthdays']]/following-sibling::table")
        for table in tables:
            trs = table.xpath(".//tr")
            for tr in trs[1:]:
                item = VilltagerItem()
                item['name'] = tr.xpath("./td/a/text()").get()
                item['birthday'] = tr.xpath("./td/text()").get()
                yield item