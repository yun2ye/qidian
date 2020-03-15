# -*- coding: utf-8 -*-
import scrapy
from qidian.items import QidianItem
import re



class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['qidian.com']
    start_urls = ['http://qidian.com/']
    item = QidianItem()

    # 获取目标小说详情页
    def parse(self, response):
        # 此处修改想要爬取的小说
        url_list = response.xpath('/html/body/div[1]/div[7]/div[1]/div/ul/li[1]/strong/a/@href').extract()
        for url in url_list:
            yield scrapy.Request(
                url='https:'+url,
                meta={'item': self.item},
                callback=self.parse_one
            )

    def parse_one(self, response):
        item = response.meta['item']
        item['text'] = []
        item['chapter_name'] = []
        item['name'] = response.xpath('/html/body/div/div[6]/div[1]/div[2]/h1/em/text()').extract_first()
        chapter_list = response.xpath('//*[@id="j-catalogWrap"]/div[2]/div/ul/li/a/@href').extract()
        yield scrapy.Request(
            url='https:' + chapter_list[0],
            meta={'item': self.item},
            callback=self.parse_two
        )

    def parse_two(self, response):
        item = response.meta['item']
        item['text_list'] = response.xpath('//*[@class="read-content j_readContent"]/p/text()').extract()
        item['chapter_name'].append(response.xpath('//*[@class="j_chapterName"]/span/text()').extract_first())
        url = response.xpath('//*[@id="j_chapterNext"]/@href').extract_first()
        nextChapterVip = re.findall(r'g_data.nextChapterVip = (\d);', response.text)[0]
        nextId = re.findall(r'nextId :(.*?),', response.text)[0]
        item['text'].append(' \n\n'.join(item['text_list']))
        if nextChapterVip == '0' and nextId != '-1':
            yield scrapy.Request(
                url='https:' + url,
                meta={'item': self.item},
                callback=self.parse_two
            )
        else:
            yield item






