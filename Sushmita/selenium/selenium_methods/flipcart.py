from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()

def get_wait(locator,wait_time=30):
    wait=WebDriverWait(driver,timeout=wait_time)
    element = wait.until(ec.presence_of_element_located(locator))
    return element


def fiip_cart():

    driver.get("https://www.flipkart.com/")
    login=(By.XPATH,"//div[@class='H6-NpN _3N4_BX']")
    log_but=get_wait(locator=login)
    action=ActionChains(driver)
    action.move_to_element(log_but)
    action.perform()

fiip_cart()


# def select_dropdown(locator,value):
#     element=get_wait(locator)
#     select_obj= Select(element)
#     select_obj.select_by_visible_text(value)
#
# def dropdowm_ele():
#     driver.get("https://www.naukri.com/")
#     geeek_loca=(By.XPATH, "https://www.naukri.com/")
#     greek_ele=get_wait(locator=geeek_loca)
#     greek_ele.click()
    # select_obj= Select(greek_ele)
    # select_obj.select_by_visible_text("Programming Languages")
    # select_obj.select_by_value("AF")
    # select_obj.select_by_index(3)






#dropdowm_ele()
time.sleep(10)
driver.close()
