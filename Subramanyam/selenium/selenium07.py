import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()

def get_element(locator,wait_time=10):
    wait=WebDriverWait(driver,timeout=wait_time)
    element=wait.until(ec.presence_of_element_located(locator))
    return element
def handle_mouse_action():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    freebook_element=get_element(locator=(By.XPATH,"//li[@id='menu-item-1561']//preceding::a[text()='Tester’s Hub']"))
    action=ActionChains(driver)
    action.move_to_element(freebook_element)
    action.perform()

    element2=(By.XPATH,"//*[text()='AngularJS Protractor Practice Site']")
    ele=get_element(element2)
    action.move_to_element(ele)
    action.perform()
    time.sleep(5)

    element3=get_element(locator=(By.XPATH,"//*[text()='Multiform']"))
    action.move_to_element(element3)
    action.click()
    action.perform()
    time.sleep(5)
handle_mouse_action()
driver.close()