from stardew_valley.spiders.simple_spider import SimpleSpider
from stardew_valley.utils.defines import CalendarType
from stardew_valley.models import CalendarDomain

class CanlendarSpider(SimpleSpider):
    url_path = 'others/Calendar'

    def parse(self, response):
        selector = response.selector
        tbodys = selector.xpath("//h2/following-sibling::table/tbody")
        # print(tbodys)
        spring_tables = tbodys[0].xpath(".//h3/following-sibling::table")
        summer_tables = tbodys[1].xpath(".//h3/following-sibling::table")
        fall_tables = tbodys[2].xpath(".//h3/following-sibling::table")
        winter_tables = tbodys[3].xpath(".//h3/following-sibling::table")

        seasons = [spring_tables, summer_tables, fall_tables, winter_tables]

        festival_items = []
        for idx, tables in enumerate(seasons):
            festival_items.extend(self._get_festival_items(tables[0], idx))
            
        other_items = []
        for idx, tables in enumerate(seasons[:-1]):
            other_items.extend(self._get_other_items(tables[1], idx))
            
        birthday_items = []
        for idx, tables in enumerate(seasons[:-1]):
            birthday_items.extend(self._get_birthday_items(tables[2], idx))
        birthday_items.extend(self._get_birthday_items(seasons[-1][1], idx))

        items = []
        items.extend(festival_items)
        items.extend(other_items)
        items.extend(birthday_items)
        CanlendarSpider.database.drop(CalendarDomain)
        CanlendarSpider.database.add(items)
            
    def _get_festival_items(self, table, offset):
        items = []
        trs = table.xpath(".//tr")
        for tr in trs[1:]:
            day_str = tr.xpath("./td[1]/text()").get()
            values = self._get_range(day_str)
            for value in values:
                item = CalendarDomain()
                item.day = value + offset * 28
                item.name = tr.xpath("./td[2]/p/a/text()").get()
                item.type = CalendarType.FESTIVAL
                items.append(item)
        return items

    def _get_other_items(self, table, offset):
        items = []
        trs = table.xpath(".//tr")
        for tr in trs[1:]:
            day_str = tr.xpath("./td[1]/text()").get()
            values = self._get_range(day_str)
            for value in values:
                item = CalendarDomain()
                item.day = value + offset * 28
                name = tr.xpath(".//td[2]//text()").extract()
                item.name = ''.join(name[:-1])
                item.type = CalendarType.EVENT
                items.append(item)
        return items

    def _get_birthday_items(self, table, offset):
        items = []
        trs = table.xpath(".//tr")
        for tr in trs[1:]:
            day_str = tr.xpath("./td[1]/text()").get()
            values = self._get_range(day_str)
            for value in values:
                item = CalendarDomain()
                item.day = value + offset * 28
                name = tr.xpath("./td[2]/a/text()").get()
                item.name = name
                item.type = CalendarType.BIRTHDAY
                items.append(item)
        return items

    def _get_range(self, str):
        if '-' not in str:
            return [int(str)]
        start, end = map(int, str.split('-'))
        return list(range(start, end + 1))
