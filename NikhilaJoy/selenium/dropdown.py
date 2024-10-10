from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()


def get_element(locator,wait_time=15):
    wait=WebDriverWait(driver,timeout=wait_time)
    element=wait.until(ec.presence_of_element_located(locator))
    return element
def dropdown_handling_without_fn():
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    drp_locator=(By.ID,"admorepass")
    ele_ment=get_element(locator=drp_locator)
    select_obj=Select(ele_ment)
    select_obj.select_by_index(3)
    time.sleep(5)
    driver.close()

dropdown_handling_without_fn()
