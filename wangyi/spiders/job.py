import scrapy
from wangyi.items import WangyiItem


class JobSpider(scrapy.Spider):
    name = "job"
    allowed_domains = ["163.com"]
    start_urls = ["https://hr.163.com/position/list.do"]

    def parse(self, response):
        # 1.提取一页的数据
        trs = response.xpath('//*[@class="position-tb"]/tbody/tr')
        # print(len(trs))
        for num, tr in enumerate(trs):
            # 设置一个过滤条件
            if num % 2 == 0:
                item = WangyiItem()
                item['name'] = tr.xpath('./td[1]/a/text()').extract_first()
                item['link'] = response.urljoin(tr.xpath('./td[1]/a/@href').extract_first())
                item['depart'] = tr.xpath('./td[2]/text()').extract_first()
                item['category'] = tr.xpath('./td[3]/text()').extract_first()
                item['type'] = tr.xpath('./td[4]/text()').extract_first()
                item['address'] = tr.xpath('./td[5]/text()').extract_first()
                item['num'] = tr.xpath('./td[6]/text()').extract_first().strip()
                item['date'] = tr.xpath('./td[7]/text()').extract_first()
                # yield item

                # 3.构建详情页面的请求
                yield scrapy.Request(
                    url=item['link'],
                    callback=self.parse_detail,
                    meta={'item': item}
                )
        # 2.进行翻页操作
        part_url = response.xpath('/html/body/div[2]/div[2]/div[2]/div/a[last()]/@href').extract_first()
        # 判断终止条件
        if part_url != 'javascript:void(0)':
            next_url = response.urljoin(part_url)
            yield scrapy.Request(
                url=next_url,
                callback=self.parse
            )

    def parse_detail(self, response):
        # 将meta传参获取
        item = response.meta['item']
        # 提取剩余的字段
        item['duty'] = response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/text()').extract()
        item['require'] = response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/text()').extract()
        yield item
