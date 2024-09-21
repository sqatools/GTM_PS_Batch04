import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://grotechminds.com/automate-me/")
element = driver.find_element(By.XPATH,"//h3[contains(text(), 'Registration')]")
action = ActionChains(driver)
action.move_to_element(element)
action.perform()
driver.find_element(By.XPATH,"//h3[contains(text(), 'Registration')]//following::a[contains(text(),'Read More')][1]").click()
time.sleep(5)
windows = driver.window_handles
driver.switch_to.window(windows[1])
time.sleep(5)
print(driver.title)
driver.find_element(By.ID,"fname").send_keys("Kirti")
time.sleep(5)

driver.execute_script("document.getElementById('fname').send_keys('Labana')")
time.sleep(5)

driver.find_element(By.XPATH,"//input[@type='lname']").send_keys("Labana")
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("Kirti.labana@abc.com")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("ZXY@123")

time.sleep(5)