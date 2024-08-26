import time
import pytest
from modules.goibigo_website.goibigo_register_page import GoibigoRegisterPage
from resources.goibigo_website.goibigo_register_page import *


@pytest.mark.usefixtures("get_driver")
class TestGoibogoRegisterPage:

    @pytest.fixture(autouse= True)
    def setup(self):
        self.gr = GoibigoRegisterPage(self.driver)

    def test_goibigo_register_page(self):
        self.driver.get("https://www.goibibo.com")

        self.gr.close_popup()
        self.gr.signin_click()
        time.sleep(5)
        self.gr.enter_phone_number(enter_data=phone_number_data)
        time.sleep(10)