# Scrapy settings for rns project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'rns'

SPIDER_MODULES = ['rns.spiders']
NEWSPIDER_MODULE = 'rns.spiders'


# USER-AGENT 설정
# USER_AGENT = 'test'

# Fake UserAgent 

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
}

# 타겟 사이트 Robopts.txt 준수 여부
# True로 설정시 Scrapy는 robots.txt 정책을 준수
ROBOTSTXT_OBEY = True

# 병렬처리, 주석처리면 기본 16
# Scrapy 다운로더가 수행할 최대 동시 요청 수
CONCURRENT_REQUESTS = 32

# 다운로드 딜레이
# 웹사이트에서 연속 페이지를 다운로드 하기 전에 다운로더가 기다려야 하는 시간 (초)
DOWNLOAD_DELAY =2 

# 웹사이트 도메인 동시 병렬 처리 개수
CONCURRENT_REQUESTS_PER_DOMAIN = 16

# 특정 웹사이트 IP주소 병렬 처리 갯수
CONCURRENT_REQUESTS_PER_IP = 16

# 쿠기 활성화 여부
COKKIES_ENABLED = True

# Telnet Console 활성화 여부
TELNETCONSOLE_ENABLED = False

# 기본 Request 헤더
'''
DEFAULT_REQUEST_HEADERS = {
   'Referer': 'https://news.daum.net/',
}
'''

# 미들웨어 사용 여부
SPIDER_MIDDLEWARES = {
   'rns.middlewares.RnsSpiderMiddleware': 543,
}

# 특정 다운로드 미들웨어 사용
DOWNLOADER_MIDDLEWARES = {
    'rns.middlewares.RnsDownloaderMiddleware': 543,
}

# 프로젝트에서 활성화 된 확장과 그 순서를 포함하는 dict
EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': None,
}
# 파이프라인 설정
ITEM_PIPELINES = {
    'rns.pipelines.RnsPipeline': 300,
}

# 캐시를 사용하면 동일하게 여러 번 요청 시 서버 사이드에 부하 절감 가능(변동사항 없을 경우)
# 캐시 사용 여부
HTTPCACHE_ENABLED = False
# 캐시 유효 기간
HTTPCACHE_EXPIRATION_SECS = 30
# 캐시 저장 경로
HTTPCACHE_DIR = 'httpcache'
# 응답 거부 캐시#
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 한글 쓰기(출력 인코딩)
FEED_EXPORT_ENCODING = 'utf-8'

# 오류 처리
# 자동 재시도 설정
RETRY_ENABLED = True

# 재시도 횟수 최대값
RETRY_TIMES = 2

# 재시도 대상 HTTP 코드
RETRY_HTTP_CODES = [500, 502, 503, 504, 408]

# 오류 무시 HTTP 상태 코드
HTTPERROR_ALLOWED_CODES = [404]

# 모든 상태 코드 오류 무시 (사용 비추천)
HTTPERROR_ALLOW_ALL = False