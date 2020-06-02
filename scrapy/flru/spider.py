import scrapy
import json


class Spider(scrapy.Spider):
    name = 'spider'
    start_urls = ['https://fl.ru/projects']

    def parse(self, response: scrapy.http.response.html.HtmlResponse):
        results = response.css("div.b-post_padbot_15")
        for result in results:
            in_script = result.css('script::text').getall()
            secure = 'Безопасная сделка' in in_script[0]
            price = (in_script[0][497:-10] if secure else in_script[0][183:-10]).replace('&nbsp', '').replace(';', '')
            text = in_script[1][142:-78]
            html_string = in_script[2][17:-3]
            type_ = 'Проект' if 'Проект' in html_string else 'Вакансия' if 'Вакансия' in html_string else 'Конкурс'

            yield {bool(result.css('img.b-pic_margtop_1')): {'title': result.css('a.b-post__link::text').get(),
                                                             'secure': secure, 'price': price,
                                                             'text': text, 'type': type_}
                   }


