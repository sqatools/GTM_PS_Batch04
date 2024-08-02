import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from locator_booking import *

driver = webdriver.Chrome()
driver.maximize_window()

def select_value(locator,value):
    element=get_element(locator)
    select=Select(element)
    select.select_by_visible_text(value)
def get_element(locator, wait_time=10):
    wait = WebDriverWait(driver, timeout=wait_time)
    element = wait.until(ec.presence_of_element_located(locator))
    return element

def booking_com_website():
    driver.get("https://www.booking.com/flights")
    get_element(locator=one_way).click()

    select_value(locator=seat_type, value="Business")

    get_element(locator=from_destiny).click()
    get_element(locator=from_destiny_type).send_keys("Kochi")
    get_element(locator=(By.XPATH, f"//span[text()='{from_destiny_select}']")).click()

    get_element(locator=To_destiny).click()
    get_element(locator=To_destiny_type).send_keys("Bengaluru")
    get_element(locator=(By.XPATH, f"//span[text()='{To_destiny_select}']")).click()

    get_element(locator=Departure_date).click()
    get_element(locator=Departure_date_select).click()

    get_element(locator=add_members).click()
    get_element(locator=adding_adult_plus).click()

    get_element(locator=adding_children).click()
    get_element(locator=select_child_age_drop).click()
    select_value(locator=select_child_age,value='6')
    get_element(locator=Done_selector).click()

    get_element(locator=submit_selector).click()

    time.sleep(5)

booking_com_website()

driver.close()


