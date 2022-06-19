# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
from openpyxl import Workbook

class BossscrapyPipeline:
    def process_item(self, item, spider):
        logging.info('用excel处理返回的数据')
        line = [
            item['company'], item['scalary'], item['jobs'], item['experiences'], item['degree'],item['work_address'],
            item['company_persion'], item['financing_condition'],item['url']
                ]
        self.ws.append(line)
        self.wb.save(self.file_name)
        return item

    def __init__(self) -> None:
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(
            [
                '公司名称', '薪资',
                '工作岗位', '要求工作经验', '要求学历',
                '公司地址', '公司人数',
                '融资情况', '招聘链接'
            ]
        )
        self.file_name = "bossInfo.xlsx"

    def close_spider(self, spider):
        # 关闭
        self.wb.close()