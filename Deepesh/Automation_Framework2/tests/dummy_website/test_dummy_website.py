import time

import pytest
from modules.dummy_website.dummy_website_page import DummyWebsite
from resource.dummy_website.dummy_website_page_data import *

@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.dw = DummyWebsite(self.driver)

    def test_enter_first_and_last_name(self):
        self.driver.get(dummy_website_url)
        self.dw.enter_first_name(first_name_value)
        self.dw.enter_last_name(last_name_value)
        time.sleep(10)
