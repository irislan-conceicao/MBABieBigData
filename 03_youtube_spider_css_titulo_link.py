scrapyimport scrapy

class YotubeSpider(scrapy.Spider):
    name = "Youtube"

    canal = 'videosimprovaveis'
    # canal = 'portadosfundos'

    start_urls = {
        'https://www.youtube.com/user/{}/videos'.format(canal)
    }

    def parse(self, response):

        elementos = response.css('.yt-ui-ellipsis-2')

        for elemento in elementos:
            yield {
                'titulo' : elemento.css('::text').extract_first(),
                'link' : 'https://youtube.com'+elemento.css('::attr("href")').extract_first()
            }
