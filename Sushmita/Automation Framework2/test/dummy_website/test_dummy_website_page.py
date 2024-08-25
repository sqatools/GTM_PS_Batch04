import time

import pytest
from module.dummy_website.dummy_website_page import DummyWebsite
from resource.dummy_website.dummy_website_data import *


@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.dw = DummyWebsite(self.driver)

    def test_enter_firstname_lastname(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        self.dw.enter_first_name(first_name_value)
        self.dw.enter_last_name(last_name_value)
        time.sleep(10)
