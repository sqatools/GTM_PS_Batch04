from modules.amazonwebsite.amazon_login import Amazonlogin

from resource.amazonwebsitelocators.amazonloginlocators import *
import time

import pytest



@pytest.mark.usefixtures("get_driver")
class Testamazon:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.al=Amazonlogin(self.driver)

    def test_login(self):
        self.driver.get("https://www.amazon.in/")
        self.al.click_signin()
        self.al.enter_uername(email=email)
        self.al.click_submit()
        self.al.enter_password(password=password)
        self.al.signin()
        time.sleep(3)

