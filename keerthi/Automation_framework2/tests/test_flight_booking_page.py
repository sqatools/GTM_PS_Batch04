import pytest
from modules.goibibo_website.flight_booking_page import flightBooking
from resource.goibibo_website.flight_booking_page_data import *


@pytest.mark.usefixtures("get_driver_goibibo")
class Testflightbooking:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.bb = flightBooking(self.driver)

    def flight_booking(self):
        self.bb.enter_city_name(enter_city_name)
        self.bb.enter_city_name_from_suggestion_list(enter_city_name)
        self.bb.To_city_name(To_city_name)
        self.bb.To_city_name_from_suggestion_list(To_city_name)
        self.bb.select_travel_date(Departure_date)
        self.bb.select_Adult(Ad_adults)

