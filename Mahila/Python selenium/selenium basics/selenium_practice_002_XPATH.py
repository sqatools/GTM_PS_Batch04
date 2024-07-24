#Advance Xpath method excercise

import  time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

header_element = driver.find_element(By.TAG_NAME,"h1")
print(header_element.text)
driver.find_element(By.XPATH,"//span[contains(text(),'Cab booking')]//preceding-sibling::input[@value='radio_558']").click()

time.sleep(10)
driver.close()