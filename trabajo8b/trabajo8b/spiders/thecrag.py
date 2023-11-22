from pathlib import Path

import scrapy

class ThecragSpider(scrapy.Spider):
    name = "thecrag"
    #allowed_domains = ["www.thecrag.com"]

    def start_requests(self):
        urls = [
            "https://www.thecrag.com/en/climbing/germany",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")









'''


    url = ["https://www.thecrag.com/en/climbing/germany"]

    scrapy.Request(url=url)

    def parse(self, response):
        page = response.url
        print("*****************************************")
        print(page)
        print("*****************************************")
        print(response.body)
        Path("prueba.html").write_bytes(response.body)
        #self.log(f"Saved file {filename}")



from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
'''