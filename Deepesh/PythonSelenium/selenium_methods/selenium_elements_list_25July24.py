import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

def click_checkboxes():
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

    print("Current URL :", driver.current_url)
    print("Title of the website :", driver.title)

    element_list = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

    for element in element_list:
        element.click()
        time.sleep(3)

def college_names():
    driver.get("https://collegedunia.com/india-colleges")
    element_list = driver.find_elements(By.XPATH, "//div[contains(@class, 'clg-column')]/a")
    for element in element_list:
        print(element.get_attribute("title"))
        print(element.get_attribute("href"))

#college_names()

def check_element_status():
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

    fromcity_element = driver.find_element(By.ID, "fromcity")
    print("check element is enabled :", fromcity_element.is_enabled())
    print("check element is displayed :", fromcity_element.is_displayed())
    fromcity_element.send_keys("Chennai")

    pune_checkbox = driver.find_element(By.XPATH, "//td[text()='Pune']//preceding-sibling::td/input")
    print("checkbox is selected :", pune_checkbox.is_selected()) # False
    pune_checkbox.click()
    print("checkbox is selected :", pune_checkbox.is_selected()) # True

check_element_status()

time.sleep(5)
driver.close()
