# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import time

class QidianPipeline(object):



    def process_item(self, item, spider):
        with open(file='{}.txt'.format(item['name']), mode='a', encoding='utf-8') as f:
            for i in range(len(item['chapter_name'])):
                f.write(item['chapter_name'][i])
                f.write('\n' * 2)
                f.write(item['text'][i])
            f.close()
        return item
