
import subprocess
import json


if __name__ == '__main__':
    print('OK...................')
    with open('data.json', 'w') as _:
        pass
    subprocess.run('scrapy runspider spider.py --output=data.json -L WARNING')
    print('..............SUCCESS')

    with open('data.json') as file:
        data = json.load(file)

    for i in data:
        print(i)
