import time

import pytest
from amazonwebsite import Amazonpage
from amazonwebsite_locator import *

@pytest.mark.usefixtures("get_driver")
class Testamazonpage:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.aw=Amazonpage(self.driver)

    def test_amazon_page(self):
        self.driver.get("https://www.amazon.in/")
        self.aw.enter_searchdata(search_data=search_data)
        self.aw.click_search()
        time.sleep(10)
