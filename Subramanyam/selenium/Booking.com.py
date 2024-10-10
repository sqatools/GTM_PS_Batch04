import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from booking_locator import *
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.maximize_window()
def get_element(locator,wait_time=30):
    wait=WebDriverWait(driver,timeout=wait_time)
    element=wait.until(ec.presence_of_element_located(locator))
    return element
def select_value(locator,value):
    element=get_element(locator)
    select=Select(element)
    select.select_by_visible_text(value)
def booking_com():
    driver.get(url)
    get_element(locator=one_way_flight).click()
    #get_element(locator=flight_class)
    select_value(locator=flight_class,value="Premium economy")
    get_element(locator=From).click()
    #get_element(locator=From).clear()
    time.sleep(5)
    try:

        element=get_element(locator=cancel_already_one)

        if element.is_displayed():
            element.click()
        else:
            pass
    except Exception as e:
        print(e)
    get_element(locator=from_airport).send_keys("Chennai")
    get_element(locator=from_city_in_list).click()
    get_element(locator=To).click()
    get_element(locator=to_airport).send_keys("bangalore")
    get_element(locator=to_city_in_list).click()
    get_element(locator=Choose_departure_date).click()
    get_element(locator=next_month).click()
    get_element(locator=Aug_14).click()
    get_element(locator=Adult).click()
    time.sleep(2)
    for i in range(2):
        get_element(locator=add_adult).click()
    get_element(locator=Done_button).click()
    get_element(locator=search_button).click()
    driver.save_screenshot("C:\\Users\\subra\\OneDrive\\Desktop\\selenium\\Screenshot\\Booking_com.png")


    time.sleep(3)
booking_com()
