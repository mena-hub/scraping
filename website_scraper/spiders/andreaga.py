import scrapy


class AndreagaSpider(scrapy.Spider):
    name = 'andreaga'
    allowed_domains = ['andreaga.com/blog']
    start_urls = ['http://andreaga.com/blog/']

    def parse(self, response):
        pass
