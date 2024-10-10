from base.selenium_base import SeleniumBase
from resources.amazon_website.amazon_end_end_purchase_data import *


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

    def enter_search_field(self, enter_data):
        self.enter_text(enter_data, search_product_loc)

    def click_search_button(self):
        self.click_element(search_button_loc)

    def select_delivery_day(self):
        self.click_element(delivery_day_loc)

    def adding_to_cart(self):
        self.click_element(add_to_cart_loc)

    def click_select_size(self):
        self.click_element(click_select_size_loc)
    def select_size(self):
        self.click_element(select_size_loc)

    def show_details(self):
        self.click_element(show_details_loc)

    def click_buy_now(self):
        self.click_element(buy_now_loc)

    def click_payment_change(self):
        self.click_element(change_pay_method_loc)

    def click_card_payment(self):
        self.click_element(click_card_loc)
