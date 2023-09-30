# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class WangyiPipeline:

    def __init__(self):
        self.file = open('wangyi_job.json', 'w')

    def process_item(self, item, spider):
        item = dict(item)
        # 1.将字典数据序列化
        job_data = json.dumps(item, ensure_ascii=False) + ',\n'
        # 2.将数据写入文件
        self.file.write(job_data)
        return item


    def __del__(self):
        self.file.close()