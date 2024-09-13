from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select



class Seleniumbase:
    def __init__(self,driver,timeout=30):
        self.driver=driver
        self.timeout=timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_element(self,locator):
        element=self.wait.until(ec.presence_of_element_located(locator))
        return element

    def sent_datato_element(self,data,locator):
        element=self.get_element(locator)
        element.send_keys(data)

    def click_element(self,locator):
        element=self.get_element(locator)
        element.click()

    def get_text(self,locator):
        element=self.get_element(locator)
        return element.text
    def get_dropdown(self,value,locator):
        element=self.get_element(locator)
        select=select(element)
        select.select_by_visible_text(value)




