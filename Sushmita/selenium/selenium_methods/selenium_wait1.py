"""
implicit wait : this wait applies on all the elements of the web page.
explicit wait : This wait applies on specific element of the web page with condition
fluent wait  : polling frequency of the element is known as fluent wait, that we
               add as parameter in WebDriverWait method. default value of poll_frequency is 0.5 sec
static wait : When we use time.sleep() method to pause the execution for specific period of time
              then it is known as static wait.
"""
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()

def get_wait(timeout=15):

    wait=WebDriverWait(driver,timeout,poll_frequency=1)
    return wait

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

billing_name=get_wait().until(ec.presence_of_element_located((By.ID,"billing_name")))
billing_name.send_keys("Rahul")

phonenumber =get_wait().until(ec.presence_of_element_located((By.ID,"billing_phone")))
phonenumber.send_keys(23456)

both=get_wait().until(ec.element_to_be_clickable((By.ID,"female")))
both.click()

time.sleep(10)
driver.close()
