
import time
import pytest

from modules.amazon_website.amazon_login_page import AmazonLoginPage
from resources.amazon_website.amazon_login_page_data import *

@pytest.mark.usefixtures("get_driver")

class TestAmazonLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.al = AmazonLoginPage(self.driver)

    def test_amazon_valid_login(self):
        self.driver.get("https://www.amazon.in/")
        self.al.click_signin()
        self.al.enter_email_details(enter_data=enter_email_data1)
        self.al.click_continue_button()
        self.al.enter_password_details(enter_data=enter_pass_data1)
        self.al.click_signin_button()
        time.sleep(10)

    def test_amazon_invalid_login(self):
        self.driver.get("https://www.amazon.in/")
        self.al.click_signin()
        self.al.enter_email_details(enter_data=enter_email_data2)
        self.al.click_continue_button()
        self.al.enter_password_details(enter_data=enter_pass_data2)
        self.al.click_signin_button()
        time.sleep(10)