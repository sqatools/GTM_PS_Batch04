
import time
import pytest
from modules.amazon_website.amazon_register_page import AmazonRegisterPage
from resources.amazon_website.amazon_register_page_data import *

@pytest.mark.usefixtures("get_driver")
class TestAmazonRegisterPage:

    @pytest.fixture(autouse= True)
    def setup(self):
        self.ar = AmazonRegisterPage(self.driver)

    def test_amazon_register_page(self):
        self.driver.get("https://www.amazon.in/")
        self.ar.click_signin()
        self.ar.enter_email_data(email_data=enter_email_data)
        self.ar.click_continue_button()
        self.ar.enter_mobile_num(phone_data=enter_mobile_num_data)
        self.ar.enter_name(enter_name_data=name_data)
        self.ar.enter_pass(enter_pass_data=pass_data)
        self.ar.click_verify_mobno()
        time.sleep(10)





