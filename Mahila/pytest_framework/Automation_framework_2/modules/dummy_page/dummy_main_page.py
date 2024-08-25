from base.selenium_base import SeleniumBase
from resource.dummy_page.dummy_page_data import *


class Dummymainpage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def select_radio_button(self):
        self.click_element(radio_button_loc)

    def first_name(self, enter_data):
        self.enter_text(enter_data,first_name_loc)

    def sec_name(self, enter_data):
        self.enter_text(enter_data,sec_name_loc)

    def dob(self, enter_data):
        self.enter_text(enter_data,dob_loc)

    def gender(self):
        self.click_element(gender_loc)

    def no_of_add_pass(self, select_data):
        self.select_from_dropdown(select_data,no_of_add_pass_loc)

    def travel_det(self):
        self.click_element(travel_det_loc)

    def from_city(self, enter_data):
        self.enter_text(enter_data,from_city_loc)

    def dest_city(self, enter_data):
        self.enter_text(enter_data,dest_city_loc)

    def dep_date(self, enter_data):
        self.enter_text(enter_data,dep_date_loc)

    def ret_date(self, enter_data):
        self.enter_text(enter_data,ret_date_loc)

    def app_date(self, enter_data):
        self.enter_text(enter_data,app_date_loc)

    def recieve_ticket(self):
        self.click_element(recieve_ticket_loc)

    def bill_name(self, enter_data):
        self.enter_text(enter_data,bill_name_loc)

    def bill_phone(self, enter_data):
        self.enter_text(enter_data,bill_phone_loc)

    def bill_email(self, enter_data):
        self.enter_text(enter_data,bill_email_loc)

    def bill_add(self, enter_data):
        self.enter_text(enter_data,bill_add_loc)

    def bill_coun(self, select_data):
        self.select_from_dropdown(select_data,bill_coun_loc)

    def post_code(self, enter_data):
        self.enter_text(enter_data,post_code_loc)

    def prefecture(self, enter_data):
        self.enter_text(enter_data,prefecture_loc)

    def stree_add1(self, enter_data):
        self.enter_text(enter_data,stree_add1_loc)

    def stree_add2(self, enter_data):
        self.enter_text(enter_data,stree_add2_loc)

    def most_visit_city(self):
        self.click_element(most_visit_city_loc)


