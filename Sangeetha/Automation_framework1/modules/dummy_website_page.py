from base.selenium_base import SeleniumBase
from resource.dummy_website_page_data import *
class DummyWebsite(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)