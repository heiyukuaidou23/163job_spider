# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class WangyiPipeline(object):

    def open_spider(self, spider):
        if spider.name == 'job':
            self.file = open('wangyi_job.json', 'w')

    def process_item(self, item, spider):
        if spider.name == 'job':
            item = dict(item)
            # 1.将字典数据序列化
            job_data = json.dumps(item, ensure_ascii=False) + ',\n'
            # 2.将数据写入文件
            self.file.write(job_data)
            return item

    def close_spider(self, spider):
        if spider.name == 'job':
            self.file.close()


class WangyiSimplePipeline(object):

    def open_spider(self, spider):
        if spider.name == 'job_simple':
            self.file = open('wangyi_simple_job.json', 'w')

    def process_item(self, item, spider):
        if spider.name == 'job_simple':
            item = dict(item)
            # 1.将字典数据序列化
            job_data = json.dumps(item, ensure_ascii=False) + ',\n'
            # 2.将数据写入文件
            self.file.write(job_data)
            return item

    def close_spider(self, spider):
        if spider.name == 'job_simple':
            self.file.close()
