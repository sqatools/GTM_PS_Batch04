import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("get_driver_session")
class TestDummyDropdown:
    @pytest.fixture(autouse=True)
    def setup(self, get_driver_session):
        self.driver = get_driver_session

    def test_add_more_passenger(self):
        add_more_pass = self.driver.find_element(By.ID, "admorepass")
        s_obj = Select(add_more_pass)
        s_obj.select_by_visible_text("Add 3 more passenger (200%)")

    def test_add_billing_country(self):
        country_dd = self.driver.find_element(By.ID, "billing_country")
        s_obj2 = Select(country_dd)
        s_obj2.select_by_visible_text("United Kingdom")
