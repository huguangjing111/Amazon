# -*- coding: utf-8 -*-
import scrapy

from Amazon.items import AmazonItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'Amazon_spider'
    allowed_domains = ['amazon.cn']
    start_urls = ['https://www.amazon.cn/gp/site-directory/ref=nav_shopall_btn/']
    # start_urls = ['https://fls-cn.amazon.cn/1/batch/1/OE/']
    cookies = {
        "x-wl-uid": "1cspaYJf/9oon/7aznDK0OLUpYi4mlnLM4UoC1h6MpmX4pdBjukQhDjECF4rDXpibTF0GmewAl7s=",
        "s_nr": "1525507157532-New", " s_vnum": "1957507157538%26vn%3D1", " s_dslv": "1525507157544",
        "csm-hit": "PX5TFHABTR4YKRNBJSAC+s-S73FC17KG9CKXPR1D294|1525506679578&tb:s-DZKQ9F22R0ZTQNYH7HPF|1525594678100&adb:adblk_no",
        "session-token": "9u3r24fg + GblQHnlYitsbmY43D / 6p8mxn3AX / 5S7XqyM3D3d + 6r2UmJoYMRbOYYBrx9NJ1fA / 5uLr1faQmfv5enCjlK3hI8ofRDGN + UmWVg3duChDvcOP7bdS2i6Lrld / Cdc218KLdkJ4l8R0Hg33xe9LBXlbxTz9Ri3NTfXo4RjPacWwsVWBBkItVnR3R / dN3qH / WIL1CCVyI + xNfl3Fa32XYXhlivN / 4XAj + MPhYjKlRBSOGffwg == ",
        "ubid - acbcn": "457 - 4181431 - 9552845",
        "session - id - time": "2082729601l",
        "session - id": "457 - 7944366 - 4993446"
    }
    headers = {
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        # "Accept-Encoding": "gzip, deflate, sdch",
        # "Accept-Language": "zh-CN,zh;q=0.8",
        # "Connection": "keep-alive",
        "Host": "www.amazon.cn",
        # "Upgrade-Insecure-Requests": "1",
        # "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    data = {"rid": "DZKQ9F22R0ZTQNYH7HPF", "sid": "457-7944366-4993446", "mid": "AAHKV2X7AFYLW", "sn": "www.amazon.cn",
            "reqs": [{"cel": {"w": 1038, "h": 5331, "t": 332960, "k": "doi"}},
                     {"cel": {"w": 1053, "h": 506, "x": 0, "y": 0, "t": 332960, "k": "vpi"}}, {
                         "cel": {"n": "result_0", "w": 267.984375, "h": 641, "d": 0, "x": 224, "y": 205, "t": 333041,
                                 "k": "ewi"}}, {
                         "cel": {"n": "result_1", "w": 267.984375, "h": 641, "d": 0, "x": 491.984375, "y": 205,
                                 "t": 333041, "k": "ewi"}}, {
                         "cel": {"n": "result_2", "w": 267.984375, "h": 641, "d": 0, "x": 759.96875, "y": 205,
                                 "t": 333041, "k": "ewi"}}, {
                         "cel": {"n": "result_3", "w": 267.984375, "h": 495, "d": 0, "x": 224, "y": 846, "t": 333041,
                                 "k": "ewi"}}, {
                         "cel": {"n": "result_4", "w": 267.984375, "h": 495, "d": 0, "x": 491.984375, "y": 846,
                                 "t": 333041, "k": "ewi"}}, {
                         "cel": {"n": "result_5", "w": 267.984375, "h": 495, "d": 0, "x": 759.96875, "y": 846,
                                 "t": 333041, "k": "ewi"}}, {
                         "cel": {"n": "result_6", "w": 267.984375, "h": 617, "d": 0, "x": 224, "y": 1341, "t": 333041,
                                 "k": "ewi"}}, {
                         "cel": {"n": "result_7", "w": 267.984375, "h": 617, "d": 0, "x": 491.984375, "y": 1341,
                                 "t": 333041, "k": "ewi"}}, {
                         "cel": {"n": "result_8", "w": 267.984375, "h": 617, "d": 0, "x": 759.96875, "y": 1341,
                                 "t": 333041, "k": "ewi"}}, {
                         "cel": {"n": "result_9", "w": 267.984375, "h": 617, "d": 0, "x": 224, "y": 1958, "t": 333041,
                                 "k": "ewi"}}, {
                         "cel": {"n": "result_10", "w": 267.984375, "h": 617, "d": 0, "x": 491.984375, "y": 1958,
                                 "t": 333041, "k": "ewi"}}, {
                         "cel": {"n": "result_11", "w": 267.984375, "h": 617, "d": 0, "x": 759.96875, "y": 1958,
                                 "t": 333041, "k": "ewi"}}, {
                         "cel": {"n": "result_12", "w": 267.984375, "h": 532, "d": 0, "x": 224, "y": 2575, "t": 333041,
                                 "k": "ewi"}}, {
                         "cel": {"n": "result_13", "w": 267.984375, "h": 532, "d": 0, "x": 491.984375, "y": 2575,
                                 "t": 333041, "k": "ewi"}}, {
                         "cel": {"n": "result_14", "w": 267.984375, "h": 532, "d": 0, "x": 759.96875, "y": 2575,
                                 "t": 333041, "k": "ewi"}}, {
                         "cel": {"n": "result_15", "w": 267.984375, "h": 480, "d": 0, "x": 224, "y": 3107, "t": 333041,
                                 "k": "ewi"}}, {
                         "cel": {"n": "result_16", "w": 267.984375, "h": 480, "d": 0, "x": 491.984375, "y": 3107,
                                 "t": 333041, "k": "ewi"}}, {
                         "cel": {"n": "result_17", "w": 267.984375, "h": 480, "d": 0, "x": 759.96875, "y": 3107,
                                 "t": 333041, "k": "ewi"}}, {
                         "cel": {"n": "result_18", "w": 267.984375, "h": 548, "d": 0, "x": 224, "y": 3587, "t": 333041,
                                 "k": "ewi"}}, {
                         "cel": {"n": "result_19", "w": 267.984375, "h": 548, "d": 0, "x": 491.984375, "y": 3587,
                                 "t": 333041, "k": "ewi"}}, {
                         "cel": {"n": "result_20", "w": 267.984375, "h": 548, "d": 0, "x": 759.96875, "y": 3587,
                                 "t": 333041, "k": "ewi"}}, {
                         "cel": {"n": "result_21", "w": 267.984375, "h": 532, "d": 0, "x": 224, "y": 4135, "t": 333041,
                                 "k": "ewi"}}, {
                         "cel": {"n": "result_22", "w": 267.984375, "h": 532, "d": 0, "x": 491.984375, "y": 4135,
                                 "t": 333041, "k": "ewi"}}, {
                         "cel": {"n": "result_23", "w": 267.984375, "h": 532, "d": 0, "x": 759.96875, "y": 4135,
                                 "t": 333041, "k": "ewi"}},
                     {"csmcount": {"counter": "primeMetric-AjaxCallCount", "value": 1, "t": 333508}},
                     {"csmcount": {"counter": "primeMetric-AjaxLatency", "value": 168, "t": 333508}}, {
                         "cel": {"k": "mmm1",
                                 "e": [{"x": 726, "y": 436, "t": 331831}, {"x": 768, "y": 255, "t": 332075},
                                       {"x": 768, "y": 173, "t": 332119}, {"x": 742, "y": 61, "t": 332190},
                                       {"x": 746, "y": 7, "t": 332263}, {"x": 821, "y": 2, "t": 333040},
                                       {"x": 868, "y": 23, "t": 333108}, {"x": 839, "y": 42, "t": 333256},
                                       {"x": 1018, "y": 43, "t": 333419}], "min": 49, "max": 304, "avg": 132}},
                     {"cel": {"w": 1037, "h": 5331, "t": 334967, "k": "doi"}},
                     {"cel": {"w": 928, "h": 506, "x": 0, "y": 0, "t": 335391, "k": "vpi"}},
                     {"cel": {"w": 1000, "h": 5331, "t": 335660, "k": "doi"}}, {
                         "cel": {"n": "result_0", "w": 255.328125, "h": 641, "d": 0, "x": 224, "y": 205, "t": 335603,
                                 "k": "ewi"}}, {
                         "cel": {"n": "result_1", "w": 255.328125, "h": 641, "d": 0, "x": 479.328125, "y": 205,
                                 "t": 335603, "k": "ewi"}}, {
                         "cel": {"n": "result_2", "w": 255.328125, "h": 641, "d": 0, "x": 734.65625, "y": 205,
                                 "t": 335603, "k": "ewi"}}, {
                         "cel": {"n": "result_3", "w": 255.328125, "h": 495, "d": 0, "x": 224, "y": 846, "t": 335603,
                                 "k": "ewi"}}, {
                         "cel": {"n": "result_4", "w": 255.328125, "h": 495, "d": 0, "x": 479.328125, "y": 846,
                                 "t": 335603, "k": "ewi"}}, {
                         "cel": {"n": "result_5", "w": 255.328125, "h": 495, "d": 0, "x": 734.65625, "y": 846,
                                 "t": 335603, "k": "ewi"}}, {
                         "cel": {"n": "result_6", "w": 255.328125, "h": 617, "d": 0, "x": 224, "y": 1341, "t": 335603,
                                 "k": "ewi"}}, {
                         "cel": {"n": "result_7", "w": 255.328125, "h": 617, "d": 0, "x": 479.328125, "y": 1341,
                                 "t": 335603, "k": "ewi"}}, {
                         "cel": {"n": "result_8", "w": 255.328125, "h": 617, "d": 0, "x": 734.65625, "y": 1341,
                                 "t": 335603, "k": "ewi"}}, {
                         "cel": {"n": "result_9", "w": 255.328125, "h": 617, "d": 0, "x": 224, "y": 1958, "t": 335603,
                                 "k": "ewi"}}, {
                         "cel": {"n": "result_10", "w": 255.328125, "h": 617, "d": 0, "x": 479.328125, "y": 1958,
                                 "t": 335603, "k": "ewi"}}, {
                         "cel": {"n": "result_11", "w": 255.328125, "h": 617, "d": 0, "x": 734.65625, "y": 1958,
                                 "t": 335603, "k": "ewi"}}, {
                         "cel": {"n": "result_12", "w": 255.328125, "h": 532, "d": 0, "x": 224, "y": 2575, "t": 335603,
                                 "k": "ewi"}}, {
                         "cel": {"n": "result_13", "w": 255.328125, "h": 532, "d": 0, "x": 479.328125, "y": 2575,
                                 "t": 335603, "k": "ewi"}}, {
                         "cel": {"n": "result_14", "w": 255.328125, "h": 532, "d": 0, "x": 734.65625, "y": 2575,
                                 "t": 335603, "k": "ewi"}}, {
                         "cel": {"n": "result_15", "w": 255.328125, "h": 480, "d": 0, "x": 224, "y": 3107, "t": 335603,
                                 "k": "ewi"}}, {
                         "cel": {"n": "result_16", "w": 255.328125, "h": 480, "d": 0, "x": 479.328125, "y": 3107,
                                 "t": 335603, "k": "ewi"}}, {
                         "cel": {"n": "result_17", "w": 255.328125, "h": 480, "d": 0, "x": 734.65625, "y": 3107,
                                 "t": 335603, "k": "ewi"}}, {
                         "cel": {"n": "result_18", "w": 255.328125, "h": 548, "d": 0, "x": 224, "y": 3587, "t": 335603,
                                 "k": "ewi"}}, {
                         "cel": {"n": "result_19", "w": 255.328125, "h": 548, "d": 0, "x": 479.328125, "y": 3587,
                                 "t": 335603, "k": "ewi"}}, {
                         "cel": {"n": "result_20", "w": 255.328125, "h": 548, "d": 0, "x": 734.65625, "y": 3587,
                                 "t": 335603, "k": "ewi"}}, {
                         "cel": {"n": "result_21", "w": 255.328125, "h": 532, "d": 0, "x": 224, "y": 4135, "t": 335603,
                                 "k": "ewi"}}, {
                         "cel": {"n": "result_22", "w": 255.328125, "h": 532, "d": 0, "x": 479.328125, "y": 4135,
                                 "t": 335603, "k": "ewi"}}, {
                         "cel": {"n": "result_23", "w": 255.328125, "h": 532, "d": 0, "x": 734.65625, "y": 4135,
                                 "t": 335603, "k": "ewi"}},
                     {"cel": {"w": 639, "h": 506, "x": 0, "y": 0, "t": 335706, "k": "vpi"}},
                     {"cel": {"w": 560, "h": 506, "x": 0, "y": 0, "t": 336347, "k": "vpi"}},
                     {"cel": {"k": "mmm1", "e": [{"x": 568, "y": 91, "t": 335617}], "min": 20, "max": 304, "avg": 109}},
                     {"csmcount": {"counter": "QF-N:SN:QN:TN", "value": 1, "t": 339344}},
                     {"csmcount": {"counter": "cel.PDM.TotalExecutions", "value": 672, "t": 339347}},
                     {"csmcount": {"counter": "cel.VPI.TotalExecutions", "value": 5, "t": 339347}},
                     {"csmcount": {"counter": "cel.VPI.TotalExecutionTime", "value": 0, "t": 339347}},
                     {"csmcount": {"counter": "cel.VPI.AverageExecutionTime", "value": 0, "t": 339347}},
                     {"csmcount": {"counter": "cel.widgets.batchesProcessed", "value": 191, "t": 339348}},
                     {"cel": {"k": "mmm1", "e": [{"x": 568, "y": 91, "t": 339348}], "min": 0, "max": 304, "avg": 91}},
                     {"cel": {"k": "hrt", "t": 339348}}, {"cel": {"k": "eod", "t0": 1525594677937, "t": 339348}},
                     {"csm": {"k": "chk", "f": 15, "l": {"csmcount": 67, "cel": 147, "csm": 16}, "s": "full"}}]}

    # def parse(self, response):
    #     yield scrapy.FormRequest.from_response(
    #         response=response,
    #         # formdata=self.data,
    #         callback=self.parse_start_url
    #     )
    #
    # def parse_start_url(self, response):
    #     url = 'https://www.amazon.cn/gp/site-directory/ref=nav_shopall_btn/'
    #     yield scrapy.Request(
    #         url=url,
    #         callback=self.parse_page
    #     )

    def parse(self, response):
        # print response.url

        href_list = response.xpath('//div[@id="cat3"]//div[@class="a-row"]/ul/li//a/@href').extract()
        text_list = response.xpath('//div[@id="cat3"]//div[@class="a-row"]/ul/li//a/text()').extract()
        for text, href in zip(text_list, href_list):
            url = 'https://www.amazon.cn' + href
            with open('url.py','a') as f:
                f.write(url)
                f.write(';\n')
            yield scrapy.Request(
                url=url,
                callback=self.parse_page,
                # cookies=self.cookies,
                headers=self.headers
            )

    def parse_page(self, response):
        with open('good_link.py', 'a') as f:
            f.write(response.url)
            f.write(';\n')
        node_list = response.xpath('//ul[@id="s-results-list-atf"]/li')
        if not node_list:
            node_list = response.xpath('//div[@id="mainResults"]/ul/li')
            if not node_list:
                return
        for index,node in enumerate(node_list):
            item = AmazonItem()
            # 商品标题
            if not node.xpath('div/div[3]//text()'):
                return
            item['title'] = node.xpath('div/div[3]//text()').extract_first()
            # print '----------------------------------------------------'
            # print response.url + '---------------------'+ item['title']
            item['type_link'] = response.url
            item['index'] = index + 1
            # 商品链接
            item['good_link'] = node.xpath('div/div[3]//a/@href').extract_first()
            # 商品logo
            item['logo'] = node.xpath('div/div[3]/div[last()]/span/text()').extract_first()
            # 商品价格
            item['price'] = node.xpath('div/div[5]/div[1]//span/text()').extract_first()
            # 商品评价星级
            rank = node.xpath('div/div[last()]//a/i[1]//text()').extract_first()
            if not rank:
                item['rank'] = u'暂无星级评分'
            else:item['rank'] = rank
            yield item
        link = response.xpath('//span[@class="pagnRA"]/a/@href')
        # yield item
        if link:
            next_link = 'https://www.amazon.cn' + link.extract_first()
            # print '-----------------------'
            # with open('next_link.py','a') as f:
            #     f.write(next_link)
            # print '-----------------------'
            yield scrapy.Request(
                url=next_link,
                callback=self.parse_page,
                cookies=self.cookies,
                headers=self.headers
            )
