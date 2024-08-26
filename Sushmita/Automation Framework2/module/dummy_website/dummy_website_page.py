import time

from base.selinium_base import SeleniumBase
from resource.dummy_website.dummy_website_data import *

class DummyWebsite(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, first_name):
        self.enter_text(first_name, first_name_locator)

    def enter_last_name(self, last_name):
        self.enter_text(last_name, last_name_locator)

    def enter_dob(self,date_birth):
        self.enter_text(date_birth,dob_locator)

    def select_radio_button(self):
        self.click_element(click_locator)

    def select_passanger(self,more_pass_value):
        self.select_value_from_dropdown(more_pass_value,Num_passanger_locator)

    def selct_travel_radio_button(self):
        self.click_element(travel_details_locator)

    def enter_fromcity(self,from_city):
        self.enter_text(from_city,from_city_locator)

    def enter_destcity(self,dest_city):
        self.enter_text(dest_city,dest_city_locator)

    def enter_depart_value(self,depart_date):
        self.enter_text(depart_date,depart_locator)

    def enter_return_date(self,return_date):
        self.enter_text(return_date,return_locator)

    def enter_appointment_date(self,appointment_date):
        self.enter_text(appointment_date,delivery_option_locator)

    def click_dummy_element(self):
        self.click_element(dummy_radio_locator)

    def enter_billing_name(self,billing_name):
        self.enter_text(billing_name,billing_name_locator)

    def enter_billing_phone(self,billing_phone):
        self.enter_text(billing_phone,billing_phone_locator)

    def enter_billing_email(self,billing_email):
        self.enter_text(billing_email,billing_email_locator)

    def enter_billing_street(self,billing_street):
        self.enter_text(billing_street,billing_adress_locator)

    def select_country(self,billing_country_value):
        self.select_value_from_dropdown(billing_country_value,billing_country_locator)

    def enter_postcode(self,postcode_value):
        self.enter_text(postcode_value,billing_postcode_locator)

    def enter_prefecture(self,precture_value):
        self.enter_text(precture_value,billing_prefecture_locator)

    def select_city(self):
        self.click_element(city_locator)
