import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
# driver.maximize_window()
# driver.implicitly_wait(10)


@pytest.mark.usefixtures("session_fix")
class TestBooking:

    def test_hotel_booking(self, wb_driver):
        wb_driver.find_element(By.ID, "fromcity").send_keys("Mumbai")
        wb_driver.find_element(By.ID, "destcity").send_keys("Kolkata")

    def test_flight_booking(self, wb_driver):
        wb_driver.find_element(By.ID, "billing_name").send_keys("John")
        wb_driver.find_element(By.ID, "billing_phone").send_keys("5646456456456")


