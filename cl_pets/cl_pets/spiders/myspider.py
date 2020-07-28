# //td[@class='views-field views-field-title active']//a

# Import key libraries 
import scrapy

# Class 
class MySpider(scrapy.Spider):
    name = "cl_pets"
    start_urls = ['https://www.towardssustainability.be/en/Investment-Product']
    
    
    def parse(self, response):
        for product in response.xpath("//td[@class='views-field views-field-title active']"):
            yield{
                'Product':product.xpath("a/text()").extract_first(),
                'Link':product.xpath("a").extract_first()
            }