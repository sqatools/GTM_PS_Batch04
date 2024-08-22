from base.selenium_base import SeleniumBase
from resource.dummy_website.dummy_website_page_data import *


class DummyWebsite(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, first_name):
        self.enter_text(first_name, first_name_locator)

    def enter_last_name(self, last_name):
        self.enter_text(last_name, last_name_locator)

    def enter_date_of_birth(self, dob_value):
        self.enter_text(dob_value, dob_locator)

    def select_male_radio_button(self):
        self.click_element(male_locator)

    def select_more_passenger_from_dropdown(self, more_pass_value):
        self.select_value_from_dropdown(more_pass_value, addmore_passenger_dd_locator)

    def select_one_way_trip(self):
        self.click_element(one_way_locator)

    def enter_from_city_value(self, from_city):
        self.enter_text(from_city, from_city_locator)

    def enter_dest_city_value(self, dest_city):
        self.enter_text(dest_city, dest_city_locator)

    def provide_journey_details(self,
                                dob,
                                no_of_pass,
                                from_city,
                                dest_city):
        self.enter_date_of_birth(dob)
        self.select_male_radio_button()
        self.select_more_passenger_from_dropdown(no_of_pass)
        self.select_one_way_trip()
        self.enter_from_city_value(from_city)
        self.enter_dest_city_value(dest_city)
