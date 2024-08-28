import os.path
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from utlities.utility_tool import CommonUtils
from selenium.webdriver.common.action_chains import ActionChains


class SeleniumBase:

    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.utils = CommonUtils()
        self.logs_folder_path = self.utils.create_unique_folder_logs()
        self.log = logging.getLogger(__name__)

    def take_screenshot_path(self, filename):
        filepath = os.path.join(self.logs_folder_path, f"{filename}_{self.utils.get_unique_name()}.png")
        self.log.info(f"screenshots : {filepath}")
        self.driver.save_screenshot(filepath)

    def get_element(self, locator):
        try:
            element = self.wait.until(ec.visibility_of_element_located(locator))
            self.log.info(f"found element with the locator : {locator}")
            return element
        except Exception as e:
            self.log.info(f"{locator}  {e}")
            # self.take_screenshot_path(filename="Element not found")

    def enter_text(self, data, locator):
        try:

            element = self.get_element(locator)
            self.log.info(f"Enter value : {data}, for {locator}")
            element.send_keys(data)
        except Exception as e:
            self.log.info(f"{locator}  {e}")
            self.take_screenshot_path(filename="Element not found")
            raise

    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def clear_fields(self, locator):
        element = self.get_element(locator)
        element.clear()

    def get_text(self, locator):
        element = self.get_element(locator)
        return element.text

    def select_from_dropdown(self, value, locator):
        element = self.get_element(locator)
        select = Select(element)
        select.select_by_visible_text(value)

    def move_to_element(self, locator):
        element = self.get_element(locator)
        action = ActionChains.move_to_element(element)
        action.perform()
