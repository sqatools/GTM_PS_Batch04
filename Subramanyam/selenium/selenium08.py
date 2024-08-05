import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome()
driver.maximize_window()

def get_element(locator,wait_time=10):
    wait=WebDriverWait(driver,timeout=wait_time)
    element=wait.until(ec.presence_of_element_located(locator))
    return element

def handle_alert():
    driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
    alert=Alert(driver)
    get_element(locator=(By.XPATH,"//input[@value='Alert Box']")).click()
    print(alert.text)
    time.sleep(5)
    alert.accept()



handle_alert()

def handle_confirm_box():
    driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
    alert=Alert(driver)
    get_element(locator=(By.XPATH,"//button[@id='button']")).click()
    print(alert.text)
    time.sleep(5)

    alert.accept()
    # print(get_element(locator=(By.XPATH,"// p[ @ id = 'demo']")).text)
    # time.sleep(4)
handle_confirm_box()
def handle_prompt_box():
    driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
    alert = Alert(driver)
    get_element(locator=(By.XPATH,"//button[@id='promptbtn']")).click()
    print(alert.text)
    time.sleep(5)
    alert.send_keys("Subbu")
    alert.accept()
    print(get_element(locator=(By.XPATH,"//p[@id='prompt']")).text)
    time.sleep(5)

handle_prompt_box()
driver.close()