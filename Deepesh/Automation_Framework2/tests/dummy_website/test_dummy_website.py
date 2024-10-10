import time

import pytest
from modules.dummy_website.dummy_website_page import DummyWebsite
from resource.dummy_website.dummy_website_page_data import *
from utilities.utility_tools import CommonUtils

@pytest.mark.dummy_website
@pytest.mark.usefixtures("get_driver_dummy")
class TestDummyWebsite:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.dw = DummyWebsite(self.driver)
        self.utils = CommonUtils()
        self.json_data = self.utils.read_json_content("resource/dummy_website/dummy_website_test_data.json")

    @pytest.mark.smoke
    @pytest.mark.p1
    def test_enter_first_and_last_name(self):
        self.dw.enter_first_name(first_name_value)
        self.dw.enter_last_name(last_name_value)
        time.sleep(5)

    @pytest.mark.sanity
    @pytest.mark.p2
    def test_provide_journey_details(self):
        self.dw.provide_journey_details(dob=self.json_data['dob'],
                                        no_of_pass=self.json_data['number_of_pass'],
                                        from_city=self.json_data['from_city'],
                                        dest_city=self.json_data['dest_city'])
        time.sleep(5)
