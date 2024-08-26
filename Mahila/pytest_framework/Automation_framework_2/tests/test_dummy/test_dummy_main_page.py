import time
import pytest
from modules.dummy_page.dummy_main_page import Dummymainpage
from resource.dummy_page.dummy_page_data import *

@pytest.mark.usefixtures("get_driver")
class TestDummymainpage:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.dm = Dummymainpage(self.driver)


    def test_dummy_main_page(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        self.dm.select_radio_button()
        self.dm.first_name(enter_data=first_name_data)
        self.dm.sec_name(enter_data=sec_name_data)
        self.dm.dob(enter_data=dob_data)
        self.dm.gender()
        self.dm.no_of_add_pass(select_data=no_of_add_pass_data)
        self.dm.travel_det()
        self.dm.from_city(enter_data=from_city_data)
        self.dm.dest_city(enter_data=dest_city_data)
        self.dm.dep_date(enter_data=dep_date_data)
        self.dm.ret_date(enter_data=ret_date_data)
        self.dm.app_date(enter_data=app_date_data)
        self.dm.recieve_ticket()
        self.dm.bill_name(enter_data=bill_name_data)
        self.dm.bill_phone(enter_data=bill_phone_data)
        self.dm.bill_email(enter_data=bill_email_data)
        self.dm.bill_add(enter_data=bill_add_data)
        self.dm.bill_coun(select_data=bill_coun_data)
        self.dm.post_code(enter_data=post_code_data )
        self.dm.prefecture(enter_data=prefecture_data)
        self.dm.stree_add1(enter_data=stree_add1_data)
        self.dm.stree_add2(enter_data=stree_add2_data)
        self.dm.most_visit_city()

        time.sleep(10)



