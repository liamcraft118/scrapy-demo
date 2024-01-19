import scrapy


class StardewValleyWiKiSpider(scrapy.Spider):
    name = "stardew_valley_wiki"
    allowed_domains = ["zh.stardewvalleywiki.com"]
    host = "https://zh.stardewvalleywiki.com"
    start_urls = [f"{host}/mediawiki/index.php?titleD=Stardew_Valley_Wiki&variant=zh"]

    def parse(self, response):
        trs = response.selector.xpath("//div[@id='mainmenucontainer']//tr")
        if len(trs) %2 != 0:
            raise ValueError("must be even number")

        titles = trs[::2].xpath(".//th/text()").extract()
        print(titles)
        # ps = list(map(lambda td: td.xpath(".//p"), trs[1::2].xpath(".//td")))
        # home_links_list = []
        # for p in ps:
        #     home_links = []
        #     for v in p:
        #         home_link = HomeLinkItem()
        #         # image
        #         image = ImageItem()
        #         image["name"] = v.xpath("./img/@alt").get()
        #         image["link"] = v.xpath("./img/@src").get()
        #         image["width"] = v.xpath("./img/@width").get()
        #         image["height"] = v.xpath("./img/@height").get()

        #         # home_link
        #         home_link["image"] = image
        #         home_link["name"] = v.xpath("./a/text()").get()
        #         home_link["link"] = f"{StardewValleyWikiSpider.host}{v.xpath('./a/@href').get()}"

        #         home_links.append(home_link)
        #     home_links_list.append(home_links)

        # for title, home_links in zip(titles, home_links_list):
        #     item = HomeItem()
        #     item["type_name"] = title
        #     item["home_links"] = home_links
        #     print(item)
            # yield item
