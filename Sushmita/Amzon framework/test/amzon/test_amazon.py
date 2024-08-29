import time

import pytest

from module.amazon.amzon_page import AmazonTesting
from resource.amazon.amzon_data import *
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("get_driver")
class TestFlightBooking:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.al = AmazonTesting(self.driver)

    def test_amazon_testing(self):
        self.driver.get("https://www.amazon.in/")
        self.al.click_signin()
        self.al.enter_email(email_input)
        self.al.click_continue()
        self.al.enter_password(password)
        self.al.click_signin_but()
        time.sleep(10)

