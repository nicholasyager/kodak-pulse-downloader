import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy import Request

from items import ImageItem


class KodakPulseSpider(scrapy.Spider):
    name = "KodakPulseSpider"
    base_url = "http://www.kodakpulse.com/"
    authentication_url = "https://www.kodakpulse.com/"

    page = 1

    def start_requests(self):
        """This function is called before crawling starts."""

        # Login
        return [
            scrapy.FormRequest(self.authentication_url,
                               formdata={
                                   'username': self.username,  # Set to the username
                                   'password': self.password  # Set to the password
                               },
                               method="post",
                               callback=self.logged_in)]

    def logged_in(self, response):
        return scrapy.Request(self.base_url + '/Frame/AllPictures')

    def parse(self, response):
        images = response.css('img').xpath('@src').extract()
        for image in images:
            if "cloudfront" in image:
                image = image.replace('~t~', '~a~')
                yield ImageItem(image_urls=[image])

        print(len(images))
        if len(images) < 48:
            return

        self.page += 1
        yield scrapy.Request(self.base_url + '/Frame/AllPictures?p=' + str(self.page), callback=self.parse)
