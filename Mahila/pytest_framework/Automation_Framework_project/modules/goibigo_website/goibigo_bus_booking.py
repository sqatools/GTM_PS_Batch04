from base.selenium_base import SeleniumBase
from resources.goibigo_website.goibigo_bus_booking_data import *


class GoibigoBusBooking(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver)

    def close_popup(self):
        self.click_element(close_pop_up_loc)

    def select_bus(self):
        self.click_element(select_bus_loc)

    def enter_from_city(self,enter_data):
        self.enter_text(enter_data,From_city_loc)

    def select_from_city(self):
        self.click_element(select_from_city_loc)

    def enter_To_city(self,enter_data):
        self.enter_text(enter_data,To_city_loc)

    def select_to_city(self):
        self.click_element(select_to_city_loc)

    def click_travel_date(self):
        self.click_element(click_travel_date_loc )

    def select_travel_date(self):
        self.click_element(select_travel_date_loc)

    def search_bus(self):
        self.click_element(search_bus_loc)

    def bus_type_selection(self):
        self.click_element(bus_type_selection_loc)

    def dep_time_selection(self):
        self.click_element(dep_time_selection_loc)

    def boarding_point_selection(self):
        self.click_element(boarding_point_loc)

    def operator_sele(self):
        self.click_element(operator_sele_loc)

    def select_seat(self):
        self.click_element(select_seat_loc)

    def boarding_point_sele(self):
        self.click_element(boarding_point_sele_loc)


