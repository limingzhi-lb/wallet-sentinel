from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags

from applications.scrapy_app.scrapy_app.items import ScrapyAppItem


class JdItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    default_item_class = ScrapyAppItem
    default_input_processor = MapCompose(remove_tags)