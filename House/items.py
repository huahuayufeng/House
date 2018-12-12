# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    loupanname = scrapy.Field()
    price=scrapy.Field()
    wuyetype=scrapy.Field()
    kaifashang=scrapy.Field()
    area1=scrapy.Field()
    area2 = scrapy.Field()
    Loupanadd=scrapy.Field()
