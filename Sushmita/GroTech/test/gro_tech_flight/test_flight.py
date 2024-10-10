import time

from module.gro_tech_flight.flight_app import GroTechFlight
from resource.gro_tech_flight.flight_data import *
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("get_driver")
class TestGroTech:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.al = GroTechFlight(self.driver)

    def test_flight(self):
        self.driver.get("https://grotechminds.com/automate-me/")
        self.al.flight_flip()
        self.al.flight_readmore()
        browser_windows = self.driver.window_handles
        print(browser_windows)
        self.driver.switch_to.window(browser_windows[1])
        self.al.click_oneway()
        self.al.select_from_value(from_city)
        self.al.select_to_value(to_city)
        self.al.enter_depart_date(depart_date)
        self.al.enter_return_date(return_date)
        self.al.select_adults(adult_val)
        self.al.select_children(children_val)
        self.al.click_serach_but()
        time.sleep(10)
