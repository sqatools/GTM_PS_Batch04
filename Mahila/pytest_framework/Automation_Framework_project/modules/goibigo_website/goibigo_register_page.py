from base.selenium_base import SeleniumBase
from resources.goibigo_website.goibigo_register_page import *


class GoibigoRegisterPage(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver)

    def close_popup(self):
        self.click_element(close_pop_up_loc)

    def signin_click(self):
        self.click_element(signin_loc)

    def enter_phone_number(self,enter_data):
        self.enter_text(enter_data,phone_number_loc)

