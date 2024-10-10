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
    element = wait.until(ec.presence_of_element_located(locator))
    return element

def use_of_clear_method():
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    city_element = get_wait(locator=(By.NAME, "fromcity"))
    city_element.send_keys("Mumbai")
    time.sleep(5)
    city_element.clear()
    time.sleep(5)
    city_element.send_keys("Bangalore")

#use_of_clear_method()

def javascript_executor():
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    element = get_wait(locator=(By.ID, "street_address2"))
    action = ActionChains(driver)
    action.scroll_to_element(element)
    action.perform()

    from_city_ele=driver.execute_script("return document.getElementById('fromcity');")
    from_city_ele.send_keys('Bangalore')
    time.sleep(10)

    URL = driver.execute_script("return document.URL")
    print("Browser URL :", URL)

    title = driver.execute_script("return document.title")
    print("Title :", title)

    driver.execute_script("document.getElementById('oneway').click()")
    header_element = driver.execute_script("return document.getElementsByTagName('h1');")
    print("header element :", header_element[0].text)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
 # https://www.w3schools.com/jsref/prop_element_scrolltop.asp
#javascript_executor()

def upload_file():
    driver.get("https://automationbysqatools.blogspot.com/2020/08/login.html")
    file=get_wait(locator=(By.ID,"myFile"))
    file.send_keys('C:\\Sushmita\\upload file\data.txt')
    time.sleep(10)
    print(file.text)
    submit_but=get_wait(locator=(By.XPATH,"//input[@id='myFile']//following-sibling::input[@type='submit']"))
    submit_but.click()


upload_file()
time.sleep(5)
driver.close()
