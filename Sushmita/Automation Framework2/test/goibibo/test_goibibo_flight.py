import time

import pytest
from module.goibibo.goibibo_flight_page import FlightBooking
from resource.goibibo.goibibo_flight_data import *
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("get_driver")
class TestFlightBooking:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.gf = FlightBooking(self.driver)

    def test_flight_booking(self):
        self.driver.get("https://www.goibibo.com/flights/")
       # self.driver.find_element(By.XPATH,""//span[@class='logSprite icClose']")
        self.gf.close_popup()
        self.gf.click_oneway()
        self.gf.enter_city()
        self.gf.enter_input(enter_from_city_data)
        self.gf.select_city()
        #self.gf.select_to_city()
        self.gf.enter_to_city(to_city_data)
        self.gf.select_to_city_data()
        self.gf.click_depart_date()
        self.gf.select_dep_date()
        self.gf.click_traveller_class()
        self.gf.click_adult_button()
        self.gf.click_children_button()
        self.gf.click_infant_button()
        self.gf.click_economy()
        self.gf.click_done()
        self.gf.click_search_button()
        time.sleep(10)


