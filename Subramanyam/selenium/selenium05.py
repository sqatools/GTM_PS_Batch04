import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver=webdriver.Chrome()
driver.maximize_window()
def get_wait(timeout=10):
    wait=WebDriverWait(driver,timeout)
    return wait
driver.get("https://www.facebook.com/login.php")
username=get_wait().until(ec.element_to_be_clickable((By.NAME,"email")))
username.send_keys("Testing01@gmail.com")

print("username is enable",username.is_enabled())

password=get_wait(timeout=5).until(ec.presence_of_element_located((By.NAME,"pass")))
password.send_keys("Test@1234")
print('password is displayed',password.is_displayed())

driver.find_element(By.XPATH,"//button[@value='1']").click()
time.sleep(10)
print(driver.title)
driver.close()
