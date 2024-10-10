import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

def get_element(locator, wait_time=30):
    wait = WebDriverWait(driver, timeout=wait_time)
    element = wait.until(ec.presence_of_element_located(locator))
    return element

def handle_iframe():
    driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
    iframe_locator = (By.NAME, "globalSqa")
    iframe_element = get_element(locator=iframe_locator)
    driver.switch_to.frame(iframe_element)

    contact_email_locator = (By.XPATH, "//div[@class='header_mail']")
    contact_email_element = get_element(contact_email_locator)
    print("contact email :", contact_email_element.text)

    mobile_menu_loc = (By.ID, "mobile_menu_toggler")
    mobile_menu_ele = get_element(mobile_menu_loc)
    mobile_menu_ele.click()
    time.sleep(3)

    cheetsheet_loc = (By.XPATH, "//div[@id='mobile_menu']//a[text()='CheatSheets']")
    cheetsheet_element = get_element(cheetsheet_loc)
    cheetsheet_element.click()
    time.sleep(5)

    driver.switch_to.default_content()
    cheetsheet_loc_top_menu = (By.XPATH, "//div[@id='menu']//a[text()='CheatSheets']")
    cheetsheet_top_menu_elm = get_element(cheetsheet_loc_top_menu)
    cheetsheet_top_menu_elm.click()




handle_iframe()
time.sleep(10)
driver.close()
