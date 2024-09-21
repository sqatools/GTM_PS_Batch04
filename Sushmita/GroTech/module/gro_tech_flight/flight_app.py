from base.gro_tech_base import SeleniumBase
from resource.gro_tech_flight.flight_data import *

class GroTechFlight(SeleniumBase):

    def __int__(self,driver):
        super().__init__(self,driver)

    def flight_flip(self):
        self.move_to_element(flight_flippop)

    def flight_readmore(self):
        self.click_element(flight_readmore)

    def click_oneway(self):
        self.click_element(oneway_loc)

    def select_from_value(self, enterdata):
        self.select_from_dropdown(enterdata, from_loc)

    def select_to_value(self, enterdata):
        self.select_from_dropdown(enterdata, To_loc)

    def enter_depart_date(self, enterdata):
        self.enter_text(enterdata, Depart_loc)

    def enter_return_date(self, enterdata):
        self.enter_text(enterdata, return_loc)

    def select_adults(self, enterdata):
        self.select_from_dropdown(enterdata, adult_loc)

    def select_children(self, enterdata):
        self.select_from_dropdown(enterdata, children_loc)

    def click_serach_but(self):
        self.click_element(search_loc)
