import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:

    def test_booking_info(self):
        self.driver.find_element(By.ID, "fromcity").send_keys("Mumbai")
        self.driver.find_element(By.ID, "destcity").send_keys("Pune")

    def test_billing_details(self):
        self.driver.find_element(By.ID, "billing_name").send_keys("John")
        self.driver.find_element(By.ID, "billing_phone").send_keys("543543543")

