
import os
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from utilities.utility_tools import CommonUtils


class SeleniumBase:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.utils = CommonUtils()
        self.logs_folder_path = self.utils.create_unique_folder_logs()
        self.log = logging.getLogger(__name__)

    def take_screenshot(self, filename):
        filepath = os.path.join(self.logs_folder_path, f"{filename}_{self.utils.get_unique_name()}.png")
        self.log.info(f"screenshot: {filepath}")
        self.driver.save_screenshot(filepath)

    def get_element(self, locator):
        try:
            element = self.wait.until(ec.visibility_of_element_located(locator))
            self.log.info(f"found element with locator: {locator}")
            return element
        except Exception as e:
            self.log.info(f"{locator} {e}")
            self.take_screenshot(filename='element_not_found')

    def get_elements_list(self, locator):
        try:
            elements_list = self.wait.until(ec.visibility_of_all_elements_located(locator))
            self.log.info(f"found element with locator: {locator}")
            return elements_list
        except Exception as e:
            self.log.info(f"{locator} {e}")
            self.take_screenshot(filename='element_not_found')

    def enter_text(self, data, locator):
        try:
            element = self.get_element(locator)
            self.log.info(f"Enter value: {data},  to the element: {locator}")
            element.send_keys(data)
        except Exception as e:
            self.log.info(f"{locator} {e}")
            self.take_screenshot(filename='element_not_found')
            raise

    def click_element(self, locator):
        try:
            element = self.get_element(locator)
            self.log.info(f"clicking to the element: {locator}")
            element.click()
        except Exception as e:
            self.log.info(f"{locator} {e}")
            self.take_screenshot(filename='element_not_found')
            raise

    def get_text(self, locator):
        try :
            element = self.get_element(locator)
            self.log.info(f"getting text from the element: {locator}")
            return element.text
        except Exception as e:
            self.log.info(f"{locator} {e}")
            self.take_screenshot(filename='element_not_found')
            raise

    def select_value_from_dropdown(self, value, locator):
        try:
            element = self.get_element(locator)
            select = Select(element)
            self.log.info(f"selecting value: {value} from the dropdown: {locator}")
            select.select_by_visible_text(value)
        except Exception as e:
            self.log.info(f"{locator} {e}")
            self.take_screenshot(filename='element_not_found')
            raise