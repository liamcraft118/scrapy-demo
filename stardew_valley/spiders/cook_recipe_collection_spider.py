import scrapy
from stardew_valley.items import CookRecipeCollectionItem
from stardew_valley.dao.cook_recipe_dao import CookRecipeDao
from stardew_valley.utils.defines import Utils, SpecColEnum

class CookRecipeCollectionSpider(scrapy.Spider):
    name = "cook_recipe_collection_spider"
    allowed_domains = ["www.stardewvalleywiki.com"]
    url_path = "others/Cooking"

    def start_requests(self):
        url = Utils.find_url(self.url_path)
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        selector = response.selector
        Utils.save_html(self.url_path, response.text)

        table = selector.xpath("//h2[span[@id='Recipes']]/following-sibling::table[1]")
        cook_recipes = CookRecipeDao().get_all()
        cook_recipe_names = list(map(lambda x: x.name, cook_recipes))
        for cook_recipe_name in cook_recipe_names:
            td = table.xpath(f".//tr[child::td[a[text()=\"{cook_recipe_name}\"]]]/td[4]")
            collection_names = td.xpath("./span/a/text()").extract()
            any_fish = td.xpath("./a/text()").get()
            if any_fish:
                collection_names.append(SpecColEnum.ANY_FISH.value)
            for collection_name in collection_names:
                if collection_name == 'Egg':
                    collection_name = 'Egg (white)'
                item = CookRecipeCollectionItem()
                item['cook_recipe_name'] = cook_recipe_name
                item['collection_name'] = collection_name
                yield item