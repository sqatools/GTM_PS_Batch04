import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
# ID Locator
driver.find_element(By.ID,"fromcity")
driver.find_element(By.ID,"destcity")

# TAG_NAME Locator
header_element=driver.find_element(By.TAG_NAME,"h1")
# text method help to print text of any specific element
print(header_element.text)

# LINK TEXT Locator
driver.find_element(By.LINK_TEXT,"Manual Testing").click()

# PARTIAL_LINK_TEXT
element_link_text = driver.find_element(By.PARTIAL_LINK_TEXT,"Software Testing Methods")
element_link_text.click()
time.sleep(10)
driver.close()
