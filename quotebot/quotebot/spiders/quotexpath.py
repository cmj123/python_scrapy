# Import key libraries
import scrapy

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = ["http://quotes.toscrape.com/"]
    
    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                'text':quote.xpath("span/text()").extract_first(),
                'author':quote.xpath("span//small/text()").extract_first(),
                'tags':quote.xpath("div/a/text()").extract()
            }