import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locator_purchase_website import *

driver = webdriver.Chrome()
driver.maximize_window()


def get_element(locator, wait_time=10):
    wait = WebDriverWait(driver, timeout=wait_time)
    element = wait.until(ec.presence_of_element_located(locator))
    return element

def purchase_website():
    driver.get("https://shopping.rediff.com/?sc_cid=inhome_icon")

    get_element(locator=search_type_locator).send_keys(search_data)
    get_element(locator=click_search_locator).click()
    get_element(locator=product_locator).click()
    get_element(locator=pin_locator).click()
    get_element(locator=pin_locator).send_keys(pin_value)
    get_element(locator=check_loc).click()
    get_element(locator=buy_now_loc).click()
    get_element(locator=place_order_loc).click()


    time.sleep(5)

purchase_website()

driver.close()


