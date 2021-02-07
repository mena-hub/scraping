import scrapy
import re

class AndreagaSpider(scrapy.Spider):
    name = 'andreaga'
    start_urls = ['http://andreaga.com/blog/']

    def __init__(self, limit_pages=None, *args, **kwargs):
        super(AndreagaSpider, self).__init__(*args, **kwargs)
        if limit_pages is not None:
            self.limit_pages = int(limit_pages)
        else:
            self.limit_pages = 0

    def parse(self, response):
        for entry in response.css(".hentry"):
            title = entry.css(".entry-title")
            url = title.css("::attr(href)").extract_first()
            yield scrapy.Request(url, callback=self.parse_entry)
        if response.css(".nav-previous>a"):
            prev_page_url = response.css(".nav-previous>a::attr(href)").extract_first()
            match = re.match(r".*\/page\/(\d+)\/", prev_page_url)
            prev_page_number = int(match.groups()[0])
            if prev_page_number <= self.limit_pages:
                yield scrapy.Request(prev_page_url)
    
    def parse_entry(self, response):
        pass