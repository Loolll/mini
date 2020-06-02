import subprocess


if __name__ == '__main__':
    print('OK...................')
    with open('news.json', 'w') as _:
        pass
    subprocess.run('scrapy runspider youtube_trends.py --output=news.json -L WARNING')
    print('..............SUCCESS')
