
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()

def get_wait(locator,waittime=30):
    wait=WebDriverWait(driver,timeout=waittime)
    element=wait.until(ec.presence_of_element_located(locator))
    return element


# Open a web page
driver.get("https://www.worldometers.info/geography/flags-of-the-world/")

# Scroll down by pixel
#driver.execute_script("window.scrollBy(0, 500)","")

#scroll down the page till element found
scroll_loc=(By.XPATH,"//img[@src='/img/flags/small/tn_in-flag.gif']")
element=get_wait(locator=scroll_loc)
driver.execute_script("arguments[0].scrollIntoView()",element)
time.sleep(10)
# Close the browser

#till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

