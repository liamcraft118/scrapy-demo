import scrapy
from stardew_valley.items import BundleCollectionItem
from stardew_valley.dao.bundle_dao import BundleDao
from stardew_valley.utils.defines import Utils

class BundleCollectionSpider(scrapy.Spider):
    name = "bundle_collection_spider"
    allowed_domains = ["stardewvalleywiki.com"]
    url_name = "others/Bundles"

    def start_requests(self):
        url = Utils.find_url(self.url_name)
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        Utils.save_html(self.url_name, response.text)
        bundles = BundleDao().get_all()
        bundle_names = list(map(lambda x: x.name, bundles))
        selector = response

        for bundle_name in bundle_names:
            bundle_name = bundle_name.replace("'", "\\'")
            collection_names = selector.xpath(f"//tr[th[text()=\"{bundle_name}\"]]/../tr/td/span/a/text()").extract()
            for collection_name in collection_names:
                item = BundleCollectionItem()
                item['bundle_name'] = bundle_name
                item['collection_name'] = collection_name
                yield item