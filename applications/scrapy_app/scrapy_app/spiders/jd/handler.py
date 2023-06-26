from scrapy import Spider, Request


class JdItemSpider(Spider):
    name = 'jd_sku'

    def start_requests(self):
        # todo 改成从Django model里取
        urls = ['https://npcitem.jd.hk/100035412643.html']
        for url in urls:
            Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        pass