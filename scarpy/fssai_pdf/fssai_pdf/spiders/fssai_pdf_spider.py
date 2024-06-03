import scrapy


class FssaiPdfSpiderSpider(scrapy.Spider):
    name = "fssai_pdf_spider"
    allowed_domains = ["fssai.gov.in"]
    start_urls = ["https://fssai.gov.in"]

    def parse(self, response):
        pass
