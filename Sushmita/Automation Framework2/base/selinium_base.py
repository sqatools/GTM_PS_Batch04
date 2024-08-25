from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from utlities.utility_tool import CommonUtils
class SeleniumBase:

    def __init__(self,driver,timeout=30):
        self.driver=driver
        self.timeout=timeout
        self.wait=WebDriverWait(self.driver,self.timeout)
        self.utils = CommonUtils()

    def get_element(self ,locator):
        try :

          element=self.wait.until(ec.visibility_of_element_located(locator))
          return element

        except Exception as e :
          print(e)
          self.driver.save_screen_shot(f"element_not_found_{self.utils.get_unique_name()}.png")

    def enter_text(self,data,locator):
        element=self.get_element(locator)
        element.send_keys(data)

    def click_element(self,locator):
        element=self.get_element(locator)
        element.click()

    def get_text(self,locator):
        element=self.get_element(locator)
        return element.text

    def select_value_from_dropdown(self,value,locator):
        element=self.get_element(locator)
        select=Select(element)
        select.select_by_visible_text(value)

