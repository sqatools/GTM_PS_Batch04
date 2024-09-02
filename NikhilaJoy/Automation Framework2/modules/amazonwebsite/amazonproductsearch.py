from Base.SeleniumBaseFile import Seleniumbase
from resource.amazonwebsitelocators.amazonproductlocator import *


class Amazonproduct(Seleniumbase):
    def __init__(self,driver):
        super().__init__(driver)

    def enter_searchdata(self,search_data):
        self.sent_datato_element(search_data,search_field)

    def click_search(self):
        self.click_element(search_button)

    def select_size(self):
        self.click_element(size)

    def select_price(self):
        self.click_element(price_range)

    def select_go(self):
        self.click_element(go)