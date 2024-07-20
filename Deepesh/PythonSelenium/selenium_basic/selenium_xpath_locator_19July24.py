"""
pip install selenium
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# open website URL
driver.get("https://www.google.co.in")
# driver.find_element(By.XPATH, "//textarea[@title='Search']").send_keys("Python Selenium")
# driver.find_element(By.XPATH, "//textarea[@aria-label='Search']").send_keys("Python Selenium")
#driver.find_element(By.XPATH, "//textarea[@name='q']").send_keys("Python Selenium")
driver.find_element(By.XPATH, "//*[@title='Search']").send_keys("Python Selenium")

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.XPATH, "(//input[@name='firstname'])[1]").send_keys("Rahul")
driver.find_element(By.XPATH, "(//input[@name='firstname'])[2]").send_keys("Gupta")

time.sleep(10)
