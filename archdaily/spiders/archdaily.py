# coding:utf-8
import scrapy
from scrapy.selector import Selector
from scrapy_splash import SplashRequest
from ..items import ArchdailyItem
import os
import json
import re

class archdaily(scrapy.Spider):
    name = "archdaily"
    allowed_domain = ["archdaily.cn"]
    start_urls = ["https://www.archdaily.cn/cn/search/projects"]

    def start_requests(self):
        for start_url in self.start_urls:
            yield SplashRequest(start_url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        sel = Selector(response)
        item = ArchdailyItem()
        item['last_page'] = sel.xpath('//div[@class="pagination"]/a[@class="last"]/@href').extract_first()
        all_num = int(item['last_page'].split('=')[1]) + 1
        for next_num in range(1, 2):
            link_url = item['last_page'].split('=')[0] + str(next_num)
            item['next_page'] = response.urljoin(link_url)
            print "next page is: " + item['next_page']
            yield SplashRequest(item['next_page'], self.next_pages, args={'wait': 0.5})

    def next_pages(self, response):
        sel = Selector(response)
        item = ArchdailyItem()
        for link_page in sel.xpath('//li[@class="afd-search-list__item"]/a/@href').extract():
            item['link_page'] = response.urljoin(link_page)
            print "link page is: " + item['link_page']
            yield SplashRequest(item['link_page'], self.link_pages, args={'wait': 0.5})

    def link_pages(self, response):
        sel = Selector(response)
        item = ArchdailyItem()
        for img_page in sel.xpath('//*[@class="js-image-size__link nr-image nr-picture"]/@href').extract():
            item['img_page'] = response.urljoin(img_page)
            print "img page is: " + item['img_page']
            yield SplashRequest(item['img_page'], self.img_urls, args={'wait': 0.5})

    def img_urls(self, response):
        sel = Selector(response)
        item = ArchdailyItem()
        for img_data in sel.xpath('//*[@id="gallery-items"]/@data-images').extract():
            js = json.loads(img_data, encoding='utf-8')
            for img_urls in js:
                item['img_url'] = img_urls['url_large']
                print "img url is: " + item['img_url']


        # for item['url'] in sel.xpath('//li[@class="afd-search-list__item"]/a/@href').extract():
        #     first_url = response.urljoin(item['url'])
        #     print "first url is: " + first_url
        #     self.logger.info("first url is: %s", first_url)
        #     #yield SplashRequest(first_url, self.second_parse, args={'wait': 0.5})

        # for item['page'] in sel.xpath('//div[@class="pagination"]/a[@class="next"]/@href').extract():
        #     next_page = response.urljoin(item['page'])
        #     print "next page is: " + next_page
        #     self.logger.info("next page is: %s", next_page)
        #     yield SplashRequest(next_page, self.parse, args={'wait': 0.5})



    # def second_parse(self, response):
    #     sel = Selector(response)
    #     for second_urls in sel.xpath('//*[@class="js-image-size__link nr-image nr-picture"]/@href').extract():
    #         second_url = response.urljoin(second_urls)
    #         print "second url is: " + second_url
    #         self.logger.info("second url is: %s", second_url)
    #         yield SplashRequest(second_url, self.third_parse, args={'wait': 0.5})
    #
    # def third_parse(self, response):
    #     sel = Selector(response)
    #     base_path = 'C:\Users\Administrator\PycharmProjects\pic\\'
    #     for path_name in sel.xpath('/html/head/title/text()').extract():
    #         new_name = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "", path_name)
    #         new_path = base_path + new_name
    #         if not os.path.exists(new_path):
    #             os.mkdir(new_path)
    #     for data in sel.xpath('//*[@id="gallery-items"]/@data-images').extract():
    #         utf8string = data.encode("utf-8")
    #         f = open(new_path + '\data.json', mode='a')
    #         f.write(utf8string + '\n')
    #         f.close()
    #         js = json.loads(data, encoding='utf-8')
    #         #strjs = json.dumps(js, ensure_ascii=False)
    #         for values in js:
    #             d = open(new_path + '\imgurl.txt', mode='a')
    #             d.write(values['url_large'] + '\n')
    #             f.close()
