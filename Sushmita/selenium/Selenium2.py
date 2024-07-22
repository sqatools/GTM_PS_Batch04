from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.ID,"firstname").send_keys("Sush")
driver.find_element(By.NAME,"firstname").send_keys("Shalin")
driver.find_element(By.ID,"female").click()
driver.find_element(By.ID,"oneway").click()
driver.find_element(By.ID,"fromcity").send_keys("Bangalore")
driver.find_element(By.NAME,"destcity").send_keys("Delhi")
driver.find_element(By.ID,"whatsapp").click()
driver.find_element(By.ID,"billing_name").send_keys("Bhumika")
driver.find_element(By.ID,"billing_phone").send_keys(34567)
driver.find_element(By.ID,"billing_email").send_keys("34567@gmail.com")
driver.find_element(By.ID,"billing_address").send_keys('shenanigan')



time.sleep(10)
driver.close()

