from base.selenium_base import SeleniumBase
from resource.amazon.amzon_data import *


class AmazonTesting(SeleniumBase):

    def __int__(self, driver):
        super().__init__(driver)

    def click_signin(self):
        self.click_element(acc_signin_loc)

    def enter_email(self,enter_data):
        self.enter_text(enter_data,email_loc)

    def click_continue(self):
        self.click_element(continue_loc)

    def enter_password(self,enter_data):
        self.enter_text(enter_data,password_loc)

    def click_signin_but(self):
        self.click_element(signin_button)
