import time
import pytest
from modules.goibigo_website.goibigo_bus_booking import GoibigoBusBooking
from resources.goibigo_website.goibigo_bus_booking_data import *


@pytest.mark.usefixtures("get_driver")
class TestGoibigoBusBooking:

    @pytest.fixture(autouse= True)
    def setup(self):
        self.gbb = GoibigoBusBooking(self.driver)

    def test_goibigo_register_page(self):
        self.driver.get("https://www.goibibo.com")
        self.gbb.close_popup()
        self.gbb.select_bus()
        self.gbb.enter_from_city(enter_data=from_city_data)
        self.gbb.select_from_city()
        self.gbb.enter_To_city(enter_data=to_city_data)
        self.gbb.select_to_city()
        self.gbb.click_travel_date()
        self.gbb.select_travel_date()
        self.gbb.search_bus()
        self.gbb.bus_type_selection()
        #self.gbb.dep_time_selection()
        #self.gbb.boarding_point_selection()
        #self.gbb.operator_sele()
        #self.gbb.select_seat()
        #self.boarding_point_sele()

        time.sleep(10)