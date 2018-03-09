# -*- coding: utf-8 -*-

from scrapy import Request
import scrapy.http.response
from qianmu.items import UniversityItem
from scrapy_redis.spiders import RedisSpider

class UniversitySpider(RedisSpider):
    name = 'u2'
    # allowed_domains = ['qianmu.iguye.com']
    # start_urls = ['http://qianmu.iguye.com/2018USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D']

    def __init__(self, max_num=0, *args, **kwargs):
        super(UniversitySpider, self).__init__(*args, **kwargs)
        self.max_num = int(max_num)

    def parse(self, response):
        links = response.xpath("//div[@id='content']//tr[position()>1]/td[2]/a/@href").extract()
        for i, link in enumerate(links):
            if self.max_num and self.max_num <= i:
                break
            if not link.startswith('http://'):
                link = 'http://qianmu.iguye.com/%s' % link
            request = Request(link, callback=self.parse_university)
            request.meta['rank'] = i + 1
            yield request

    def parse_university(self, response):
        response=response.replace(body=response.text.replace('\t',''))
        self.logger.info(response.url)
        wiki_content = response.xpath('//div[@id="wikiContent"]')[0]
        item = UniversityItem(
            name=wiki_content.xpath('./h1[@class="wikiTitle"]/text()').extract_first(),
            rank=response.meta['rank'],
        )



        # item = dict(title=wiki_content.xpath('./h1[@class="wikiTitle"]/text()').extract_first())
        # item['rank'] = response.meta['rank']
        keys = wiki_content.xpath('./div[@class="infobox"]/table//tr/td[1]/p/text()').extract()
        cols = wiki_content.xpath('./div[@class="infobox"]/table//tr/td[2]')
        values = [''.join(col.xpath('.//text()').extract()) for col in cols]
        # item.update(zip(keys, values))
        data = dict(zip(keys,values))
        item['country'] = data.get('国家','')
        item['state'] = data.get('州省','')
        item['city'] = data.get('城市','')
        item['undergraduate_num']=data.get('本科生人数','')
        item['postgraduate_num']=data.get('研究生人数','')
        item['website']=data.get('网址','')
        self.logger.info('item %s scraped' % item['name'])
        yield item
