import scrapy
import json


class Spider(scrapy.Spider):
    name = 'spider'
    start_urls = ['https://osu.ppy.sh/home/news']

    def parse(self, response):
        sel = scrapy.Selector(response)
        results = sel.xpath("//*[@id='json-sidebar']/text()").get()
        data = json.loads(results)
        for post in data['news_posts']:
            yield {post['id']: [post['author'], post['title'], post['updated_at'], str('https://osu.ppy.sh/home/news/' +
                                                                                       post['edit_url'][49:-3])]}
