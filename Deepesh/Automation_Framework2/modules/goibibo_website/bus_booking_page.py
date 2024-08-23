from selenium.webdriver.common.by import By
from base.selenium_base import SeleniumBase
from resource.goibibo_website.bus_booking_page_data import *


class BusBooking(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        element = self.close_popup()
        if element:
            element.click()
        self.navigate_to_bus_booking_page()

    def close_popup(self):
        return self.get_element(login_popup_close)

    def navigate_to_bus_booking_page(self):
        self.click_element(bus_booking_page_link)

    def enter_source_city(self, source_city_name):
        self.enter_text(source_city_name, enter_source_field_locator)

    def enter_dest_city(self, dest_city_name):
        self.enter_text(dest_city_name, enter_destination_field_locator)

    def select_city_name_from_suggestion_list(self, city_name):
        locator = (By.XPATH, f"//span[text()='{city_name}']")
        self.click_element(locator)

    def select_travel_date(self, travel_date):
        self.click_element(calender_locator)
        date_locator = (By.XPATH, f"//span[text()='{travel_date}']//parent::li")
        self.click_element(date_locator)

    def click_search_button(self):
        self.click_element(search_bus_button)

    def select_first_seat_of_bus(self, bus_name):
        seat_locator = (By.XPATH, f"(//p[text()='{bus_name}'])[1]//parent::div//following-sibling::div[2]//button")
        self.click_element(seat_locator)
        self.click_element(boarding_point_location)
        self.click_element(dropping_point_location)
        self.click_element(select_first_upper_seat)
        self.click_element(select_seat_continue_button)

    def verify_review_booking_header(self):
        return self.get_element(review_booking_header)

