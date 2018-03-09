# -*- coding: utf-8 -*-

# Scrapy settings for qianmu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'qianmu'

SPIDER_MODULES = ['qianmu.spiders']
NEWSPIDER_MODULE = 'qianmu.spiders'

HTTPPROXY_ENABLED = True
PROXIES = ['http://ms0108:ms0108@182.84.98.201:888',
    'http://ms0108:ms0108@117.41.187.112:888',
    'http://ms0108:ms0108@210.16.189.75:888',
    'http://ms0108:ms0108@1.82.230.108:888',
    'http://ms0108:ms0108@117.41.184.182:888',
    'http://ms0108:ms0108@222.73.48.188:888',
    'http://ms0108:ms0108@103.21.142.201:888',]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; PPC Mac OS X 10_6_0) AppleWebKit/5352 (KHTML, like Gecko) Chrome/14.0.881.0 Safari/5352'
PORXY_MAX_FAILED = 3
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 10
REACTOR_THREADPOOL_MAXSIZE =20
# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# DOWNLOAD_TIMEOUT=15
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
  'Content-Encoding': 'gzip, deflate',
  'Content-Type': 'text/html; charset=UTF-8',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'qianmu.middlewares.QianmuSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'qianmu.middlewares.MyCustomDownloaderMiddleware': 543,
    'qianmu.middlewares.useragent.RandomUserangetMiddleware':543,
    'qianmu.middlewares.proxy.RandomProxyMiddleware':749,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'qianmu.pipelines.CheckPipeline': 300,
    'qianmu.pipelines.RedisPipeline':301,
    # 'qianmu.pipelines.MysqlPipeline':302,
#redis分布式配置
'scrapy_redis.pipelines.RedisPipeline': 300,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


#redis分布式配置
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# REDIS_URL = 'redis://user:pass@hostname:6379'
SCHEDULER_PERSIST = True