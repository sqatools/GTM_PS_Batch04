from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
import time
import os #curent directory
from datetime import datetime

headless_execution =False
option=Options()
option.add_argument("--disable-notification")
if headless_execution:
    option.add_argument("--headless")
driver = webdriver.Chrome(options=option)
driver.maximize_window()

cur_dire = os.getcwd()   #cureent directory
images_folder_path = os.path.join(cur_dire, "images")
print(images_folder_path)


def get_element(locator, wait_time=30):
    wait = WebDriverWait(driver, timeout=wait_time)
    element = wait.until(ec.presence_of_element_located(locator))
    return element

def get_latest_date_val():
   return datetime.now().strftime("%d_%m_%Y_%H_%M_%S")


def handle_alert_on_facebook():
    driver.get("https://www.facebook.com/login.php")
    latest_var = get_latest_date_val()
    driver.save_screenshot(f"E://{latest_var}_login_page.png")
    username=get_element(locator=(By.NAME,"email"))
    username.send_keys("Testing01@gmail.com")

    print("username is enable",username.is_enabled())

    password=get_element(locator=(By.NAME,"pass"))
    password.send_keys("Test@1234")
    print('password is displayed',password.is_displayed())

    driver.find_element(By.XPATH,"//button[@value='1']").click()
    time.sleep(5)

    driver.save_screenshot(f"{images_folder_path}//{latest_var}_facebook_page.png")

handle_alert_on_facebook()

time.sleep(10)
driver.close()
