import inspect
import os
import scrapy
from stardew_valley.utils.defines import Utils
from stardew_valley.database import Database

class SimpleSpider(scrapy.Spider):
    name = ""
    database = Database()
    allowed_domains = ["www.stardewvalleywiki.com"]

    def __init_subclass__(cls, **kwargs):
        # 获取子类所在的模块信息
        caller_frame = inspect.currentframe().f_back
        caller_module = inspect.getmodule(caller_frame)
        caller_module_path = caller_module.__file__

        # 设置子类的 name 属性为文件名（不包含扩展名）
        cls.name = os.path.splitext(os.path.basename(caller_module_path))[0]

    def start_requests(self):
        url = Utils.find_url(self.url_path)
        yield scrapy.Request(url, callback=self._inner_parse)

    def _inner_parse(self, response):
        Utils.save_html(self.url_path, response.text)
        yield from self.parse(response)

    def parse(self, response):
        raise NotImplementedError("Subclasses must implement this method")