import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

def get_element(locator, wait_time=30):
    wait = WebDriverWait(driver, timeout=wait_time)
    element = wait.until(ec.presence_of_element_located(locator))
    return element

def select_dropdown_value(locator, value):
    element = get_element(locator)
    select = Select(element)
    select.select_by_visible_text(value)

def use_of_clear_method():
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    city_element = get_element(locator=(By.NAME, "fromcity"))
    city_element.send_keys("Mumbai")
    time.sleep(5)
    city_element.clear()
    time.sleep(5)
    city_element.send_keys("Bangalore")

#use_of_clear_method()

def java_script_executor():
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    element = get_element(locator=(By.ID, "street_address2"))
    action = ActionChains(driver)
    action.scroll_to_element(element)
    action.perform()

    time.sleep(10)

    from_city_elem = driver.execute_script("return document.getElementById('fromcity');")
    from_city_elem.send_keys("Chennai")

    URL = driver.execute_script("return document.URL")
    print("Browser URL :", URL)

    title = driver.execute_script("return document.title")
    print("Title :", title)

    driver.execute_script("document.getElementById('oneway').click()")
    header_element = driver.execute_script("return document.getElementsByTagName('h1');")
    print("header element :", header_element[0].text)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # https://www.w3schools.com/jsref/prop_element_scrolltop.asp




java_script_executor()

def upload_file_via_selenium():
    driver.get("https://automationbysqatools.blogspot.com/2020/08/login.html")

    upload_file = get_element(locator=(By.ID, 'myFile'))
    upload_file.send_keys("E:\\Filesdata\\count_name.txt")

    time.sleep(10)
    submit_button = get_element(locator=(By.XPATH, "//input[@id='myFile']//following-sibling::input[@type='submit']"))
    submit_button.click()



#upload_file_via_selenium()

time.sleep(5)
driver.close()

