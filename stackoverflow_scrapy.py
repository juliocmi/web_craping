from scrapy.item import Field, Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class Question(Item):
    id = Field()
    question = Field()
    #description = Field()

class StackOverflowSpider(Spider):
    name = "MyFirstSpider"
    custom_settings = {
        "user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/126.0.6478.114 Safari/17.4.1"
        }
    
    start_urls = ['https://stackoverflow.com/questions']

    def parse(self, response):
        sel = Selector(response)
        questions = sel.xpath('//div[@id="questions"]//div[starts-with(@id, "question-summary-")]')
        
        for question in questions:
            item = ItemLoader(Question(), question)
            item.add_xpath('question', './/h3/a/text()')
            #item.add_xpath('description', './/div[@class="s-post-summary--content-excerpt"]/text()')
            item.add_value('id', 1)

            yield item.load_item()