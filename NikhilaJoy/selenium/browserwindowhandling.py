from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
#from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome()
driver.maximize_window()

def get_element(locator,wait_time=15):
    wait=WebDriverWait(driver ,timeout=wait_time)
    element=wait.until(ec.presence_of_element_located(locator))
    return element
def browser_handling():
    driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
    ele_locator=(By.XPATH,"//a[text()='Software Testing Principles']")
    ele_ment=get_element(locator=ele_locator)
    ele_ment.click()

    browser_windows=driver.window_handles
    print(browser_windows)
    driver.switch_to.window(browser_windows[1])
    driver.find_element(By.XPATH,"//div[@class='navigate'][1]").click()

    time.sleep(2)
    driver.close()
browser_handling()


