
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = "chrome"
if browser == "chrome":
    driver = webdriver.Chrome()
elif browser == "firefox":
    driver = webdriver.Firefox()
elif browser == "edge":
    driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
time.sleep(3)

#driver.find_element(By.input,"radio_123").click(tag name)
driver.find_element(By.NAME, "firstname").send_keys("keerthi")
#(driver.find_element(By.ID, "firstname"))[2].send_keys("latha")
driver.find_element(By.ID, "male").click()
driver.find_element(By.ID, "female").click()
driver.find_element(By.ID, "admorepass").click()
driver.find_element(By.ID, "oneway").click()
driver.find_element(By.ID, "roundtrip").click()
# (how to give  atype ) Tag name as well.
driver.find_element(By.NAME, "fromcity").send_keys("pune")
driver.find_element(By.NAME,"destcity").send_keys("hyderabad")
driver.find_element(By.NAME,"departdate").click()
time.sleep(10)

