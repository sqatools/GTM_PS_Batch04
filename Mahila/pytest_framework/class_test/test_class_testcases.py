import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("get_driver")
class TestDummy:

    def test_user_details(self):
        self.driver.find_element(By.ID,"fromcity").send_keys("TVM")
        self.driver.find_element(By.ID,"destcity").send_keys("Banglr")
        time.sleep(10)

    def test_billing_details(self):
        self.driver.find_element(By.ID,"billing_name").send_keys("Mahila")
        self.driver.find_element(By.ID,"billing_phone").send_keys("7909175279")
        time.sleep(5)
