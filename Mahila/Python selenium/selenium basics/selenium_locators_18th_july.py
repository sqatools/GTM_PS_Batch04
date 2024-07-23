
import time

from selenium import
from selenium.webdriver.common.by import By

"""
LOCATORS :::::::::::::::::
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
"""
browser = "chrome"
if browser == "chrome":
    driver = webdriver.Chrome()   #open a browser
elif browser == "firefox":
    driver = webdriver.Firefox()
elif browser == "edge":
    driver = webdriver.Edge()

driver.maximize_window() # maximize the browser windows
driver.implicitly_wait(10) # implicit wait applies on all web elements
#wait for 10 sec to look for each element if it is there it will work if it is not there it will give error after 10 sec

# get method open URL in browser
driver.get("https://www.google.co.in")
# find_element method, help to find element in current web page with the help of locator
# and return the element
t1 = time.time()
try:
    element = driver.find_element(By.NAME, "q1")
except:
    pass
t2 = time.time()
print("total time take :", t2-t1)
print(element)
# send_keys method, send data to text field
element.send_keys("Python Selenium")
# click method, perform click operation on specific element
driver.find_element(By.NAME, "btnK").click()
# time.sleep help to hold the execution for specific amount of time
time.sleep(10)
# close method close the existing running browser
driver.close()


#HOW to find any particular element(link,button, checkbox,text) has an ID
