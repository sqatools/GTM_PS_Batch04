from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


class SeleniumBase:

    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_element(self, locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        # self.log.info(f"found element with the locator : {locator}")
        return element

        # self.log.info(f"{locator}  {e}")
        # self.take_screenshot_path(filename="Element not found")

    def enter_text(self, data, locator):
        element = self.get_element(locator)
        element.send_keys(data)

        # self.log.info(f"{locator}  {e}")
        # self.take_screenshot_path(filename="Element not found")

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

    def handle_browser_window(self, locator):
        element = self.get_element(locator)
        element.click()
        browser_windows = self.driver.window_handles
        # print(browser_windows)
        self.driver.switch_to.window(browser_windows[1])

    def handle_alert(self, locator):
        alert = Alert(self.driver)
        element = self.get_element(locator)
        element.click()
        alert.accept()
