# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ArchdailyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    last_page = scrapy.Field()
    next_page = scrapy.Field()
    link_page = scrapy.Field()
    img_page = scrapy.Field()
    img_data = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_paths = scrapy.Field()
    # file_urls = scrapy.Field()
    # files = scrapy.Field()
    pass
