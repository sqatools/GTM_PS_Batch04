import time

from base.selinium_base import SeleniumBase
from resource.dummy_website.dummy_website_data import *

class DummyWebsite(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, first_name):
        self.enter_text(first_name, first_name_locator)

    def enter_last_name(self, last_name):
        self.enter_text(last_name, last_name_locator)
