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

    def slider_price(self):
        self.slider_ele(slider_loc)

    def click_go_submit(self):
        self.click_element(go_price_loc)
    def click_size(self):
        self.click_element(L_loc)

    def click_dress(self):
        self.click_element(dress_loc)

    def click_cart(self):
        self.click_element(cart_loc)

    def click_proceed_cart(self):
        self.click_element(proceed_loc)

    def click_adress_button(self):
        self.click_element(your_address_loc)

    def click_use_address(self):
        self.click_element(use_address_loc)
