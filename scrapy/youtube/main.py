# OUTPUT JSON: {id: [title, duration, channel, time, views, link]}

import subprocess
import json


if __name__ == '__main__':
    print('OK...................')
    with open('trends.json', 'w') as _:
        pass
    subprocess.run('scrapy runspider youtube_trends.py --output=trends.json -L WARNING')
    print('..............SUCCESS')

    with open('trends.json') as file:
        data = json.load(file)

    for i in data:
        print(i)
