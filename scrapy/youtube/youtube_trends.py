import scrapy
import json


class Spider(scrapy.Spider):
    name = 'spider'
    start_urls = ['https://youtube.com/feed/trending']

    def parse(self, response: scrapy.http.response.html.HtmlResponse):
        results = response.css("li.expanded-shelf-content-item-wrapper").css("div.yt-lockup-content")
        for i, result in enumerate(results):
            yield {i: [result.css('a.yt-uix-tile-link::text').get(),
                       result.css('span.accessible-description::text').get()[3:],
                       result.css('div.yt-lockup-byline').css('a.spf-link::text').get(),
                       *result.css('ul.yt-lockup-meta-info').css('li::text').getall(),
                       str('https://youtube.com' + result.css('a.yt-uix-tile-link::attr(href)').get())]}
