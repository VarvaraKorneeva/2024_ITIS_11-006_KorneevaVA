import re

import scrapy
from bs4 import BeautifulSoup


URL = 'https://pythonru.com/primery/nahozhdenie-delitelej-chisla-s-pomoshhju-python'


def get_main_url(url):
    if url[-1] == '/':
        return url[:-1]
    return url


class QuotesSpider(scrapy.Spider):
    name = 'spider'
    start_urls = [URL]
    custom_settings = {
        'FEED_EXPORT_FORMAT': 'utf-8',
        # 'CLOSESPIDER_PAGECOUNT': 300
    }

    def __init__(self):
        scrapy.Spider.__init__(self)
        self.index = 1

    @staticmethod
    def get_full_link(link):
        if link[:4] != 'http':
            return get_main_url(URL) + link
        return link

    def parse(self, response):
        with open('../../index.txt', 'r') as f:
            lines = f.read().splitlines()
            written_links = [x.split(' ')[1] for x in lines]
        # check stop condition
        if self.index > 100:
            return

        # check unique link
        if response.url not in written_links and response.status == 200:
            # get all links and scrap it
            links = response.xpath('//a/@href').getall()
            for link in links:
                full_link = self.get_full_link(link)
                if full_link not in written_links:
                    yield scrapy.Request(url=full_link, callback=self.parse)

            # get page's content, remove html tags, check 1000 rus words, write page's content in files
            content = response.body
            soup = BeautifulSoup(content, 'html.parser')
            data = soup.get_text(' ', strip=True)
            text = re.findall(r'[А-я]+', data)
            if len(text) >= 1000:
                with open(f'../../pages/{self.index}.txt', 'w') as c:
                    for word in text:
                        c.write(word + ' ')

                # write link to index file with index
                with open('../../index.txt', 'a') as f:
                    f.write(str(self.index) + ' ' + response.url + '\n')
                    self.index += 1
