from selenium.webdriver.common.by import By
from base.selinium_base import SeleniumBase
from resource.goibibo.goibibo_flight_data import *


class FlightBooking(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        # element = self.close_popup()
        # if element:
        #     element.click()
        # self.navigate_flight()

    def close_popup(self):
        self.click_element(close_popup_link)

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

    def select_to_city(self):
        self.click_element(To_city)

    def enter_to_city(self,dest_city):
        self.enter_text(dest_city,to_city_input)

    def select_to_city_data(self):
        self.click_element(to_city_name)

    def click_depart_date(self):
        self.click_element(depart_date_click)

    def select_dep_date(self):
        self.click_element(departure_date_select_loc)

    def click_traveller_class(self):
        self.click_element(traveller_class)

    def click_adult_button(self):
        self.click_element(adult_loc)

    def click_children_button(self):
        self.click_element(children_loc)

    def click_infant_button(self):
        self.click_element(Infant_loc)

    def click_economy(self):
        self.click_element(economy_loc)

    def click_done(self):
        self.click_element(done_loc)

    def click_search_button(self):
        self.click_element(search_loc)
