import time

import pytest
from modules.dummy_website_page import DummyWebsite
from resouces.dummy_website_page_data import *

#from utilities.utility_tools import CommonUtils
@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.dw = DummyWebsite(self.driver)

    def test_click_radio_button_locator(self):
        self.dw.select_radio_button_locator()
    def test_enter_first_and_last_name(self):
        self.dw.enter_first_name(first_name_value)
        self.dw.enter_last_name(last_name_value)

    def test_enter_dob(self):
        self.dw.enter_date_of_birth(dob_value)
        time.sleep(10)

