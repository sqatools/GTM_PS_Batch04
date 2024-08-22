import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.flipkart.com")
driver.find_element(By.XPATH,"(//a[@title='Login'])[2]").click()
time.sleep(5)