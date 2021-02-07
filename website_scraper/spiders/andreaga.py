import scrapy

class AndreagaSpider(scrapy.Spider):
    name = 'andreaga'
    start_urls = ['http://andreaga.com/blog/']

    def parse(self, response):
        for entry in response.css(".hentry"):
            title = entry.css(".entry-title")
            url = title.css("::attr(href)").extract_first()
            yield scrapy.Request(url, callback=self.parse_entry)
        if response.css(".nav-previous>a"):
            prev_page_url = response.css(".nav-previous>a::attr(href)").extract_first()
            yield scrapy.Request(prev_page_url)
    
    def parse_entry(self, response):
        pass