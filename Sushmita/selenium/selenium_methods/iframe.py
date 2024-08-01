from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver=webdriver.Chrome()
driver.maximize_window()

def get_wait(locator,wait_time=30):
    wait=WebDriverWait(driver,timeout=wait_time)
    element=wait.until(ec.visibility_of_element_located(locator))
    return element

def handle_iframe():
    driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
    ifrmae_loca=(By.NAME,"globalSqa")
    iframe_ele=get_wait(locator=ifrmae_loca)
    driver.switch_to.frame(iframe_ele)

    email_loc=(By.XPATH,"//div[@class='header_mail']")
    email_ele=get_wait(email_loc)
    print('contact email:',email_ele.text)
    time.sleep(10)

    mobile_menu_loc=(By.ID,"mobile_menu_toggler")
    mobile_menu_ele=get_wait(locator=mobile_menu_loc)
    mobile_menu_ele.click()
    time.sleep(10)

    cheatshet_loca=(By.XPATH,"//div[@id='mobile_menu']//a[text()='CheatSheets']")
    cheat_ele=get_wait(cheatshet_loca)
    cheat_ele.click()
    time.sleep(5)

    driver.switch_to.default_content()
    cheat_top=(By.XPATH,"//div[@id='menu']//a[text()='CheatSheets']")
    cheat_top_ele=get_wait(cheat_top)
    cheat_top_ele.click()


handle_iframe()
time.sleep(10)
driver.close()


handle_iframe()
driver.close()
