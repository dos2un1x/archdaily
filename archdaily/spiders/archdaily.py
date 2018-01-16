# coding:utf-8
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
import os
from scrapy_splash import SplashRequest
import json
import re

class zhuoku(scrapy.Spider):
    name = "archdaily"
    allowed_domain = ["archdaily.cn"]
    start_urls = ["https://www.archdaily.cn/cn/search/projects"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        sel = Selector(response)
        for first_urls in sel.xpath('//*[@id="search-results"]/div[2]/ul/li[@class="afd-search-list__item"]/a/@href').extract():
            first_url = response.urljoin(first_urls)
            print "first url is: " + first_url
            self.logger.info("first url is: %s", first_url)
            yield SplashRequest(first_url, self.second_parse, args={'wait': 0.5})

    def second_parse(self, response):
        sel = Selector(response)
        for second_urls in sel.xpath('//*[@class="js-image-size__link nr-image nr-picture"]/@href').extract():
            second_url = response.urljoin(second_urls)
            print "second url is: " + second_url
            self.logger.info("second url is: %s", second_url)
            yield SplashRequest(second_url, self.third_parse, args={'wait': 0.5})

    def third_parse(self, response):
        sel = Selector(response)
        base_path = 'C:\Users\Administrator\PycharmProjects\pic\\'
        for path_name in sel.xpath('/html/head/title/text()').extract():
            new_name = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "", path_name)
            new_path = base_path + new_name
            if not os.path.exists(new_path):
                os.mkdir(new_path)
        for data in sel.xpath('//*[@id="gallery-items"]/@data-images').extract():
            utf8string = data.encode("utf-8")
            f = open(new_path + '\data.json', mode='a')
            f.write(utf8string + '\n')
            f.close()
            js = json.loads(data, encoding='utf-8')
            #strjs = json.dumps(js, ensure_ascii=False)
            for values in js:
                d = open(new_path + '\imgurl.txt', mode='a')
                d.write(values['url_large'] + '\n')
                f.close()
