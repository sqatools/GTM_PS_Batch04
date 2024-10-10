import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome()
driver.maximize_window()

def get_element(locator,wait_time=10):
    wait=WebDriverWait(driver,timeout=wait_time)
    element=wait.until(ec.presence_of_element_located(locator))
    return element

# def handle_multi_browser():
#     driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
#     ele_locator=(By.XPATH,"//a[text()='Software Testing Principles']")
#     link_element=get_element(locator=ele_locator)
#     link_element.click()
#
#     browser_windows =driver.window_handles
#     print(browser_windows)
#     driver.switch_to.window(browser_windows[1])
#
#     principle_header_locator=(By.XPATH,"//span[text()='Here are the 7 Principles:']")
#     header_element=get_element(locator=principle_header_locator)
#     assert header_element.is_displayed()
#
#     time.sleep(5)
#     driver.close()
#
#     driver.switch_to.window(browser_windows[0])
#     home_locator=(By.XPATH,"//li/a[text()='Home']")
#     home_element=get_element(locator=home_locator)
#     home_element.click()
#     time.sleep(5)
#
# handle_multi_browser()
# driver.close()
def handle_multiple_browser_window_with_loop():
    driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
    links_text_list = [
        "Software Testing Principles",
        "Integration Testing",
        "White Box Testing",
        "Grey Box Testing"
    ]
    for link_text in links_text_list:
        elem_locator = (By.LINK_TEXT, link_text)
        link_element = get_element(locator=elem_locator)
        link_element.click()

    tab_list = driver.window_handles

    for tab in range(1, len(tab_list)):
        driver.switch_to.window(tab_list[tab])
        try:
            principle_header_locator = (By.XPATH, "//span[text()='Here are the 7 Principles:']")
            header_element=get_element(locator=principle_header_locator)
            assert header_element.is_displayed()
        except Exception as e:
            print(f"Element is not  in this windows{tab}")
        #time.sleep(2)
        driver.close()

    driver.switch_to.window(tab_list[0])
    home_locator = (By.XPATH, "//li/a[text()='Home']")
    home_element = get_element(locator=home_locator)
    home_element.click()
    time.sleep(5)

handle_multiple_browser_window_with_loop()

driver.close()