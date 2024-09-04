from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

log = logging.getLogger(__name__)


class WebdriverFactory:
    def __init__(self, browser, headless=None):
        self.browser = browser
        self.headless = headless

    def get_driver(self):
        log.info(f"headless value: {self.headless}")
        print("headless value")
        driver = None
        if self.browser is None:
            chr_option = Options()
            if self.headless:
                chr_option.add_argument('--headless')
            driver = webdriver.Chrome(options=chr_option)
        elif self.browser.lower() == "chrome":
            chr_option = Options()
            if self.headless:
                chr_option.add_argument('--headless')
            driver = webdriver.Chrome(options=chr_option)
        elif self.browser.lower() == "firefox":
            driver = webdriver.Firefox()
        elif self.browser.lower() == "edge":
            driver = webdriver.Edge()
        driver.maximize_window()

        return driver
