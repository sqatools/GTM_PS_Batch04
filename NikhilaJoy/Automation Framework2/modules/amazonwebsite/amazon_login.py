from Base.SeleniumBaseFile import Seleniumbase
from resource.amazonwebsitelocators.amazonloginlocators import *

class Amazonlogin(Seleniumbase):
    def __init__(self,driver):
        super().__init__(driver)


    def click_signin(self):
        self.click_element(login)
    def enter_uername(self,email):
        self.sent_datato_element(email,login_email)

    def click_submit(self):
        self.click_element(login_submit)

    def enter_password(self,password):
        self.sent_datato_element(password,login_password)

    def signin(self):
        self.click_element(login_signin)