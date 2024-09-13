
import time
import pytest

from modules.amazon_website.amazon_end_end_purchase import AmazonLoginPage
from resources.amazon_website.amazon_end_end_purchase_data import *

@pytest.mark.usefixtures("get_driver")

class TestAmazonLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.al = AmazonLoginPage(self.driver)

    def test_amazon_valid_login(self):
        self.driver.get("https://www.amazon.in/")
        self.al.click_signin()
        self.al.enter_email_details(enter_data=enter_email_data)
        self.al.click_continue_button()
        self.al.enter_password_details(enter_data=enter_pass_data)
        self.al.click_signin_button()
        self.al.enter_search_field(enter_data=search_product_data)
        self.al.click_search_button()
        self.al.select_delivery_day()
        self.al.adding_to_cart()
        self.al.click_select_size()
        self.al.select_size()
        self.al.show_details()
        self.al.click_buy_now()
        self.al.click_payment_change()
        self.al.click_card_payment()
        time.sleep(10)

