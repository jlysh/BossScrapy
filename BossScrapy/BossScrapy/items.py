# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BossscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company = scrapy.Field() #��˾����
    scalary = scrapy.Field() #н��
    jobs = scrapy.Field() #������λ
    experiences = scrapy.Field() #Ҫ��������
    degree = scrapy.Field() #Ҫ��ѧ��
    work_address = scrapy.Field() #��˾��ַ
    company_persion = scrapy.Field() #��˾����
    financing_condition = scrapy.Field() #�������
    url = scrapy.Field() #��Ƹ����