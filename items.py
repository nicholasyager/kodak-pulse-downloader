import scrapy


class ImageItem(scrapy.Item):

    image_urls = scrapy.Field()
    images = scrapy.Field()