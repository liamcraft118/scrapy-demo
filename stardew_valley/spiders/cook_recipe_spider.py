import scrapy
from stardew_valley.items import CookRecipeItem
from stardew_valley.utils.defines import Utils

class CookRecipeSpider(scrapy.Spider):
    name = "cook_recipe_spider"
    allowed_domains = ["www.stardewvalleywiki.com"]
    url_path = "others/Cooking"

    def start_requests(self):
        url = Utils.find_url(self.url_path)
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        Utils.save_html(self.url_path, response.text)
        selector = response
        trs = selector.xpath("//h2[span[@id='Recipes']]/following-sibling::table[1]/tbody/tr")
        names = trs.xpath("./td[2]/a/text()").extract()
        for name in names:
            item = CookRecipeItem()
            item['name'] = name
            yield item