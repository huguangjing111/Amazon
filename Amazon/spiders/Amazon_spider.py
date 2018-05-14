# -*- coding: utf-8 -*-
import logging
import scrapy

from Amazon.items import AmazonItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'Amazon_spider'
    allowed_domains = ['amazon.cn']
    # 以分类页作为起始页
    start_urls = ['https://www.amazon.cn/gp/site-directory/ref=nav_shopall_btn/']
    num = 0

    def parse(self, response):
        # print u'[INFO] 正在解析分类页%s' % response.url
        # 商品小类链接
        href_list1 = response.xpath('//div[@id="cat3"]//div[@class="a-row"]/ul/li//a/@href').extract()
        href_list2 = response.xpath('//div[@id="cat3"]//div[@class="a-row"]/ul/li//a/@href').extract()
        href_list3 = response.xpath('//div[@id="cat3"]//div[@class="a-row"]/ul/li//a/@href').extract()
        href_list4 = response.xpath('//div[@id="cat3"]//div[@class="a-row"]/ul/li//a/@href').extract()
        href_list5 = response.xpath('//div[@id="cat3"]//div[@class="a-row"]/ul/li//a/@href').extract()
        href_list6 = response.xpath('//div[@id="cat3"]//div[@class="a-row"]/ul/li//a/@href').extract()
        href_list7 = response.xpath('//div[@id="cat3"]//div[@class="a-row"]/ul/li//a/@href').extract()
        href_list8 = response.xpath('//div[@id="cat3"]//div[@class="a-row"]/ul/li//a/@href').extract()
        href_list9 = response.xpath('//div[@id="cat3"]//div[@class="a-row"]/ul/li//a/@href').extract()
        href_list = href_list1 + href_list2 + href_list3 + href_list4 + href_list5 + href_list6 + href_list7 + href_list8 + href_list9
        print len(href_list)
        # 遍历取出每一个商品首页的链接
        for href in href_list:
            url = 'https://www.amazon.cn' + href
            print u'[INFO] 正在请求商品页%s' % url
            yield scrapy.Request(
                url=url,
                callback=self.parse_page,
            )

    def parse_page(self, response):
        print u'[INFO] 正在解析商品页%s' % response.url
        # 获取下一页链接
        link = response.xpath('//span[@class="pagnRA"]/a/@href')
        if link:
            next_link = 'https://www.amazon.cn' + link.extract_first()
            # print u'[INFO] 正在请求下一页商品页%s' % next_link
            yield scrapy.Request(
                url=next_link,
                callback=self.parse_page,
            )
        # 商品类型
        title = response.xpath('//span[@class="a-color-state a-text-bold"]//text()').extract_first()
        # 一页的商品列表
        # node_list1 = response.xpath('//div[@id="mainResults"]/ul/li')
        node_list2 = response.xpath('//div[@id="atfResults"]/ul/li')
        # node_list3 = response.xpath('//div[@id="btfResults"]/ul/li')
        node_list = node_list2
        print len(node_list)
        for node in node_list:
            item = AmazonItem()
            # 商品标题
            item['title'] = node.xpath('div/div[3]//h2/@data-attribute').extract_first()
            # print item['title']
            if not item['title']:
                item['title'] = node.xpath('div/div[3]//h2/@data-attribute').extract_first()
                if not item['title']:
                    item['title'] = node.xpath('div/div[4]//h2//text()').extract_first()

            # 商品类型
            item['type'] = title
            # 商品页url地址
            item['type_link'] = response.url

            # 图片地址
            item['img_url'] = node.xpath('div/div[2]//img/@src').extract_first()
            # print item['img_url']

            # 商品链接
            item['good_link'] = node.xpath('div/div[3]//a/@href').extract_first()

            # 商品logo
            item['logo'] = node.xpath('div/div[3]/div[last()]/span/text()').extract_first()

            # 商品价格
            price = node.xpath('div/div[5]/div[1]//span/text()').extract_first()
            if not price:
                price = node.xpath('div/div[6]/div[1]//span/text()').extract_first()
            item['price'] = price
            # print price
            if item['title'] == '[广告]':
                with open('title.py', 'a') as f:
                    f.write(response.url)
                    f.write(';\n')
                    f.write(price)
                    f.write(';\n')

            # 商品评价星级
            rank = node.xpath('div/div[last()]//a/i[1]//text()').extract_first()
            if not rank:
                rank = u'暂无星级评分'
            item['rank'] = rank
            yield item