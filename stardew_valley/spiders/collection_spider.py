import scrapy
import os
from stardew_valley.items import CollectionDetailItem
from stardew_valley.dao.collection_dao import CollectionDao
from stardew_valley.database import Database

class CollectionSpider(scrapy.Spider):
    name = "collection_spider"
    allowed_domains = ["stardewvalleywiki.com"]
    host = "https://zh.stardewvalleywiki.com"
    # start_urls = [f"{host}/%E6%94%B6%E9%9B%86%E5%93%81", f"https://www.stardewvalleywiki.com/Collections"]

    def __init__(self, *args, **kwargs):
        super(CollectionSpider, self).__init__(*args, **kwargs)
        self.curr_path = os.getcwd()
        self.resource_path = f'{self.curr_path}/stardew_valley/resources'
        

    def start_requests(self):
        downloaded_files = self._get_downloaded_htmls()
        items = CollectionDao().get_collections()
        result_items = [item for item in items if item['zh_name'] not in downloaded_files]

        if (len(result_items) == 0):
            print("all collection is downloaded")
            for file_name in downloaded_files[0:2]:
                file_url = f"file://{self.resource_path}/{file_name}"
                yield scrapy.Request(url=file_url, callback=self.parse)
        else:
            for item in result_items:
                link = f"{self.host}{item['link']}"
                yield scrapy.Request(url=link, callback=self.download_htmls, meta={"item": item})

    # parse collection html
    def parse(self, response):
        pass

    # download htmls
    def download_htmls(self, response):
        collection_item = response.meta["item"]
        zh_name = collection_item["zh_name"]
        self._save_html_to_file(zh_name, response.text)

    # html files input/output
    def _save_html_to_file(self, name, html):
        directory = self.resource_path
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(f"{directory}/{name}", "w", encoding="utf-8") as f:
            f.write(html)

    def _get_downloaded_htmls(self):
        directory = self.resource_path
        file_names = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        return file_names
