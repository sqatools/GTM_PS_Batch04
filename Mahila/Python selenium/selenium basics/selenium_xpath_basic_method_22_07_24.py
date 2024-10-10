import  time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
#driver.find_element(By.XPATH,"//a[text()='Code Practice']")
#driver.find_element(By.XPATH,"//li/a[text()='Home']").click() #call by parent   ##text method
element = driver.find_element(By.XPATH,"//h1[contains(text(),'Dummy')]")
print(element.text)
driver.find_element(By.XPATH,"//input[contains(@name,'from')]").send_keys("Bglr")