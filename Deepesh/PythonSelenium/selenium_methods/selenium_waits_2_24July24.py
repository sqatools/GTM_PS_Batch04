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


driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# wait for the text be preset
# website_header = get_wait().until(ec.text_to_be_present_in_element((By.XPATH, "//h1[@align='center']"), "Dummy1"))
# print(website_header)
# assert website_header
#
# billing_name = get_wait().until(ec.presence_of_element_located((By.ID, "billing_name")))
# billing_name.send_keys("Rahul Gupta")
#
# phone_number = get_wait(timeout=20).until(ec.visibility_of_element_located((By.ID, "billing_phone")))
# phone_number.send_keys("9867787687")
#
# email_address = get_wait().until(ec.element_to_be_clickable((By.ID, "billing_email")))
# email_address.send_keys("rahul@gmail.com")

website_header = get_element((By.XPATH, "//h1[@align='center']"))
assert website_header

billing_name = get_element((By.ID, "billing_name"), wait_cond=ec.element_to_be_clickable)
billing_name.send_keys('Akshay')

phone_number = get_element((By.ID, "billing_phone"), wait_cond=ec.visibility_of_element_located)
phone_number.send_keys("65464564656")

email_address = get_element((By.ID, "billing_email"), wait_cond=ec.presence_of_element_located, timeout=20)
email_address.send_keys("akshay@gmail.com")


time.sleep(5)
driver.close()
