"""
pip install selenium -tool using for automation.

"""
#import libabries from selenium

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  #which browser we need to pick
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.google.co.in")
driver.find_element(By.NAME, "q").send_keys("Python Selenium")
driver.find_element(By.NAME, "btnK").click()
time.sleep(10)
driver.close()

###########################################################################

"""
browser = "chrome"
if browser == "chrome":
    driver = webdriver.Chrome()
elif browser == "firefox":
    driver = webdriver.Firefox()
elif browser == "edge":
    driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.google.co.in")
driver.find_element(By.NAME, "q").send_keys("Python Selenium")
driver.find_element(By.NAME, "btnK").click()
time.sleep(10)
driver.close()

"""

#F12--> Directly open code for particular element