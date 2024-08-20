"""
pip install selenium
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
"""

browser="chrome"
if browser=="chrome":
    driver=webdriver.Chrome()
elif browser=="firefox":
    driver=webdriver.Firefox()
elif browser=="edge":
    driver=webdriver.Edge()

driver.maximize_window()# maximize the browser windows

#driver.implicitly_wait(10) # implicit wait applies on all web elements
driver.get("https://www.google.com/")
# find_element method, help to find element in current web page with the help of locator
# and return the element
t1=time.time()
try:
    element = driver.find_element(By.NAME,"q")
except:
    pass
t2=time.time()
print("total time take :", t2-t1)
print(element)
# send_keys method, send data to text field
element.send_keys("Python Selenium")
driver.find_element(By.NAME,"btnK").click()
time.sleep(15)
driver.close()
