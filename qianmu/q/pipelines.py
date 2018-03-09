# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import redis
import logging
import pymysql
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
class CheckPipeline(object):
    def process_item(self, item, spider):
        if not item['undergraduate_num'] or not item['postgraduate_num']:
            raise DropItem('Miss field in %s' % item)
        return item

class RedisPipeline(object):
    def __init__(self):
        self.r = redis.Redis()
    def process_item(self,item,spider):
        self.r.sadd(spider.name,item['name'])
        logger.info('redis:add %s to %s '%(item['name'],spider))
        return item

class MysqlPipeline(object):
    def __init__(self):
        self.conn =None
        self.cur = None

    def open_spider(self,spider):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='rock1204',
            db='qianmu',
            charset='utf8',

        )
        self.cur = self.conn.cursor()
    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()

    def process_item(self,item,spider):
        # cols = item.keys()
        # values = [item[col] for col in cols]
        # cols = ['`%s`'% key for key in cols]
        #zip *语法解压
        cols,values = zip(*item.items())
        sql = "insert into `universities` (%s)VALUE (%s);"% (','.join(cols),','.join(['%s']*len(cols)))
        self.cur.execute(sql,values)
        self.conn.commit()
        logger.info(self.cur._last_executed)
        return item
