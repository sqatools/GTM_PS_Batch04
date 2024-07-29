import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://collegedunia.com/india-colleges")
element_list = driver.find_elements(By.XPATH, "//div[contains(@class, 'clg-column')]/a")
for element in element_list:
    print(element.get_attribute("title"))
    print(element.get_attribute("href"))