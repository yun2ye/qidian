# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank_name = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
    word_number = scrapy.Field()
    recommended_number = scrapy.Field()
    introduction = scrapy.Field()
    text = scrapy.Field()
    text_list = scrapy.Field()
    chapter_name = scrapy.Field()
