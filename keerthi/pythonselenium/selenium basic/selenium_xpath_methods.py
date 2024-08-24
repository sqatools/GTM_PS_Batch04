import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.find_element(By.XPATH, "//textarea[@title='Search']").send_keys("Python Selenium")
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.XPATH, "//input[@id='firstname']").send_keys("keerthi")

driver.find_element(By.XPATH, "//input[@id='firstname'][2]").send_keys("latha")
driver.find_element(By.XPATH,"//input[@id='male']").click()
driver.find_element(By.XPATH, "//input[@id='female']").click()

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
time.sleep(10)

handle_dropdown()



