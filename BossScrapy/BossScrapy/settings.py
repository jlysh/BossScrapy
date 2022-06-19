# Scrapy settings for BossScrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'BossScrapy'

SPIDER_MODULES = ['BossScrapy.spiders']
NEWSPIDER_MODULE = 'BossScrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'BossScrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
   # 'cookie':'lastCity=101190400; wd_guid=e0afac60-aa63-4f98-8495-d938bb72f550; historyState=state; _bl_uid=7zlp721hh9ChyLdzzsU5ng82bk6v; wt2=D6yLXYtmO5DN-Xkvy-ji4CpukgADINuY4wvFwSkhizXjohqwolD9FQwFpRv7P7AO3Mk_b1fQIaZVooyEqGZAk4A~~; wbg=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1653700494,1655595662,1655602859; __zp_seo_uuid__=00c42b1e-81d7-4c17-8530-72be852488d2; __g=-; acw_tc=0b6e703216556228747703283e016e76be2a670acaa87f08a3fa1d9f165ca1; geek_zp_token=V1RNsiEOz-0lxjVtRvyhgeKy-w6DzTxCo~; __zp_stoken__=7f3adPDQ1F11%2FWzFpWmF%2BIHp%2Fa38%2Fcm04IkcrZSg6aWBiTWFKGD5AW0BWXAN%2FWF5iHmMJJWVWcXclbSFVPH1VXyE8cjZsdBhpLDEAGgtKR3ZFBBtvbwwTLAMSdVpKOAN%2FXFo7W2BffFxtXSU%3D; __c=1655602859; __l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fwww.zhipin.com%2Fc101190400%2F%3Fquery%3D%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%26page%3D2&s=3&g=&friend_source=0&s=3&friend_source=0; __a=16256098.1651058103.1655595662.1655602859.264.6.154.247; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1655623508',
   'referer': 'https://www.zhipin.com/',
   'sec-ch-ua-platform': "Windows",
   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'

}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'BossScrapy.middlewares.BossscrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'BossScrapy.middlewares.BossscrapyDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'BossScrapy.pipelines.BossscrapyPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
