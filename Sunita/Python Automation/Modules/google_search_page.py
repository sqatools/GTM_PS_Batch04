from base.selenium_base import SeleniumBase
from resource.google_page.google_search_page_data import *

class GoogleSearchPage(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver)

    def enter_search_data(self,search_data):
        self.enter_text(search_data,search_field_locator)

    def click_google_search_button(self):
        self.click_element(search_button_locator)

