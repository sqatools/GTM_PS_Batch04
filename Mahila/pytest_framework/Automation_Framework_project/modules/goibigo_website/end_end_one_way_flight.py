from base.selenium_base import SeleniumBase
from resources.goibigo_website.end_end_one_way_flight import *


class GoibigoOneWayFlight(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver)

    def close_popup(self):
        self.click_element(close_pop_up_loc)

    def click_one_way(self):
        self.click_element(click_one_way_loc)

    def click_from_city_filed(self):
        self.click_element(click_from_city_loc)

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

    def travel_and_class(self):
        self.click_element(travel_and_class_loc)

    def adult_button(self):
        self.click_element(adult_button_loc)

    def child_button(self):
        self.click_element(child_button_loc)

    def select_economy(self):
        self.click_element(economy_loc)
    def select_done(self):
        self.click_element(done_loc)

    def search_flight(self):
        self.click_element(search_flight_loc)

    def dep_time_select(self):
        self.click_element(dep_time_select_loc)

    def click_stops_details(self):
        self.click_element(stops_loc)
    def pref_airline(self):
        self.click_element(pref_airline_loc)

    def view_fair(self):
        self.click_element(view_fair_loc)

    def price_range_drag(self):
        self.click_and_hold(price_range_drag_loc)
