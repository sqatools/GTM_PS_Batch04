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

def get_element(locator,timeout=15,wait_cond=ec.presence_of_element_located):
    return get_wait(timeout=15).until(wait_cond(locator))

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# website_header=get_wait().until(ec.presence_of_element_located((By.XPATH,"//h1[text()=' Dummy Ticket Booking Website']")))
# print(website_header)
#
# billing_name=get_wait().until(ec.presence_of_element_located((By.ID,"billing_name")))
# billing_name.send_keys("Rahul")
#
# phonenumber =get_wait().until(ec.presence_of_element_located((By.ID,"billing_phone")))
# phonenumber.send_keys(23456)
#
# both=get_wait().until(ec.element_to_be_clickable((By.ID,"female")))
# both.click()
website_header=get_element((By.XPATH,"//h1[text()=' Dummy Ticket Booking Website']"))
assert website_header

billing_name=get_element((By.ID,"billing_name"),wait_cond=ec.element_to_be_clickable)
billing_name.send_keys('Rahul')

phonenumber=get_element((By.ID,"billing_phone"),wait_cond=ec.visibility_of_element_located)
phonenumber.send_keys(3456)

both=get_element((By.XPATH,"//span[text()='Both']//preceding-sibling::input[1]"),wait_cond=ec.element_to_be_clickable)
both.click()

time.sleep(10)
driver.close()
