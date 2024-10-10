import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
#Link Test
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.LINK_TEXT,"Manual Testing").click()

#partical link test

element=driver.find_element(By.PARTIAL_LINK_TEXT,"Testing Principles")
element.click()

time.sleep(10)
