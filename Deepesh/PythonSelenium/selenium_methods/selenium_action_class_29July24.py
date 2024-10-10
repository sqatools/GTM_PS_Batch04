import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

def get_element(locator, wait_time=30):
    wait = WebDriverWait(driver, timeout=wait_time)
    element = wait.until(ec.presence_of_element_located(locator))
    return element

def move_to_element():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    free_ebook_element = get_element(locator=(By.XPATH, "//div[@id='menu']//a[text()='Free Ebooks']"))
    action = ActionChains(driver)
    action.move_to_element(free_ebook_element)
    action.perform()

    tests_hub_elem = get_element(locator=(By.XPATH, "//div[@id='menu']//a[text()='Tester’s Hub']"))
    action.move_to_element(tests_hub_elem)
    action.perform()

    time.sleep(5)
    demo_testing_site_elem = get_element(locator=(By.XPATH, "//*[text()='Demo Testing Site']"))
    action.move_to_element(demo_testing_site_elem)
    action.perform()

    time.sleep(5)
    alert_box = get_element(locator=(By.XPATH, "//*[text()='AlertBox']"))
    action.move_to_element(alert_box)
    action.click()
    action.perform()

    time.sleep(5)


#move_to_element()

def handle_drag_drop():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    iframe_elem = get_element(locator=(By.XPATH, "//iframe[@class='demo-frame lazyloaded']"))
    driver.switch_to.frame(iframe_elem)
    action = ActionChains(driver)
    images_text_names = ["High Tatras", "High Tatras 2", "High Tatras 3", "High Tatras 4"]
    for name in images_text_names:
        image_elm = get_element(locator=(By.XPATH, f"//h5[text()='{name}']//parent::li"))
        target_trash_elm = get_element(locator=(By.ID, "trash"))
        action.drag_and_drop(image_elm, target_trash_elm)
        action.perform()
        time.sleep(5)


handle_drag_drop()

time.sleep(10)
driver.close()
