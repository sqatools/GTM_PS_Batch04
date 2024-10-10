

import time


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https:www.google.co.in")
#driver.find_element(By.XPATH,"//textarea[@title='Search']").send_keys("python selenium")
#driver.find_element(By.XPATH,"//textarea[@aria-label='Search']").send_keys("python selenium")
#driver.find_element(By.XPATH,"//textarea[@name='q']").send_keys("pythonselenium")
time.sleep(10)

#we are using * instead of tagname
#//*[@attribute=value]
#//*[@name='q']

driver.find_element(By.XPATH,"//*[@name='q']").send_keys("Python")

#indexing on duplicate XPath
#https://automationbysqatools.blogspot.com/2021/05/dummy-website.html
#(//input[@name='firstname'])[1]
#(//input[@type="radio])[1]

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.XPATH,"//input[@value='radio_123']").click()
driver.find_element(By.XPATH,"(//input[@name='firstname'])[1]").send_keys("keerthi")
driver.find_element(By.XPATH,"(//input[@name='firstname'])[2]").send_keys("latha")
driver.find.element(By.XPATH,"(//input[@type='radio'])[1])").click
time.sleep(10)

#parent XPATH
