# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
    imdb_rating = scrapy.Field()

    cover = scrapy.Field()
    genres = scrapy.Field()
    plot = scrapy.Field()
    creator = scrapy.Field()
    stars = scrapy.Field()

    
