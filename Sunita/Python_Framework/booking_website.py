import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime
from booking_locator import *

headless_execution =False
option = Options()
option.add_argument("--disable-notifications")
if headless_execution:
    option.add_argument("--headless")
driver = webdriver.Chrome(options=option)
driver.maximize_window()

cur_dire = os.getcwd()
images_folder_path = os.path.join(cur_dire, "images")
print(images_folder_path)


def get_element(locator, wait_time=30):
    wait = WebDriverWait(driver, timeout=wait_time)
    element = wait.until(ec.presence_of_element_located(locator))
    return element

def get_latest_date_val():
   return datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

def automate_booking_website():
    driver.get("https://www.booking.com/")

    get_element(locator=Where_are_you_going).click()
    get_element(locator=Where_are_you_going).send_keys("Pune")
    get_element(locator=(By.XPATH,))


automate_booking_website()