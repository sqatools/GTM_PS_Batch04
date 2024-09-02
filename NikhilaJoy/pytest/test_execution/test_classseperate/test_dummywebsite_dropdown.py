import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('get_driver')
class TestDummyDropdown:
    def test_addpassenger(self):
        addpass=self.driver.find_element(By.ID, "admorepass")
        sobj=Select(addpass)
        sobj.select_by_index(2)
        time.sleep(5)

    def test_addcountry(self):
        addcountry=self.driver.find_element(By.ID, "billing_country")
        sobj=Select(addcountry)
        sobj.select_by_visible_text("American Samoa")
        time.sleep(5)