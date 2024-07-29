import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()
#driver.implicitly_wait(5)
def get_wait(timeout=10):
    wait=WebDriverWait(driver,timeout,poll_frequency=2)
    return wait
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.XPATH,"//input[@value='radio_678']").click()
t1=time.time()
try:
    element=get_wait().until(ec.element_to_be_clickable((By.XPATH,"//input[@value='radio_124']")))
    element.click()
except Exception as e:
    print(e)
t2=time.time()
fromcit=get_wait(timeout=5).until(ec.presence_of_element_located((By.ID,"male"))).click()
print(t2-t1)

time.sleep(10)
driver.close()