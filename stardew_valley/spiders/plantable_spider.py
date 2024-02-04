from stardew_valley.models import PlantableDomain, PlantableSeasionDomain, SeasonDomain
from stardew_valley.spiders.simple_spider import SimpleSpider

class PlantableSpider(SimpleSpider):
    url_path = 'others/Spring_Seeds'

    def parse(self, response):
        selector = response
        self._scrape_season(selector)
        self._scrape_plantable(selector)
        self._scrape_plantable_season(selector)

    def _scrape_plantable(self, selector):
        names = selector.xpath("(//table)[last()]//tr[position() > 1]/td/a/text()").extract()
        names = sorted(set(names))

        domains = []
        for name in names:
            domain = PlantableDomain()
            domain.name = name
            domains.append(domain)

        # PlantableSpider.database.drop(PlantableDomain)
        # PlantableSpider.database.add(domains)

    def _scrape_season(self, selector):
        names = selector.xpath("(//table)[last()]//tr[position() > 1]/th/text()").extract()
        names = list(map(lambda x: x.replace('\n', ''), names))
        domains = []
        for name in names:
            domain = SeasonDomain()
            domain.name = name
            domains.append(domain)

        # PlantableSpider.database.drop(SeasonDomain)
        # PlantableSpider.database.add(domains)

    def _scrape_plantable_season(self, selector):
        trs = selector.xpath("(//table)[last()]//tr[position() > 1]")
        domains = []
        for tr in trs:
            season_name = tr.xpath("./th/text()").get()
            season_name = season_name.replace('\n', '')
            season_id = PlantableSpider.database.get_id_by_name(SeasonDomain, season_name)
            plantable_names = tr.xpath(".//td/a/text()").extract()
            for plantable_name in plantable_names:
                plantable_id = PlantableSpider.database.get_id_by_name(PlantableDomain, plantable_name)
                domain = PlantableSeasionDomain()
                domain.season_id = season_id
                domain.plantable_id = plantable_id
                domains.append(domain)

        PlantableSpider.database.drop(PlantableSeasionDomain)
        PlantableSpider.database.add(domains)