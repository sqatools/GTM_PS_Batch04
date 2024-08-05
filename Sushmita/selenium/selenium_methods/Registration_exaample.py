import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options

driver=webdriver.Chrome()
driver.maximize_window()

def get_wait(locator,wait_time=30):
    wait=WebDriverWait(driver,timeout=wait_time)
    element=wait.until(ec.presence_of_element_located(locator))
    return element

def registration_from():
    driver.get("https://grotechminds.com/registration/")
    file=get_wait(locator=(By.NAME,"file")).send_keys("screshot.png")
    print("file name is:",file.text)
    time.sleep(200)
    driver.close()


