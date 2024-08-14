import time
import selenium.webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("get_driver")
class TestDropDowns:

    @pytest.mark.smoke
    def test_drop_down(self):
        add_pass = self.driver.find_element(By.ID,"admorepass")
        select_obj = Select(add_pass)
        select_obj.select_by_visible_text("Add 3 more passenger (200%)")
        time.sleep(5)

    def test_bill(self):
        bill_country = self.driver.find_element(By.ID,"billing_country")
        sel_obj = Select(bill_country)
        sel_obj.select_by_visible_text("Andorra")
        time.sleep(5)

