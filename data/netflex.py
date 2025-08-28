from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider

class NetflexSpider(CrawlSpider):

    name = "netflex"
    base_url = "https://help.netflix.com/en"
    start_urls = ["https://help.netflix.com/en"]
    allowd_domains = ["help.netflix.com"]
    max_pages = 100
    counter = 0
    
    custom_settings = {
        'CONCURRENT_REQUESTS': 5,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 10,
        'ROBOTSTXT_OBEY': False,
        'CONCURRENT_ITEMS': 100,
        'REACTOR_THREADPOOL_MAXSIZE': 400,
        'LOG_LEVEL': 'INFO',
        'RETRY_ENABLED': False,
        'REDIRECT_MAX_TIMES': 1,

        # do not fetch more than 5mb contents
        'DOWNLOAD_MAXSIZE': 5592405,

        # Grabs xpath before site finish loading
        'DOWNLOAD_FAIL_ON_DATALOSS': False,

        'DEPTH_PRIORITY': 1,
        'SCHEDULER_DISK_QUEUE' : 'scrapy.squeues.PickleFifoDiskQueue',
        'SCHEDULER_MEMORY_QUEUE' :'scrapy.squeues.FifoMemoryQueue'
    }

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True)
    )

    # to parse html content
    def parse_item(self, reponse):
        if self.counter > self.max_pages:
            raise CloseSpider("Page limit reached")
        
        data = reponse.css('.left-pane').getall()

        page_title = reponse.css('title::text').get()

        # to save file with page title
        if (not page_title) or (not data) or (not isinstance(data, list)) or (len(data) == 0):
            return

        # preprocessing title        
        page_title = page_title.replace(' ', '_').replace('/', '_').replace('//', '_').strip()

        print(f"Downloading {page_title}:\n{reponse.url}")

        file_name = 'netflex_data/' + page_title + '.html'

        with open(file_name, 'w', encoding='utf-8') as f:
            f.write('\n'.join(data))
