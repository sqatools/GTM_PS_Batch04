import time

from modules.dummywebsite.dummywebsitepage import Dummywebsitepage
from resource.dummylocator_data import *

import pytest
@pytest.mark.usefixtures("get_driver")
class Testdummypage:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.dw=Dummywebsitepage(self.driver)

    def test_dummywebsite(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        self.dw.enter_fname(fname=fname)
        self.dw.enter_lname(lname=lname)
        self.dw.enter_dob(dob=dob)
        self.dw.select_sex()
        self.dw.select_passanger(passanger=passanger)
        self.dw.select_trip()
        self.dw.select_fcity(fcity=fcity)
        self.dw.select_dcity(dcity=dcity)
        self.dw.select_ddate(ddate=ddate)
        self.dw.select_rdate(rdate=rdate)
        time.sleep(10)
