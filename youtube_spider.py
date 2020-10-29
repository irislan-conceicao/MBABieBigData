import scrapy
from scrapy.utils.response import open_in_browser

class YoutubeSpider(scrapy.Spider):   
    name = 'youtube_spider'
    start_urls = ['https://www.youtube.com/c/floremanu/videos']
    
    def parse (self,response):
        open_in_browser(response)
        titulos = response.css('.yt-simple-endpoint::text')
        for titulo in titulos:
            conteudo = titulo.get().strip()
            if conteudo != "":
                yield{'titulo': conteudo}

