import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/p/home.html")
driver.find_element(By.LINK_TEXT,"Dummy Website").click()
driver.find_element(By.XPATH,"//a[text()='Python Selenium']").click()
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH,"//a[text()='Code Practice']//preceding::a[text()='Home']").click()
driver.find_element(By.XPATH,"//div[text()=' Dummy Website ']").click()
element_lst=driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for element in element_lst:
    print("Element is selected1: ",element.is_selected())
    element.click()
    print("Element is selected2: ", element.is_selected())
    print(element.get_attribute("type"))
time.sleep(10)
driver.close()