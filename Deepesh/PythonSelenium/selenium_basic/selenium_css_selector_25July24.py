"""
CSS Selector :
1). ID  :
    -> #fromcity
    -> input#fromcity

2). Class
    -> div>input.inputtext
    -> button.selected

3). Attribute
    -> input[id='email']
    -> input[placeholder="Password"]
    -> div>input[placeholder="Password"]

4). Combine attribute
    -> input.inputtext[name='email']
    -> input.inputtext[name='pass']
    -> button.selected[name='login']
    -> input[type=radio][id=male]

5). substring in CSS selectors
    -> input[type^=ra][id^=m]
    -> input[id^=from]

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# open website URL
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

driver.find_element(By.CSS_SELECTOR, "input[id^=from]").send_keys("Mumbai")
driver.find_element(By.CSS_SELECTOR, "input[id^=dest]").send_keys("Bangalore")
driver.find_element(By.CSS_SELECTOR, "input[id=billing_name]").send_keys("John")
driver.find_element(By.CSS_SELECTOR, "input[id=billing_phone]").send_keys("54356345634")


time.sleep(5)

driver.get("https://www.facebook.com/")

#driver.find_element(By.CLASS_NAME, "selected").click()
driver.find_element(By.CSS_SELECTOR, ".selected").click()

time.sleep(5)

driver.close()
