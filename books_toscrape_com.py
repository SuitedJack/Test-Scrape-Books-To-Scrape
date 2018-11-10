from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import TippingTheVelvetBooksToScrapeSandboxItem, AllProductsBooksToScrapeSandboxItem, PortiaItem


class BooksToscrape(BasePortiaSpider):
    name = "books.toscrape.com"
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[Item(TippingTheVelvetBooksToScrapeSandboxItem,
                   None,
                   '.product_main',
                   [Field('Title',
                          'h1 *::text',
                          []),
                       Field('Price',
                             '.price_color *::text',
                             []),
                       Field('Stock',
                             '.instock *::text',
                             [])])]]
