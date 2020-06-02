# url = 'https://dotabuff.com/players/208035041'
import subprocess
import json


if __name__ == '__main__':
    base = """

import scrapy
import json


class Spider(scrapy.Spider):
    name = 'spider'
    start_urls = [url]

    def parse(self, response: scrapy.http.response.html.HtmlResponse):
        # Popular heroes parser:
        results = response.css('div.heroes-overview').css('div.r-row')
        for i, result in enumerate(results):
            hero = result.css('div.r-icon-text').css('div.r-body').css('div.r-none-mobile').css('a::text').get()
            temp = result.css('div.r-10')
            matches = temp[0].css('div.r-body::text').get()
            winrate = temp[1].css('div.r-body::text').get()
            kda = temp[2].css('div.r-body::text').get()
            temp = result.css('div.r-175')
            try:
                role = temp[0].css('div.r-body').css('div.group').css('span::text').get()
            except IndexError:
                role = 'Undefined'

            try:
                line = temp[1].css('div.r-body').css('div.group').css('span::text').get()
            except IndexError:
                line = 'Undefined'

            yield {i: {'hero': hero, 'matches': matches, 'winrate': winrate, 'KDA': kda, 'role': role, 'line': line}}
"""
    url = f'url = "https://dotabuff.com/players/{int(input())}"'
    with open('spider.py', 'w') as spider:
        spider.write(str(url + base))

    with open('data.json', 'w') as _:
        pass
    subprocess.run('scrapy runspider spider.py --output=data.json -L WARNING')
    try:
        with open('data.json') as file:
            data = json.load(file)

        for i in data:
            print(i)
    except:
        pass
