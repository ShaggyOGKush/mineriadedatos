from datetime import datetime
import scrapy

class economicindicators(scrapy.Spider):
    name='e_indicators'
    start_urls = [
        'https://www.dane.gov.co/index.php/indicadores-economicos'
    ] 
    custom_settings = {
        'FEED_URI': 'indicadores_economicos.cvs',
        'FEED FORMAT': 'cvs',
        'ROBOTSTXT_OBEY': True,
        'FEED_EXPORT_ENCODING' :'utf-8'
    }   

    def parse(self, response):
        indicators = response.xpath('//section[contains(@class,"article-content") and @itemprop="articleBody"]//table//h2//strong/text()').getall()
        values = response.xpath('//section[contains(@class,"article-content") and @itemprop="articleBody"]//table//h1//text()').getall()

        for ind, val in zip(indicators, values):
            info = {
                'indicador':ind,
                'valor': val,
                'fecha': datetime.today().date()
            }                                       
            yield info    