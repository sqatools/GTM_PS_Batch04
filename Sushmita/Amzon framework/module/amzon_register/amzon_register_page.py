from base.selenium_base import SeleniumBase
from resource.amazon_register.amzon_register_data import *


class AmazonTesting(SeleniumBase):

    def __int__(self, driver):
        super().__init__(driver)

    def click_signin(self):
        self.click_element(acc_signin_loc)

    def enter_email(self,enter_data):
        self.enter_text(enter_data,signin_loc)

    def click_continue(self):
        self.click_element(continue_loc)

    def enter_password(self,enter_data):
        self.enter_text(enter_data,password_loc)

    def click_signin_but(self):
        self.click_element(signin_button)




    def click_all_menu(self):
        self.click_element(all_loc)

    def click_account_filed(self):
        self.click_element(account_loc)

    def click_address(self):
        self.click_element(adress_loc)

    def enter_search_field(self,enter_data):
        self.enter_text(enter_data,search_loc)

    def click_serach_but(self):
        self.click_element(search_button)

    def click_add_cart(self):
        self.click_element(add_cart_ele)
    def click_amazon_basic(self):
        self.click_element(amzon_basic)
