from selenium.webdriver.common.by import By
from base.selenium_base import selenium_base
from resources.goibibo_flight_data import *
class FlightBooking(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        element = self.close_popup()
        if element:
            element.click()
        self.navigate_to_bus_booking_page()

    def close_popup(self):
        return self.get_element(login_popup_close)

    def navigate_to_flight_booking_page(self):
        self.click_element(flight_booking_page_link)
    def navigate_to_flight_booking_page(self):
        self.click_element(flight_booking_page_link)

    def flight_oneway_button(self):
        self.click_element(flight_oneway_button)

    def from_enter_city_name(self):
        self.enter_text(from_enter_city_name)

    def from_city_input_field(self):
        self.enter_text(from_city_input_field)

    def To_city_input_field(self):
        self.To_city_input_field(To_city_input_field)

    def select_travel_date(self, travel_date):
        self.click_element(calender_locator)

