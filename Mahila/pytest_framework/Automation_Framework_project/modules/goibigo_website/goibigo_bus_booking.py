from base.selenium_base import SeleniumBase
from resources.goibigo_website.goibigo_bus_booking_data import *


class GoibigoBusBooking(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver)

    def close_popup(self):
        self.click_element(close_pop_up_loc)


