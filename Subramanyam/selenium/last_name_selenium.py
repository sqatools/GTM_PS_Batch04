import time

from selenium import webdriver
from  selenium.webdriver.common.by import By

subbu= webdriver.Chrome()
subbu.maximize_window()
subbu.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
time.sleep(5)
subbu.find_element(By.ID,"firstname").send_keys("Dasini")

time.sleep(10)
subbu.close()