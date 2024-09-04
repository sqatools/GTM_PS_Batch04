import time

from module.gro_tech_register.register_module import GroTechRegisterPage
from resource.gro_tech_register.register_data import *
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("get_driver")
class TestGroTech:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.al = GroTechRegisterPage(self.driver)

    def test_amazon_testing(self):
        self.driver.get("https://grotechminds.com/flights/")
        self.al.click_oneway()
        self.al.select_from_value(from_city)
        self.al.select_to_value(to_city)
        self.al.enter_depart_date(depart_date)
        self.al.select_adults(adult_val)
        self.al.select_children(children_val)
        self.al.click_serach_but()
        var=self.al.element_displayed().text
        time.sleep(10)
