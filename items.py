# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class ScriptV1Item(Item):
    domain_list = Field()
    commerce_platform_title = Field()
    customer_service_title = Field()

class ScriptV2Item(Item):
    monthly_visits = Field()
    country_name = Field()
    domain_list = Field()