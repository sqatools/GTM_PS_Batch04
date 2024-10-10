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

driver = webdriver.Chrome()
driver.maximize_window()


# explicit wait applies on specific element of the web page with condition
def get_wait(timeout=15):
    wait = WebDriverWait(driver, timeout, poll_frequency=1)
    return wait


def get_element(locator, timeout=15, wait_cond=ec.presence_of_element_located):
    return get_wait(timeout).until(wait_cond(locator))

# Locators section
header_loc = (By.XPATH, "//h1[@align='center']")
bill_name_loc = (By.ID, "billing_name")
phone_num_loc = (By.ID, "billing_phone")
email_loc = (By.ID, "billing_email")

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

website_header = get_element(header_loc)
assert website_header

billing_name = get_element(bill_name_loc, wait_cond=ec.element_to_be_clickable)
billing_name.send_keys('Akshay')

phone_number = get_element(phone_num_loc, wait_cond=ec.visibility_of_element_located)
phone_number.send_keys("65464564656")

email_address = get_element(email_loc, wait_cond=ec.presence_of_element_located, timeout=20)
email_address.send_keys("akshay@gmail.com")


time.sleep(5)
driver.close()
