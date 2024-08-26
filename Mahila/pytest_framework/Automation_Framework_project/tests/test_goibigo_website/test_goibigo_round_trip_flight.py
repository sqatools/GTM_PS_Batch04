import time
import pytest
from modules.goibigo_website.goibigo_round_trip_flight import GoibigoOneWayFlight
from resources.goibigo_website.goibigo_round_trip_flight import *


@pytest.mark.usefixtures("get_driver")
class TestGoibigoOneWayFlight:

    @pytest.fixture(autouse= True)
    def setup(self):
        self.gof = GoibigoOneWayFlight(self.driver)

    def test_goibigo_register_page(self):
        self.driver.get("https://www.goibibo.com")
        self.gof.close_popup()
        self.gof.click_round_trip()
        time.sleep(5)
        self.gof.click_from_trip()
        self.gof.enter_from_city(enter_data=enter_form_city_data)
        self.gof.select_from_city()
        self.gof.enter_to_city(enter_data=enter_to_city_data)
        self.gof.select_to_city()
        self.gof.dep_date_click()
        self.gof.select_dep_date(enter_data=dep_date_value)
        self.gof.travel_and_class()
        self.gof.adult_button()
        self.gof.child_button()
        self.gof.premium_economy_selection()
        self.gof. select_done()
        self.gof.search_flight()

        time.sleep(10)