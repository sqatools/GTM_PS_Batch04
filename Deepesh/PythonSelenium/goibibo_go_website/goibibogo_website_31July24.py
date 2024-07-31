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
from website_locators import *


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

def automate_goibibo_website():
    driver.get("https://www.goibibo.com/")

    get_element(locator=close_pop_button).click()
    get_element(locator=from_enter_city_loc).click()

    get_element(locator=from_city_input_field).send_keys("Mumbai (BOM)")
    get_element(locator=(By.XPATH, f"//span[text()='{source_city_name}']")).click()

    get_element(locator=to_city_input_field).send_keys("Bengaluru")
    get_element(locator=(By.XPATH, f"//span[text()='{target_city_name}']")).click()

    get_element(locator=cal_locator).click()
    get_element(locator=(By.XPATH, f"//div[contains(@aria-label, '{depart_date}')]")).click()

    get_element(locator=travellers_class_loc).click()

    # add adults
    for _ in range(1):
        get_element(locator=add_adults_icon).click()

    # add children
    for _ in range(2):
        get_element(locator=add_children_icon).click()

    # add infants
    for _ in range(2):
        get_element(locator=add_infants_icon).click()

    time.sleep(5)

    # select travel class type
    get_element(locator=(By.XPATH, f"//li[text()='{travel_class_type}']")).click()

    get_element(locator=travel_class_done_button).click()
    get_element(locator=search_button).click()

    time.sleep(30)

automate_goibibo_website()


# Home work to automate the booking.com website
