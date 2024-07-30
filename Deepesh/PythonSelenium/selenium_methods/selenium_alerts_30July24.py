import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options


option = Options()
option.add_argument("--disable-notifications")
option.add_argument("--headless")
driver = webdriver.Chrome(options=option)
driver.maximize_window()

def get_element(locator, wait_time=30):
    wait = WebDriverWait(driver, timeout=wait_time)
    element = wait.until(ec.presence_of_element_located(locator))
    return element

def handle_alert_box():
    driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
    alert = Alert(driver)
    get_element(locator=(By.ID, "btnShowMsg")).click()
    print(alert.text)
    time.sleep(5)
    alert.accept()

#handle_alert_box()

def handle_confirm_box():
    driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
    alert = Alert(driver)
    get_element(locator=(By.ID, "button")).click()
    print(alert.text)
    time.sleep(5)
    #alert.accept()
    alert.dismiss()  # You pressed Cancel!
    print(get_element(locator=(By.ID, "demo")).text)
    time.sleep(5)


#handle_confirm_box()

def handle_prompt_box():
    driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
    alert = Alert(driver)
    get_element(locator=(By.ID, "promptbtn")).click()
    print(alert.text)
    time.sleep(5)
    alert.send_keys("GrowTechMind")
    # alert.accept() # Hello GrowTechMind! How are you today?
    alert.dismiss()  # You pressed Cancel!
    print(get_element(locator=(By.ID, "prompt")).text)
    time.sleep(5)

#handle_prompt_box()

def handle_alert_on_facebook():
    driver.get("https://www.facebook.com/login.php")
    username=get_element(locator=(By.NAME,"email"))
    username.send_keys("Testing01@gmail.com")

    print("username is enable",username.is_enabled())

    password=get_element(locator=(By.NAME,"pass"))
    password.send_keys("Test@1234")
    print('password is displayed',password.is_displayed())

    #alert=Alert(driver)
    driver.find_element(By.XPATH,"//button[@value='1']").click()
    # time.sleep(10)
    # alert.accept()
    # print(alert.text)
    #
    # print(driver.title)
    #driver.close()

handle_alert_on_facebook()

time.sleep(10)
driver.close()
