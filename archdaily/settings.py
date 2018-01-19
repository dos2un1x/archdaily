# -*- coding: utf-8 -*-

# Scrapy settings for archdaily project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'archdaily'

SPIDER_MODULES = ['archdaily.spiders']
NEWSPIDER_MODULE = 'archdaily.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'archdaily (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
DOWNLOAD_TIMEOUT = 60
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 32
CONCURRENT_REQUESTS_PER_IP = 0

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = True
TELNETCONSOLE_PORT = [6023, 6073]

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Referer": "https://www.archdaily.cn/cn/search/projects"
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
    # 'scrapy.spidermiddleware.depth.DepthMiddleware': None,
    # 'scrapy.spidermiddleware.referer.RefererMiddleware': None,
    # 'scrapy.spidermiddleware.httperror.HttpErrorMiddleware': None,
}
SPLASH_URL = 'http://192.168.1.16:8050'
DEPTH_LIMIT = 3
DEPTH_PRIORITY = 3
DEPTH_STATS = False
DEPTH_STATS_VERBOSE = False
#HTTPERROR_ALLOWED_CODES = [504]
REFERER_ENABLED = True

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
    # 'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
    # 'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    # 'scrapy.downloadermiddleware.cookies.CookiesMiddleware': None,
    # 'scrapy.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware': None,
    # 'scrapy.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware': None,
    # 'scrapy.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
    # 'scrapy.downloadermiddleware.stats.DownloaderStats': None,
}

# ROTATING_PROXY_LIST = [
#     'https://209.91.223.227:8080',
#     'https://36.78.60.125:8080',
#     # ...
# ]
ROTATING_PROXY_LIST_PATH = 'proxies.txt'
# ROTATING_PROXY_LOGSTATS_INTERVAL = 5
# ROTATING_PROXY_CLOSE_SPIDER = True
# ROTATING_PROXY_PAGE_RETRY_TIMES = 5
# ROTATING_PROXY_BACKOFF_BASE = 300
# ROTATING_PROXY_BACKOFF_CAP = 3600
# ROTATING_PROXY_BAN_POLICY = 'rotating_proxies.policy.BanDetectionPolicy'

COMPRESSION_ENABLED = True
DOWNLOADER_STATS = True
RANDOMIZE_DOWNLOAD_DELAY = True
#REDIRECT_MAX_TIMES = 20
#DNSCACHE_ENABLED = True
RETRY_ENABLED = True
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 408]

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#    'scrapy.pipeline.images.ImagesPipeline': 1,
#    'scrapy.pipeline.files.FilesPipeline': 1,
    'archdaily.middlewares.MyImagesPipeline': 1,
}
IMAGES_STORE = 'C:\Users\Administrator\PycharmProjects\pic'
FILES_STORE = 'C:\Users\Administrator\PycharmProjects\pic'

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 3
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_FILE = "test.log"
LOG_LEVEL = "INFO"
LOG_STDOUT = False
