import time
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
log = logging.getLogger(__name__)


@pytest.mark.usefixtures("get_driver")
class TestDummyDropdown:

    @pytest.mark.smoke
    def test_add_more_passenger(self):
        log.info("selecting value from add more passenger dropdown")
        add_more_pass = self.driver.find_element(By.ID, "admorepass")
        s_obj = Select(add_more_pass)
        s_obj.select_by_visible_text("Add 3 more passenger (200%)")

    @pytest.mark.sanity
    def test_add_billing_country(self):
        log.info("selecting value from billing country dropdown")
        country_dd = self.driver.find_element(By.ID, "billing_country")
        s_obj2 = Select(country_dd)
        s_obj2.select_by_visible_text("United Kingdom")
