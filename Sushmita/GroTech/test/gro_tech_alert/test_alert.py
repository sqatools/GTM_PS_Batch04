import time

from module.gro_tech_alert.alert_module import GroTechRegisterPage
from resource.gro_tech_alert.alert_data import *
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("get_driver")
class TestGroTech:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.al = GroTechRegisterPage(self.driver)

    def test_amazon_testing(self):
        self.driver.get("https://grotechminds.com/hoverover/")
        #self.al.move_cursor()
        #self.al.click_alert_tab()
        #self.al.alert_but()
        self.al.hover_on_demo()
        time.sleep(10)
