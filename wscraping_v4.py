# Title: El Universo Website
# Date : 23/Jul/24
# Script : Ing. Julio Martínez
#-------------------------------------------------
# Objetive: Create an script to stract information
# about El Universo website, using Scrapy methods.
#--------------------------------------------------
from typing import Any
from scrapy.http.response import Response
from scrapy.item import Field, Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class News(Item):
    title = Field()
    description = Field()

class ElUniversoSpider(Spider):
    name = "MySecondSpider"
    custom_settings = {
        "user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/126.0.6478.114 Safari/17.4.1"
    }

    start_url = ["https://www.eluniverso.com/deportes"]

    def parse(self, response):
        sel  = Selector(response)
        news = sel.xpath('//div[@class="card-content | space-y-1 "]/div')
        for noticia in news:
            item = ItemLoader(News(), noticia)
            item.add_xpath('titular', './/h2/a/text()')
            item.add_xpath('description', './/p/text()')
            yield item.load_item()