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
# implicit wait applies on all the elements of the web page by default
# driver.implicitly_wait(10)

# explicit wait applies on specific element of the web page with condition
wait = WebDriverWait(driver, 15, poll_frequency=1)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

t1 = time.time()
try:
    element = wait.until(ec.presence_of_element_located((By.ID, "billing_name")))
    element.send_keys("Rahul Gupta")
except Exception as e:
    print(e)
t2 = time.time()

print("total time taken :", t2-t1)

a1 = time.time()
try:
    phone = driver.find_element(By.ID, "billing_phone")
    phone.send_keys(5654645645)
except Exception as e:
    print(e)
a2 = time.time()

print("total time take phone_number :",a2-a1 )

time.sleep(10) # static wait
driver.close()


