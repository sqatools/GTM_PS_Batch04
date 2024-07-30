import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
#driver.implicitly_wait(10)


# driver.get("https://www.naukri.com/")
# ele=driver.find_element(By.LINK_TEXT,"Jobs")
# #ele.click()
# ele1=driver.find_element(By.XPATH,"//div[text()='Marketing jobs']")
# ele1.click()
# browser_window=driver.window_handles
# driver.switch_to.window(browser_window[1])

#driver.switch_to.window(browser_window[0])

def get_element(locator, wait_time=30):
    wait = WebDriverWait(driver, timeout=wait_time)
    element = wait.until(ec.presence_of_element_located(locator))
    return element

def handle_browser_window():
    driver.get("https://www.tutorialspoint.com/index.htm")
    ele_locator=(By.LINK_TEXT,"Javascript")
    browse_ele=get_element(locator=ele_locator)
    browse_ele.click()

    # browser_windows=driver.window_handles
    # driver.switch_to.window(browser_windows[1])

    header_loc=(By.XPATH,"//h1[text()='JavaScript Tutorial']")
    header_ele=get_element(locator=header_loc)
    assert header_ele
    # driver.close()
    # driver.switch_to.window(browser_windows[0])

    # ele_locator=(By.XPATH,"//h1[@class='hero__title ']")
    # browse_ele=get_element(locator=ele_locator)
    # browse_ele.is_displayed()
    time.sleep(10)

handle_browser_window()
driver.close()
