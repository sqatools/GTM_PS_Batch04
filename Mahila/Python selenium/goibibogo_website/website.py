import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locator_file import *

driver = webdriver.Chrome()
driver.maximize_window()

def get_element(locator, wait_time=30):
    wait = WebDriverWait(driver, timeout=wait_time)
    element = wait.until(ec.presence_of_element_located(locator))
    return element
def web_driver():
    driver.get("https://www.goibibo.com/")

    get_element(locator=popup_close).click()
    get_element(locator=from_destiny_click).click()

    get_element(locator=from_destiny_text).send_keys("Mumbai")
    get_element(locator=(By.XPATH, f"//span[text()='{from_destiny_name}']")).click()

    get_element(locator=To_destiny_text).send_keys("Bengaluru")
    get_element(locator=(By.XPATH, f"//span[text()='{To_destiny_name}']")).click()ll



    time.sleep(10)

web_driver()
driver.close()


