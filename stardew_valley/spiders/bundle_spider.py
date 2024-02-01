import scrapy
from stardew_valley.items import BundleItem
from stardew_valley.dao.bundle_dao import BundleDao

class BundleSpider(scrapy.Spider):
    name = "bundle_spider"
    allowed_domains = ["www.stardewvalleywiki.com"]

    def start_requests(self):
        url = "https://www.stardewvalleywiki.com/Bundles"
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        selector = response
        # trs = selector.xpath("tr[th[@id='Spring_Foraging_Bundle']]")
        bundles = selector.xpath("//tr[th[contains(@id, 'Bundle')]]/th[@id]/text()").extract()
        names = []
        names.extend(bundles[:-5])
        names.append(bundles[-1])
        for name in names:
            item = BundleItem()
            item['name'] = name
            yield item


