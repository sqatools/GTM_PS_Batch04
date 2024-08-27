from selenium.webdriver.common.by import By
from base.selinium_base import SeleniumBase
from resource.goibibo.goibibo_flight_data import *


class FlightBooking(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        # element = self.close_popup()
        # if element:
        #     element.click()
        # self.navigate_()

    def close_popup(self):
        self.click_element(self.close_popup_link)

    def navigate_flight(self):
        self.click_element(flight_link)

    def click_oneway(self):
        self.click_element(oneway)

    def enter_city(self):
        self.click_element(enter_city)

    def enter_input(self, city_name):
        self.enter_text(city_name, click_input)

    def select_city(self):
        self.click_element(source_city)
