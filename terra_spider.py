import scrapy

class TerraSpider(scrapy.Spider):   
    name = 'terra_spider'
    start_urls = ['https://terra.com.br']
    
    def parse (self,response):
        titulos = response.css('.main-url::text')
        for titulo in titulos:
            conteudo = titulo.get().strip()
            if conteudo != "":
                yield{'titulo': conteudo}

