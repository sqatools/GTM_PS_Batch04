from base.selenium_base import SeleniumBase
from resources.amazon_website.amazon_register_page_data import *


class AmazonRegisterPage(SeleniumBase):

    def __init__(self,driver):
        super().__init__(driver)

    def click_signin(self):
        self.click_element(signin_click_loc)

    def enter_email_data(self, email_data):
        self.clear_fields(enter_email_loc)
        self.enter_text(email_data, enter_email_loc)

    def click_continue_button(self):
        self.click_element(continue_button_loc)

    def enter_mobile_num(self, phone_data):
        self.enter_text(phone_data, enter_mobile_num_loc)

    def enter_name(self, enter_name_data):
        self.clear_fields(name_loc)
        self.enter_text(enter_name_data, name_loc)

    def enter_pass(self, enter_pass_data):
        self.clear_fields(pass_loc)
        self.enter_text(enter_pass_data, pass_loc)

    def click_verify_mobno(self):
        self.click_element(verify_mob_no)

