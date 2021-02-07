import scrapy
import re
from website_scraper.items import WebsiteScraperItem

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
        item = WebsiteScraperItem(
            title = response.css("h1::text").extract_first(),
            author = response.css(".url::text").extract_first().strip(),
            published_at = response.css(".entry-date::attr(datetime)").extract_first(),
            content = self.extract_content(response),
            url = response.url
        )
        yield(item)

    def extract_content(self, response):
        paragraphs_texts = [
        p.css(" ::text").extract()
            for p in response.css(".entry-content>p")
        ]
        paragraphs = ["".join(p) for p in paragraphs_texts]
        paragraphs = [re.subn("\n", "", p)[0] for p in paragraphs]
        paragraphs = [p for p in paragraphs if p.strip() != ""]
        return "\n\n".join(paragraphs)