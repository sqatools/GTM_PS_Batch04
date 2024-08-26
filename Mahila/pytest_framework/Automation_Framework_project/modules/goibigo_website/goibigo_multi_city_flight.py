from base.selenium_base import SeleniumBase
from resources.goibigo_website.goibigo_multi_city_flight import *


class GoibigoOneWayFlight(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver)

    def close_popup(self):
        self.click_element(close_pop_up_loc)

    def click_multi_city(self):
        self.click_element(click_multi_city_loc)

    def click_from_trip(self):
        self.click_element(click_from_trip_loc)

    def enter_from_city(self,enter_data):
        self.enter_text(enter_data,enter_form_city_loc)

    def select_from_city(self):
        self.click_element(select_from_city_loc)

    def enter_to_city(self,enter_data):
        self.enter_text(enter_data,enter_to_city_loc)

    def select_to_city(self):
        self.click_element(select_to_city_loc)

    def dep_date_click(self):
        self.click_element(departure_date_click_loc)

    def select_dep_date(self,enter_data):
        self.enter_text(enter_data,departure_date_select_loc)

    def select_adult(self):
        self.click_element(select_adult_loc)

    def select_child(self):
        self.click_element(select_child_loc)

    def select_infant(self):
        self.click_element(select_infant_loc)

    def select_travel_class(self):
        self.click_element(select_travel_class_loc)

    def select_done(self):
        self.click_element(done_loc)

    def click_enter_to_city(self):
        self.click_element(click_enter_to_city_loc)

    def enter_to_city2(self,enter_data):
        self.enter_text(enter_data,enter_to_city_loc2)

    def select_to_city2(self):
        self.click_element(select_to_city_loc2)

    def search_flight(self):
        self.click_element(search_flight_loc)