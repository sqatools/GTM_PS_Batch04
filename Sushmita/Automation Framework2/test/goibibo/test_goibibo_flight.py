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
        #self.driver.find_element(By.XPATH,)
        self.gf.click_oneway()
        self.gf.enter_city()
        self.gf.enter_input(source_city)
        self.gf.select_city()

