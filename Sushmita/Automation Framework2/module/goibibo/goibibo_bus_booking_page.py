from resource.goibibo.goibibo_bus_booking_data import *
from base.selinium_base import SeleniumBase
from selenium.webdriver.common.by import By


class BusBooking(SeleniumBase):

    def __int__(self, driver):
        super().__init__(driver)
        element = self.close_popup()
        if element:
            element.click()
        self.navigate_to_bus_booking_page()

    def close_popup(self):
        return self.get_element(close_popup_link)

    def navigate_bus(self):
        self.click_element(navigate_bus_link)

    def source_element(self, source_city_name):
        self.enter_text(source_city_name, source_link)
