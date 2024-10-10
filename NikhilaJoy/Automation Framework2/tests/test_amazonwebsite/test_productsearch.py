import time
import pytest
from modules.amazonwebsite.amazonproductsearch import Amazonproduct
from resource.amazonwebsitelocators.amazonproductlocator import *

@pytest.mark.usefixtures("get_driver")
class Testamazonproduct:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.ap=Amazonproduct(self.driver)

    def test_product(self):
        self.driver.get("https://www.amazon.in/")
        self.ap.enter_searchdata(search_data=search_data)
        self.ap.click_search()
        self.ap.select_size()
        self.ap.select_price()
        self.ap.select_go()
        time.sleep(10)
