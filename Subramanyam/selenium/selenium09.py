import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://grotechminds.com/automate-me/")
element=driver.find_element(By.XPATH,"//h3[contains(text(), 'Registration')]")
action=ActionChains(driver)
action.move_to_element(element)
action.perform()
driver.find_element(By.XPATH,"//h3[contains(text(), 'Registration')]//following::a[contains(text(),'Read More')][1]").click()

time.sleep(5)