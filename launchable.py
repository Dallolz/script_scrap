# # import the spiders you want to run
# from spiders.similartechSpider import SimilarTechSpider
# from spiders.addonsimilartechSpider import AddonSimilarSpider

# # scrapy api imports
# from scrapy import signals, log
# from twisted.internet import reactor
# from scrapy.crawler import Crawler
# from scrapy.settings import Settings


# # list of crawlers
# TO_CRAWL = [similartechSpider, addonsimilartechSpider]

# # crawlers that are running 
# RUNNING_CRAWLERS = []

# def spider_closing(spider):
#     """
#     Activates on spider closed signal
#     """
#     log.msg("Spider closed: %s" % spider, level=log.INFO)
#     RUNNING_CRAWLERS.remove(spider)
#     if not RUNNING_CRAWLERS:
#         reactor.stop()

# # start logger
# log.start(loglevel=log.DEBUG)

# # set up the crawler and start to crawl one spider at a time
# for spider in TO_CRAWL:
#     settings = Settings()

#     # crawl responsibly
#     settings.set("USER_AGENT", "Dallolz (+http://dallolz.github.io)")
#     crawler = Crawler(settings)
#     crawler_obj = spider()
#     RUNNING_CRAWLERS.append(crawler_obj)

#     # stop reactor when spider closes
#     crawler.signals.connect(spider_closing, signal=signals.spider_closed)
#     crawler.configure()
#     crawler.crawl(crawler_obj)
#     crawler.start()

# # blocks process; so always keep as the last statement
# reactor.run()

import scrapy
from scrapy.crawler import CrawlerProcess

import os
print(os.getcwd())

from script_v1.spiders import AddonSimilarSpider, SimilarTechSpider                                                     
process = CrawlerProcess()
process.crawl(SimilarTechSpider)
process.crawl(AddonSimilarSpider)
process.start()