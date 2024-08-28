from base.selinium_base import SeleniumBase
from resource.goibibo.goibigo_hotel_data import *


class HotelBooking(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)

    def close_popup(self):
        self.click_element(close_popup_link)

    def click_radio_button(self):
        self.click_element(radio_button)

    def click_landmark(self):
        self.click_element(landmark_loc)

    def select_landmark(self,enter_data):
        self.enter_text(enter_data,select_landmark)

    def click_checkin(self):
        self.click_element(checkin_date)

    def click_chekin_input(self):
        self.click_element(select_checkin_date)
