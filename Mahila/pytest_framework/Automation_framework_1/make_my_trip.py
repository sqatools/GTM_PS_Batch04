from selenium_base import SeleniumBase
from make_my_trip_locators import *

class MakeMyTrip(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def close_popup(self):
        self.click_element(close_pop_up_locator)

    def click_from(self):
        self.click_element(click_from_locator)

    def send_from_location(self,search_data):
        self.enter_text(search_data,send_from_locator)

    def select_from_location(self):
        self.click_element(select_from_locator)

