import scrapy
import os
from stardew_valley.items import CollectionDetailItem
from stardew_valley.dao.collection_dao import CollectionDao
from stardew_valley.utils.defines import Utils

class CollectionDetailSpider(scrapy.Spider):
    name = "collection_detail_spider"
    allowed_domains = ["www.stardewvalleywiki.com"]

    def __init__(self, *args, **kwargs):
        super(CollectionDetailSpider, self).__init__(*args, **kwargs)
        self.curr_path = os.getcwd()
        self.resource_path = f'{self.curr_path}/stardew_valley/resources/collections'

    def start_requests(self):
        downloaded_files = Utils.get_downloaded_htmls()
        items = CollectionDao().get_collections()
        undownload_items = [item for item in items if item['name'] not in downloaded_files]

        if undownload_items:
            for item in undownload_items:
                link = item['link']
                link = f"https://www.stardewvalleywiki.com/{link}"
                yield scrapy.Request(url=link, callback=self.download_htmls, meta={"item": item})
        else:
            print("all collection is downloaded")
            for file_name in downloaded_files:
                file_url = f"file://{self.resource_path}/{file_name}"
                yield scrapy.Request(url=file_url, callback=self.parse, meta={"name": file_name})

#   <tr>
# 		<td id="infoboxsection">Growth Time</td>
# 		<td id="infoboxdetail">4 days</td>
# 	</tr>
    # parse collection html
    def parse(self, response):
        name = response.meta["name"]
        growth_time = response.selector.xpath("//td[text()='Growth Time']/following-sibling::td/text()").get()
        if growth_time is not None:
            growth_time = growth_time.split("days")[0].strip()
        item = CollectionDetailItem()
        item["name"] = name
        item["growth_time"] = growth_time
        yield item

    # download htmls
    def download_htmls(self, response):
        item = response.meta["item"]
        name = item["name"]
        html = response.text
        path = f"{Utils.resource_path}"
        Utils.save_html_to_file(name, html, path)
