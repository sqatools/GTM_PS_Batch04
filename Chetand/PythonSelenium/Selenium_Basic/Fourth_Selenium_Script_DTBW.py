import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.XPATH, "(//input[@value='radio_123'])").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "(//input[@id='firstname'])[1]").send_keys("Chetan")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "(//input[@id='firstname'])[2]").send_keys("Dhok")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "(//input[@name='birthday'])").send_keys("08-10-1992")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "(//input[@id='male'])").click()
driver.implicitly_wait(10)
##driver.find_element(By.XPATH, "(//input[@id='admorepass'])").send_keys(" I'm the only one traveler ")##
driver.find_element(By.XPATH, "(//input[@id='oneway'])").click()
driver.implicitly_wait(10)
driver.find_element(By.ID, "fromcity").send_keys("Pune")
driver.implicitly_wait(10)
driver.find_element(By.ID, "destcity").send_keys("Nagpur")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "(//input[@id='departdate'])").send_keys("22-07-2024")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "(//input[@name='returndate'])").send_keys("22-07-2024")
driver.implicitly_wait(10)
##driver.find_element(By.XPATH, "(//input[@id='departdate'])").send_keys("22-07-2024")##
driver.find_element(By.XPATH, "(//input[@id='whatsapp'])").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "(//input[@id='billing_name'])").send_keys("Chetan Dhok")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "(//input[@id='billing_phone'])").send_keys("8738332323")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "(//input[@id='billing_email'])").send_keys("crdhok@gmail.com")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "(//input[@id='billing_address'])").send_keys("36 Avenue Nagpur")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "(//input[@name='postcode'])").send_keys("440015")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "(//input[@id='Prefecture'])").send_keys("Maharashtra")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "(//input[@id='street_address1'])").send_keys("Wall street")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "(//input[@value='checkbox'])").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "(//input[@value='checkbox'])[2]").click()

time.sleep(100)