from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH,"//*[@name='user-name']").send_keys('standard_user')
driver.find_element(By.XPATH,"//*[@name='password']").send_keys('secret_sauce')
driver.find_element(By.XPATH,"//input[@id='login-button']").click()


driver.find_element(By.XPATH,"//button[text()='Add to cart']").click()
driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
driver.find_element(By.XPATH,"//button[contains(text(),'Open Menu')]").click()
#driver.find_element(By.LINK_TEXT,"About").click()
driver.find_element(By.LINK_TEXT,"Logout").click()

time.sleep(10)
