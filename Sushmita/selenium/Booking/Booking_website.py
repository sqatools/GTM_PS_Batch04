import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Booking_locator_path import *

driver=webdriver.Chrome()
driver.maximize_window()

def  get_wait(locator,wait_time=30):
    wait=WebDriverWait(driver,timeout=wait_time)
    element=wait.until(ec.presence_of_element_located(locator))
    return element

def Booking_automation():
    driver.get("https://www.booking.com/")
    get_wait(locator=Destination_path).click()
    #dest.send_keys('Bangalore')

    get_wait(locator=Destination_city).click()

    #print(destion.text())
    time.sleep(10)

Booking_automation()
time.sleep(5)
driver.close()
