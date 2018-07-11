# coding:utf-8
import scrapy


class testSpider(scrapy.Spider):
    name = 'test'
    start_urls = [
        'http://www.mafengwo.cn/travel-scenic-spot/mafengwo/10184.html'
    ]

    def parse(self, response):
        print(response.body)
    # def parse(self, response):
    #     for title in response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "item-title", " " ))]//a'):
    #         yield scrapy.Request('http:' + title.xpath('@href').extract()[0], self.detail)
    #
    # def detail(self, response):
    #     data = BeautifulSoup(response.body, 'lxml')
    #     area = data.select('#J_Property > h1')
    #     print(area[0].get_text())
