from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()

def get_wait(locator,waittime=30):
    wait=WebDriverWait(driver,timeout=waittime)
    element=wait.until(ec.presence_of_element_located(locator))
    return element

def handle_browser():
    driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
    ele_locator=(By.XPATH,"//a[text()='Software Testing Principles']")
    link_element=get_wait(locator=ele_locator)
    link_element.click()

    browser_windows=driver.window_handles
    print(browser_windows)
    driver.switch_to.window(browser_windows[1])

    header_locator=(By.XPATH,"//span[text()='Here are the 7 Principles:']")
    header_element= get_wait(locator=header_locator)
    assert  header_element.is_displayed()

    search_locator=(By.NAME,"q")
    search_ele=get_wait(locator=search_locator)
    search_ele.send_keys('python selenium')

    time.sleep(5)
    driver.close()

    driver.switch_to.window(browser_windows[0])
    home_locator=(By.XPATH,"//li//a[text()='Home']")
    home_element=get_wait(locator=home_locator)
    home_element.click()
    time.sleep(5)

handle_browser()

def handle_multipple_browser_loop():
    driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
    link_test_list=['Software Testing Principles',
               'Software Testing Methods',
               'Black Box Testing',
               'Grey Box Testing']

    for link_text in link_test_list:
        ele_locator=(By.LINK_TEXT,link_text)
        link_element=get_wait(locator=ele_locator)
        link_element.click()

#handle_multipple_browser_loop()
time.sleep(10)
driver.close()






