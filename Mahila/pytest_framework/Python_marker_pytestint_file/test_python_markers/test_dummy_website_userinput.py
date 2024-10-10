import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("get_driver")

class TestDummy:

    @pytest.mark.sanity
    def test_city_details(self):
        from_city_loc = (By.ID,"fromcity")
        from_city_val = "Chennai"
        self.driver.find_element(*from_city_loc).send_keys(from_city_val)

        des_city_loc = (By.ID,"destcity")
        des_city_val = "Bengaluru"
        self.driver.find_element(*des_city_loc).send_keys(des_city_val)

        time.sleep(5)

    @pytest.mark.sanity
    def test_billing_details(self):
        bill_name_locator = (By.ID, "billing_name")
        bill_name_val = "Mahila"
        self.driver.find_element(*bill_name_locator).send_keys(bill_name_val)

        phone_num_loca = (By.ID,"billing_phone")
        phone_num_val = "7909175279"
        self.driver.find_element(*phone_num_loca).send_keys(phone_num_val)
        time.sleep(5)
