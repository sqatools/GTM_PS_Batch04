import time
import pytest
from modules.google_page.google_search_page import GoogleSearchPage
from resource.google_page.google_search_page_data import *


@pytest.mark.usefixtures("get_driver")
class TestGoogleSearch:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.gs = GoogleSearchPage(self.driver)

    def test_search_on_google(self):
        self.driver.get("https://www.google.co.in")
        self.gs.enter_search_data(search_data=google_search_data)
        self.gs.click_search_button()
        time.sleep(10)
