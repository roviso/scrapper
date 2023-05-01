# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RatopatiScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    heading = scrapy.Field()
    content = scrapy.Field()
    label = scrapy.Field()
    date = scrapy.Field()
    comments = scrapy.Field()
    shares = scrapy.Field()
    pass
