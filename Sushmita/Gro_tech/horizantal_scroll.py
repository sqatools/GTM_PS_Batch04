import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://grotechminds.com/vertical-scrolling/")
# driver.execute_script("window.scrollBy(0,5000)","")
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")
# time.sleep(10)
# driver.execute_script("window.scrollBy(5000,0)","")
element = driver.find_element(By.XPATH, "//a[text()='Practice5']")
driver.execute_script("argument[0].scrollIntoView()", element)
time.sleep(10)
driver.close()
