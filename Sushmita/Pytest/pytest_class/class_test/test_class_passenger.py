import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('session_fix')
class TestBooking1:

    def test_passenger_details(self, driver):
        driver.find_element(By.NAME, "firstname").send_keys('Mallika')
        driver.find_element(By.XPATH, "//input[@id='firstname'][2]").send_keys('ps')

    def test_travel_details(self, driver):
        driver.find_element(By.ID, "fromcity").send_keys('Delhi')
        driver.find_element(By.ID, "destcity").send_keys('Bangalore')

# from selenium.webdriver.common.by import By
#
# @pytest.mark.usefixtures('session_fix')
# class TestBooking :
#
#     def test_travel_details(self,driver):
#         driver.find_element(By.ID,"fromcity").send_keys('Mumbia')
#         driver.find_element(By.ID,'destcity').send_keys('kolkata')
#
#     def test_billing_details(self,driver):
#         driver.find_element(By.ID,'billing_name').send_keys('Arun')
#         driver.find_element(By.ID,'billing_phone').send_keys('67899')
