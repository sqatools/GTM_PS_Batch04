from base.selenium_base import SeleniumBase
from resources.amazon_website.amazon_login_page_data import *


class AmazonLoginPage(SeleniumBase):

    def __init__(self,driver):
        super().__init__(driver)

    def click_signin(self):
        self.click_element(signin_click_loc)

    def enter_email_details(self, enter_data):
        self.clear_fields(enter_email_loc)
        self.enter_text(enter_data, enter_email_loc)

    def click_continue_button(self):
        self.click_element(continue_button_loc)

    def enter_password_details(self, enter_data):
        self.enter_text(enter_data, enter_pass_loc)

    def click_signin_button(self):
        self.click_element(click_sign_in_loc)