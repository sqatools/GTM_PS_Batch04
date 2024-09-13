from Base.SeleniumBaseFile import Seleniumbase
from resource.dummylocator_data import *


class Dummywebsitepage(Seleniumbase):
    def __init__(self,driver):
        super().__init__(driver)

    def enter_fname(self,fname):
        self.sent_datato_element(fname,first_name)

    def enter_lname(self,lname):
        self.sent_datato_element(lname,last_name)

    def enter_dob(self,dob):
        self.sent_datato_element(dob,date_ofbirth)

    def select_sex(self):
        self.click_element(radio_button)

    def select_passanger(self,passanger):
        self.get_dropdown(passanger,add_passanger)

    def select_trip(self):
        self.click_element(tripdetails)

    def select_fcity(self,fcity):
        self.sent_datato_element(fcity,f_city)

    def select_dcity(self,dcity):
        self.sent_datato_element(dcity,d_city)
    def select_ddate(self,ddate):
        self.sent_datato_element(ddate,d_date)

    def select_rdate(self,rdate):
        self.sent_datato_element(rdate,r_date)

