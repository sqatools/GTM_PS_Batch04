from Base.SeleniumBaseFile import Seleniumbase
from resource.goibibolocator.goibibolocator_data import *
from selenium.webdriver.common.by import By

class Goibibowbsite(Seleniumbase):
    def __init__(self,driver):
        super().__init__(driver)

    def select_train(self):
        self.click_element(train)

    def select_close(self):
        self.click_element(close)

    def select_fcity(self):
        self.click_element(f_city)

    def enter_fcity(self,fcity):
        self.sent_datato_element(fcity, f_city_input_field)

    def select_fsuggestion(self):
        self.click_element(f_suggestion)

    def select_dcity(self):
        self.click_element(d_city)

    def enter_dcity(self,dcity):
        self.sent_datato_element(dcity, d_city_input_field)


    def select_suggestion(self):
        self.click_element(d_suggestion)

    def select_railwaystation(self, station_name):
        locator = (By.XPATH, f"//span[text()='{station_name}']//ancestor::li")
        self.click_element(locator)
