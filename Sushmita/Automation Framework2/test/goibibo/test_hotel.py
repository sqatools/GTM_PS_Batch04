import time

import pytest
from module.goibibo.goibigo_hotel_page import HotelBooking
from resource.goibibo.goibigo_hotel_data import *


@pytest.mark.usefixtures("get_driver")
class TestHotelBooking:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.gh = HotelBooking(self.driver)

    def test_hotel_booking(self):
        self.driver.get("https://www.goibibo.com/hotels/")
        #self.gh.close_popup()
        self.gh.click_radio_button()
        self.gh.click_landmark()
        self.gh.select_landmark(city_name)

        #time.sleep(10)
