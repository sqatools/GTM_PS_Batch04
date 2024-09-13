from SeleniumBaseFile import Seleniumbase
from amazonwebsite_locator import *

class Amazonpage(Seleniumbase):
    def __init__(self,driver):
        super().__init__(driver)

    def enter_searchdata(self,search_data):
        self.sent_datato_element(search_data,search_field)

    def click_search(self):
        self.click_element(search_button)

