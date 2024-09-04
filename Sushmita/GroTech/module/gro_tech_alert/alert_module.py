from base.gro_tech_base import SeleniumBase
from resource.gro_tech_alert.alert_data import *


class GroTechRegisterPage(SeleniumBase):

    def __int__(self, driver):
        super().__init__(driver)

    def move_cursor(self):
        self.move_to_element(alert_loc)

    def click_alert_tab(self):
        self.handle_browser_window(read_more_alert)

    def alert_but(self):
        self.handle_alert(alert_loc1)
