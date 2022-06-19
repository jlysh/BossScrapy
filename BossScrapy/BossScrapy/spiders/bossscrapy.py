# -*- coding: utf-8 -*-
import scrapy
import logging
from BossScrapy.items import BossscrapyItem

class BossscrapySpider(scrapy.Spider):
    name = 'bossscrapy'
    allowed_domains = ['zhipin.com']
    prefix_url = 'http://www.zhipin.com/'
    start_urls = [
        'http://www.zhipin.com/'
    ]

    def __init__(self, name=None, **kwargs):
        self.url = 'https://www.zhipin.com/c101190400/?page={pageNo}&ka=page-{pageNo}&query=数据分析'
        self.now_page = 1
        super().__init__(name, **kwargs)

    # @classmethod
    # def from_crawler(cls, crawler, *args, **kwargs):
    #     return super().from_crawler(crawler, *args, **kwargs)
    #
    def start_requests(self):
        yield scrapy.Request(self.url.format(pageNo=self.now_page), callback=self.parse,)


    def parse(self, response):
        global degree
        global company_persion
        logging.info(response)
        item = BossscrapyItem()
        if bool(response.xpath("//div[@class='job-list']")) == False:
            logging.info('cookie已失效')
            return
        for info in response.xpath("//div[@class='job-list']/ul//li"):
            url = self.prefix_url + ''.join(info.xpath(".//span[@class='job-name']/a/@href").extract())
            jobs = ''.join(info.xpath(".//span[@class='job-name']/a/text()").extract())
            work_address = info.xpath(".//span[@class='job-area']/text()").get()
            scalary = info.xpath(".//div[@class='job-limit clearfix']/span/text()").get()
            if len(info.xpath(".//div[@class='job-limit clearfix']/p/text()").extract()) == 2:
                experiences, degree = info.xpath(".//div[@class='job-limit clearfix']/p/text()").extract()
            else:
                experiences = ''.join(info.xpath(".//div[@class='company-text']/p/text()").extract())
            company = ''.join(info.xpath(".//div[@class='company-text']/h3/a/text()").extract())
            if len(info.xpath(".//div[@class='company-text']/p/text()").extract()) == 2:
                financing_condition,company_persion = info.xpath(".//div[@class='company-text']/p/text()").extract()
            else:
                financing_condition = ''.join(info.xpath(".//div[@class='company-text']/p/text()").extract())
            item['url'] = url
            item['jobs'] = jobs
            item['work_address'] = work_address
            item['scalary'] = scalary
            item['experiences'] = experiences
            item['degree'] = degree
            item['company'] = company
            item['financing_condition'] = financing_condition
            item['company_persion'] = company_persion
            yield item
        try:
            page = response.xpath("//div[@class='page']/a[last()]/@href").get()
            next_url = self.prefix_url + page
            if not page:
                logging.info("爬取完毕，退出爬虫")
                return
            else:
                logging.info("下一页地址：{}".format(next_url))
                yield scrapy.Request(next_url)

        except Exception as e:
            logging.info('爬虫异常，退出爬虫...{}'.format(e))
            return

