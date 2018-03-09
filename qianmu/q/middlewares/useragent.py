# -*- coding: utf-8 -*-
import faker


class RandomUserangetMiddleware(object):
    def __init__(self, settings):
        self.faker = faker.Faker()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
        request.headers['User-Agent'] = self.faker.user_agent()
        print(request.headers)