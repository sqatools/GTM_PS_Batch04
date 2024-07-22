
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
header_element = driver.find_element(By.TAG_NAME, "h1")

driver.find_element(By.XPATH,"(//input[@type='radio'])[2]").click()
driver.find_element(By.ID,"firstname").send_keys("Mahila")

driver.find_element(By.XPATH,"(//input[@name='firstname'])[2]").send_keys("Mahesh")
driver.find_element(By.ID,"female").click()

driver.find_element(By.ID,"roundtrip").click()

driver.find_element(By.ID, "fromcity").send_keys("Banglore")

driver.find_element(By.ID, "destcity").send_keys("Kerala")

driver.find_element(By.ID,"eamil").click()

driver.find_element(By.ID,"billing_name").send_keys("Mahila")
driver.find_element(By.ID,"billing_phone").send_keys("7909175279")
driver.find_element(By.ID,"billing_email").send_keys("mahila@gmail.com")
driver.find_element(By.ID,"billing_address").send_keys("A-128,banglore")

driver.find_element(By.ID,"billing_country").send_keys("India")

driver.find_element(By.ID,"postcode").send_keys("695141")
driver.find_element(By.XPATH,"(//input[@type='checkbox'])[3]").click()


