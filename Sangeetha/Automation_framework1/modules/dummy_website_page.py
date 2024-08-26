from base.seleniumbase import Seleniumbase
from resouces.dummy_website_page_data import *


class DummyWebsite(Seleniumbase):
    def __init__(self, driver):
        super().__init__(driver)
        self.navigate_to_dummy_website()

    def navigate_to_dummy_website(self):
        self.driver.get(dummy_website_url)
    def select_radio_button_locator(self):
        self.click_element(radio_button_locator)

    def enter_first_name(self, first_name):
        self.enter_text(first_name, first_name_locator)

    def enter_last_name(self, last_name):
        self.enter_text(last_name, last_name_locator)

    def enter_date_of_birth(self, dob_value):
        self.enter_text(dob_value, dob_locator)

    def select_female_radio_button(self):
        self.click_element(female_locator)

    def select_more_passenger_from_dropdown(self, more_pass_value):
        self.select_value_from_dropdown(more_pass_value, addmore_passenger_dd_locator)

    def select_one_way_trip(self):
        self.click_element(one_way_locator)

    def enter_from_city_value(self, from_city):
        self.enter_text(from_city, from_city_locator)

    def enter_dest_city_value(self, dest_city):
        self.enter_text(dest_city, dest_city_locator)

    def enter_departure_date(self, departure_date):
        self.enter_text(departure_date, departure_date_locator)

    def enter_return_date(self, return_date_value):
        self.enter_text(return_date_value, return_date_locator)

    def enter_visa_date(self, visa_date_value):
        self.enter_text(visa_date_value, visa_date_locator)

    def enter_whatsapp(self, whatsapp_value):
        self.click_element(whatsapp_value, whatsapp_locator)

    def enter_billing_name(self, billing_name):
        self.enter_text(billing_name, billing_name_locator)

    def enter_billing_phone(self, billing_phone):
        self.enter_text(billing_phone, billing_phone_locator)

    def enter_billing_email(self, billing_email):
        self.enter_text(billing_email, billing_email_locator)

    def enter_billing_address(self, billing_address):
        self.enter_text(billing_address, billing_address_locator)

    def enter_post_code(self, post_code):
        self.enter_text(post_code, post_code_locator)

    def enter_street_address(self, street_address):
        self.enter_text(street_address, street_address_locator)

    def select_country_locator_from_dropdown(self, country_locator_value):
        self.select_value_from_dropdown(country_locator_value, country_locator_dd_locator)

    def select_checkbox_list_locator_locator(self):
        self.click_element(checkbox_list_locator)
