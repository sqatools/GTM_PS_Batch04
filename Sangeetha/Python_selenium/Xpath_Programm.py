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
driver.find_element(By.XPATH,"(//input[@type='radio'])[2]").click()
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@name='firstname'])[1]").send_keys("sangeetha")
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@name='firstname'])[2]").send_keys("kokkonda")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='birthday']").send_keys("07/21/2024")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='female']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='oneway']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='fromcity']").send_keys("chennai")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='destcity']").send_keys("banglore")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='departdate']").send_keys("07/21/2024")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='returndate']").send_keys("07/30/2024")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='visadate']").send_keys("07/23/2024")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='whatsapp']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='billing_name']").send_keys("sangeetha")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='billing_phone']").send_keys("9059993936")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='billing_email']").send_keys("sangeetha123@gmail.com")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='billing_address']").send_keys("No119,f4,sai homes,chennai")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='postcode']").send_keys("600053")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='Prefecture']").send_keys("Tamilnadu")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='street_address1']").send_keys("No119,f4,sai homes,chennai")
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@type='checkbox'])[3]").click()

time.sleep(5)