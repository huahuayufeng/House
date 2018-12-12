# -*- coding: utf-8 -*-
import scrapy
from House.items import HouseItem

class AnjukehouseSpider(scrapy.Spider):
    name = 'anjukeHouse'
    allowed_domains = ['chengdu.anjuke.com']
    #start_urls = ['http://chengdu.anjuke.com/']

    def start_requests(self):
        for i in range(400000,500000):
            start_urls='https://cd.fang.anjuke.com/loupan/canshu-{0}.html?from=loupan_tab'.format(str(i))
            yield scrapy.Request(start_urls,callback=self.parse)

    def parse(self, response):
        body=response.xpath("//div[@class='can-left']")
        #print body.extract()
        item1=HouseItem()
        for item in body:
            loupanname=item.xpath(".//div[@class='can-border']/ul/li[1]//a/text()").extract()
            price = item.xpath(".//div[@class='can-border']/ul/li[2]//div[@class='des']/text()").extract()
            wuyetype = item.xpath(".//div[@class='can-border']/ul/li[3]//div[@class='des']/text()").extract()
            kaifashang = item.xpath(".//div[@class='can-border']/ul/li[4]//div[@class='des']/a/text()").extract()
            area1=item.xpath(".//div[@class='can-border']/ul/li[5]//div[@class='des']/a[1]/text()").extract()
            area2 = item.xpath(".//div[@class='can-border']/ul/li[5]//div[@class='des']/a[2]/text()").extract()
            Loupanadd = item.xpath(".//div[@class='can-border']/ul/li[6]//div[@class='des']/text()").extract()
            print loupanname[0].replace(' ',''),\
                price[0].replace(' ',''),\
                wuyetype[0].replace(' ','')+'\n',\
                kaifashang[0].replace(' ','')+'\n',\
                area1[0].replace(' ','')+'-'+area2[0].replace(' ','')+'\n', \
                Loupanadd[0].replace(' ', '')+'\n'
            item1['loupanname']=loupanname[0].replace(' ','')
            item1['price'] = price[0].replace(' ', '')
            item1['wuyetype'] = wuyetype[0].replace(' ', '')
            item1['kaifashang'] = kaifashang[0].replace(' ', '')
            item1['area1'] = area1[0].replace(' ', '')
            item1['area2'] = area2[0].replace(' ', '')
            item1['Loupanadd'] = Loupanadd[0].replace(' ', '')
            yield item1





