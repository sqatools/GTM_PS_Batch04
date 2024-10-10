import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.NAME,"firstname").send_keys("Nikhila")
#driver.find_element(By.NAME,"firstname").send_keys("Joy")
#driver.find_element(By.ID,"female")
driver.find_element(By.ID,"eamil").click()
driver.find_element(By.ID,"billing_name").send_keys("Nikhila Joy")
driver.find_element(By.ID,"billing_phone").send_keys("8564367890")
driver.find_element(By.ID,"billing_email").send_keys("nikhilajoy11@gmail.com")
driver.find_element(By.ID,"billing_address").send_keys("agfdyfgjg")
driver.find_element(By.ID,"postcode").send_keys("646664")
driver.find_element(By.LINK_TEXT,"Python Selenium").click()
driver.find_element(By.LINK_TEXT,"Home").click()
#driver.find_element(By.ID,"radio_558")
time.sleep(10)