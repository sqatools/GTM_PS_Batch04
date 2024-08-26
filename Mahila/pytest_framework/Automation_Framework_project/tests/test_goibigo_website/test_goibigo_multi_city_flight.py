import time
import pytest
from modules.goibigo_website.goibigo_multi_city_flight import GoibigoOneWayFlight
from resources.goibigo_website.goibigo_multi_city_flight import *


@pytest.mark.usefixtures("get_driver")
class TestGoibigoOneWayFlight:

    @pytest.fixture(autouse= True)
    def setup(self):
        self.gof = GoibigoOneWayFlight(self.driver)

    def test_goibigo_register_page(self):
        self.driver.get("https://www.goibibo.com")
        self.gof.close_popup()
        self.gof.click_multi_city()
        self.gof.click_from_trip()
        self.gof.enter_from_city(enter_data=enter_form_city_data)
        self.gof.select_from_city()
        self.gof.enter_to_city(enter_data=enter_to_city_data)
        self.gof.select_to_city()
        self.gof.dep_date_click()
        self.gof.select_dep_date(enter_data=dep_date_value)
        self.gof.select_adult()
        self.gof.select_child()
        self.gof.select_infant()
        self.gof.select_travel_class()
        self.gof.select_done()
        self.gof.click_enter_to_city()
        self.gof.enter_to_city2(enter_data=enter_to_city_data2)
        self.gof.select_to_city2()
        self.gof.search_flight()
        time.sleep(10)