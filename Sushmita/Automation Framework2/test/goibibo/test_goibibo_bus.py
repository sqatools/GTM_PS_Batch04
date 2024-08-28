import time

import pytest
from module.goibibo.goibibo_bus_booking_page import BusBooking
from resource.goibibo.goibibo_bus_booking_data import *

@pytest.mark.usefixtures("get_driver")

class TestBusBooking :

    @pytest.fixture(autouse=True)
    def setup(self):
        self.bb = BusBooking(self.driver)


    def test_bus_booking_page(self):
        self.driver.get("https://www.goibibo.com/")

        self.bb.source_element(city_name)
        time.sleep(10)
