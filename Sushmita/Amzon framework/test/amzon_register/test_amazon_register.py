import time

import pytest

from module.amzon_register.amzon_register_page import AmazonTesting
from resource.amazon_register.amzon_register_data import *
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("get_driver")
class TestFlightBooking:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.al = AmazonTesting(self.driver)

    def test_amazon_testing(self):
        self.driver.get("https://www.amazon.in/")
        self.al.click_signin()
        #self.click_new_customer()
        self.al.enter_email(email_input)
        self.al.click_continue()
        self.al.enter_password(password)
        self.al.click_signin_but()
        #self.al.click_search_field()

        self.al.click_all_menu()
        self.al.click_account_filed()
        self.al.click_address()
        self.driver.execute_script("window.scrollBy(0, 500)","")
        self.al.enter_search_field(search_data)
        self.al.click_serach_but()
        self.driver.execute_script("window.scrollBy(0, 500)","")
        self.al.slider_price()
        self.al.click_size()
        self.al.brand_select()
        self.al.click_dress()
        browser_windows = self.driver.window_handles
        print(browser_windows)
        self.driver.switch_to.window(browser_windows[1])
        self.driver.execute_script("window.scrollBy(0, 500)","")
        self.al.click_cart()
        self.al.click_proceed_cart()
        self.al.click_adress_button()
        self.al.click_use_address()
        time.sleep(15)


