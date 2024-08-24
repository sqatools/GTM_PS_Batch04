import pytest
from modules.goibibo_website.bus_booking_page import BusBooking
from resource.goibibo_website.bus_booking_page_data import *


@pytest.mark.usefixtures("get_driver_goibibo")
class TestBusBooking:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.bb = BusBooking(self.driver)

    def test_search_bus_select_seat(self):
        self.bb.enter_source_city(src_city_name)
        self.bb.select_city_name_from_suggestion_list(src_city_name)
        self.bb.enter_dest_city(dest_city_name)
        self.bb.select_city_name_from_suggestion_list(dest_city_name)
        self.bb.select_travel_date(travel_date)
        self.bb.click_search_button()
        self.bb.select_first_seat_of_bus(bus_name)
        assert self.bb.verify_review_booking_header()

