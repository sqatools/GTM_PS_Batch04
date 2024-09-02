from Base.SeleniumBaseFile import Seleniumbase
from resource.amazonwebsitelocators.amazonregisterlocator import *


class Amazonwebsite(Seleniumbase):

    def __init__(self,driver):
      super().__init__(driver)


    def user_fnamelname(self,name):
        self.sent_datato_element(name,first_n_lname)

    def user_email(self,email):
        self.sent_datato_element(email,register_email)

    def user_password(self,password):
        self.sent_datato_element(password,reg_password)

    def user_recheck(self,password):
        self.sent_datato_element(password,recheck_password)


    def user_submit(self):
        self.click_element(submit)
