import scrapy
from stardew_valley.database import Database
from stardew_valley.models import PlantableDetailDomain, PlantableDomain
from stardew_valley.utils.defines import Utils

class PlantableDetailSpider(scrapy.Spider):
    name = "plantable_detail_spider"
    allowed_domains = ["www.stardewvalleywiki.com"]

    def start_requests(self):
        Database().drop(PlantableDetailDomain)

        domains = Database().get_all(PlantableDomain)
        names = list(map(lambda x: f"plantables/{x.name}", domains))
        urls = list(map(lambda x: Utils.find_url(x), names))
        for url, name, domain in zip(urls, names, domains):
            print(f"{url}, {name}")
            yield scrapy.Request(url, self.parse, meta={"path": name, "domain": domain})


    def parse(self, response):
        name = response.meta['path']
        Utils.save_html(name, response.text)

        domain = response.meta['domain']
        id = domain.id
        name = domain.name
        growth_time = response.selector.xpath("//td[contains(text(),'Growth Time')]/following-sibling::td/text()").get()
        if growth_time is not None:
            growth_time = growth_time.split("days")[0].strip()
            growth_time = growth_time.split("Days")[0].strip()
            domain = PlantableDetailDomain()
            domain.id = id
            domain.name = name
            domain.growth_time = growth_time
        Database().add([domain])
