from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()
driver.maximize_window()

def get_element(locator,wait_time=10):
    wait = WebDriverWait(driver, timeout=wait_time)
    element = wait.until(ec.presence_of_element_located(locator))
    return element

def mouse_action():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    mouse_locator=(By.XPATH,"//div[@id='menu']//a[text()='Free Ebooks']")
    ele_ment=get_element(locator=mouse_locator)
    action=ActionChains(driver)
    action.move_to_element(ele_ment)
    action.perform()

    tests_hub_elem = get_element(locator=(By.XPATH, "//div[@id='menu']//a[text()='Tester’s Hub']"))
    action.move_to_element(tests_hub_elem)
    action.perform()

    time.sleep(5)
    demo_testing_site_elem = get_element(locator=(By.XPATH, "//*[text()='Demo Testing Site']"))
    action.move_to_element(demo_testing_site_elem)
    action.perform()

    time.sleep(5)
    alert_box = get_element(locator=(By.XPATH, "//*[text()='AlertBox']"))
    action.move_to_element(alert_box)
    action.click()
    action.perform()

    time.sleep(5)


mouse_action()

time.sleep(5)