import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("session_fix")
class TestBookingInfo:

    def test_billing_booking(self, wb_driver):
        wb_driver.find_element(By.ID, "billing_email").send_keys("john@gmail.com")
        wb_driver.find_element(By.ID, "billing_address").send_keys("Kurla complex")

    def test_gender_booking(self, wb_driver):
        wb_driver.find_element(By.ID, "male").click()
        wb_driver.find_element(By.ID, "female").click()



