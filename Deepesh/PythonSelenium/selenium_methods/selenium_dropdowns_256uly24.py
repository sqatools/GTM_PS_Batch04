import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

def get_element(locator, wait_time=30):
    wait = WebDriverWait(driver, timeout=wait_time)
    element = wait.until(ec.presence_of_element_located(locator))
    return element

def select_dropdown_value(locator, value):
    element = get_element(locator)
    select = Select(element)
    select.select_by_visible_text(value)

def handle_dropdown():
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    country_dd_locator = (By.ID, "billing_country")
    country_dd_elem = get_element(locator=country_dd_locator)
    select_obj = Select(country_dd_elem)
    #select_obj.select_by_visible_text("Antarctica")
    #select_obj.select_by_value("BB")
    select_obj.select_by_index(3)
    time.sleep(5)

    add_pass_dd_locator = (By.ID, "admorepass")
    select_dropdown_value(locator=add_pass_dd_locator, value="Add 3 more passenger (200%)")
    time.sleep(5)

handle_dropdown()



driver.close()

