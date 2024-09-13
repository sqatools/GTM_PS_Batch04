import time
import pytest
from modules.goibigo_website.goibigo_bus_booking import GoibigoBusBooking
from resources.goibigo_website.goibigo_bus_booking_data import *


@pytest.mark.usefixtures("get_driver")
class TestGoibigoBusBooking:

    @pytest.fixture(autouse= True)
    def setup(self):
        self.gbb = GoibigoBusBooking(self.driver)

    def test_goibigo_register_page(self):
        self.driver.get("https://www.goibibo.com")
        self.gbb.close_popup()


        time.sleep(10)