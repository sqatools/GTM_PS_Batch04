import time
import pytest
from make_my_trip import MakeMyTrip
from make_my_trip_test_data import *


@pytest.mark.usefixtures("get_driver")
class TestMakeMyTrip:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.bc = MakeMyTrip(self.driver)

    def test_booking_cab(self):
        self.driver.get("https://www.makemytrip.com/cabs/")
        self.bc.close_popup()
        self.bc.click_from()
        self.bc.send_from_location(search_data=send_from_data)
        self.bc.select_from_location()
        time.sleep(3)
