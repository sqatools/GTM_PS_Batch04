import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()

def get_wait(locator,wait_time=30):
    wait=WebDriverWait(driver,timeout=wait_time)
    element=wait.until(ec.presence_of_element_located(locator))
    return element

def move_element():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

    ebook_loc=(By.XPATH,"//div[@id='menu']//a[text()='Free Ebooks']")
    ebook_ele=get_wait(ebook_loc)
    action=ActionChains(driver)
    action.move_to_element(ebook_ele)
    action.perform()
    time.sleep(5)

    tester_ele=get_wait(locator=(By.XPATH,"//div[@id='menu']//a[text()='Tester’s Hub']"))
    action.move_to_element(tester_ele)
    action.perform()
    time.sleep(5)

    Demo_ele=get_wait(locator=(By.XPATH,"//*[text()='Demo Testing Site']"))
    action.move_to_element(Demo_ele)
    action.perform()
    time.sleep(5)

    Alert_ele=get_wait(locator=(By.XPATH,"//*[text()='AlertBox']"))
    action.move_to_element(Alert_ele)
    action.click()
    action.perform()
    time.sleep(5)
#move_element()

def drap_drop():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    iframe_ele=get_wait(locator=(By.XPATH,"//iframe[@class='demo-frame lazyloaded']"))
    driver.switch_to.frame(iframe_ele)
    action=ActionChains(driver)
    # image_text=get_wait(locator=(By.XPATH,"//h5[text()='High Tatras']//parent::li"))
    # tar_ele=get_wait(locator=(By.ID,"trash"))
    # action.drag_and_drop(image_text,tar_ele)
    # action.perform()
    # time.sleep(10)
#multiple drag _drop
    images_text_names = ["High Tatras", "High Tatras 2", "High Tatras 3", "High Tatras 4"]
    for name in images_text_names:
         image_elm = get_wait(locator=(By.XPATH, f"//h5[text()='{name}']//parent::li"))
         tar_ele=get_wait(locator=(By.ID,"trash"))
         action.drag_and_drop(image_elm,tar_ele)
         action.perform()
         time.sleep(10)
drap_drop()
time.sleep(5)
driver.close()
