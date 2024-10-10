import time

import pytest
from module.dummy_website.dummy_website_page import DummyWebsite
from resource.dummy_website.dummy_website_data import *


@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.dw = DummyWebsite(self.driver)

    def test_enter_firstname_lastname(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        self.dw.enter_first_name(first_name_value)
        self.dw.enter_last_name(last_name_value)
        self.dw.enter_dob(dob_value)
        self.dw.select_radio_button()
        self.dw.select_passanger(no_of_pass)
        self.dw.selct_travel_radio_button()
        self.dw.enter_fromcity(from_city_value)
        self.dw.enter_destcity(dest_city_value)
        self.dw.enter_depart_value(depart_value)
        self.dw.enter_return_date(return_value)
        self.dw.enter_appointment_date(delivery_date_value)
        self.dw.click_dummy_element()
        self.dw.enter_billing_name(billing_name)
        self.dw.enter_billing_phone(billing_phone)
        self.dw.enter_billing_email(billing_email)
        self.dw.enter_billing_street(billing_street)
        self.dw.select_country(billing_country)
        self.dw.enter_postcode(billing_postcode)
        self.dw.enter_prefecture(billing_prefectue)
        self.dw.select_city()
        time.sleep(10)
