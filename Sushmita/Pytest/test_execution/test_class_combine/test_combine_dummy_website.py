import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("get_driver_session")
class TestDummyWebsite:

    @pytest.fixture(autouse=True)
    def setup(self,get_driver_session):
        self.driver = get_driver_session()

    def test_booking_info(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        self.driver.find_element(By.ID, "fromcity").send_keys('Delhi')
        self.driver.find_element(By.ID, "destcity").send_keys('kolkata')

    def test_billing_details(self):
        self.driver.find_element(By.ID,"billing_name").send_keys('arun')
        self.driver.find_element(By.ID,"billing_phone").send_keys('3455')
