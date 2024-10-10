import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
header_element = driver.find_element(By.TAG_NAME, "h1")
print(" Dummy Ticket Booking Website")
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@type='radio'])[4]").click()
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@name='firstname'])[1]").send_keys("Swapna")
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@name='firstname'])[2]").send_keys("S")
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@id='birthday'])").send_keys("19-05-1990")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='female']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='roundtrip']").click()
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@name='fromcity'])").send_keys("Blore")
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@name='destcity'])").send_keys("Mumbai")
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@name='departdate'])").send_keys("01-08-2024")
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@name='returndate'])").send_keys("10-08-2024")
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@id='visadate'])").send_keys("05-08-2024")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='eamil']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='billing_name']").send_keys("Swapna")

time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='billing_phone']").send_keys("8000613536")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='billing_email']").send_keys("abc@gmail")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='billing_address']").send_keys("Hassan")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='postcode']").send_keys("641009")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='checkbox'][1]").click()
time.sleep(5)

