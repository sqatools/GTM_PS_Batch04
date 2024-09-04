import time

from modules.goibibowebsite.goibibowebsitepage import Goibibowbsite
import pytest
from resource.goibibolocator.goibibolocator_data import *

@pytest.mark.usefixtures("get_driver")
class Testgoibibo:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.gw=Goibibowbsite(self.driver)

    def test_goibibo(self):
        self.driver.get("https://www.goibibo.com/")
        self.gw.select_close()
        self.gw.select_train()
        self.gw.select_fcity()
        self.gw.enter_fcity(fcity=fcity)
        self.gw.select_railwaystation(station_name=from_station_name)
        self.gw.select_dcity()
        self.gw.enter_dcity(dcity=dcity)
        self.gw.select_railwaystation(station_name=dest_station_name)

        time.sleep(10)

