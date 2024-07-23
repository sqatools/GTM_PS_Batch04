import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/p/home.html#")
driver.find_element(By.LINK_TEXT,"Dummy Website").click()
driver.find_element(By.XPATH,"//input[@value='radio_678']").click()
driver.find_element(By.XPATH,"//input[@value='radio_123']").click()
driver.find_element(By.NAME,"firstname").send_keys("subbu")
driver.find_element(By.ID,"male").click()
driver.find_element(By.ID,"roundtrip").click()
driver.find_element(By.ID,"fromcity").send_keys("pune")
driver.find_element(By.ID,"destcity").send_keys("Delhi")
driver.find_element(By.ID,"whatsapp").click()
driver.find_element(By.ID,"billing_name").send_keys("subramanyam")
driver.find_element(By.ID,"billing_phone").send_keys("9966466046")
driver.find_element(By.ID,"billing_email").send_keys("subramanyam@gmail.com")
driver.find_element(By.ID,"billing_address").send_keys("Bengalore")
driver.find_element(By.ID,"postcode").send_keys("517501")
driver.find_element(By.ID,"street_address1").send_keys("Marathalli")
time.sleep(10)
driver.close()