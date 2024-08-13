from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=12375659314113963398&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9149419&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1")
driver.find_element(By.XPATH,"//div[@aria-label='navigation']//following::input[@id='twotabsearchtextbox']").send_keys("womens outfit")
time.sleep(5)
driver.find_element(By.XPATH,"//span[@aria-label='Go']//child::input").click()
time.sleep(5)

t1 = time.time()
try:
    wait=WebDriverWait(driver,15 , poll_frequency=1)
    element=wait.until(ec.presence_of_element_located((By.XPATH,"//a[text()='Amazon miniTV']//following-sibling::a[text()='Sell']")))
except Exception as e:
    print(e)
t2 = time.time()
print("total time taken :", t2-t1)

def get_wait(timeout=15):
    wait =WebDriverWait(driver, timeout, poll_frequency=1)
    return wait
def get_element(locator,timeout=15,wait_cond=ec.presence_of_element_located):
    return get_wait(timeout).until(wait_cond(locator))

ham_element=get_element((By.XPATH,"//a[@id='nav-hamburger-menu']//child::i"), wait_cond=ec.element_to_be_clickable).click()
time.sleep(2)
close_element=get_element((By.XPATH,"//div[@class='nav-sprite hmenu-close-icon']"), wait_cond=ec.element_to_be_clickable).click()
time.sleep(2)
head_element=get_element((By.XPATH,"//div[@class='a-cardui-header']//child::h2[text()='Starting ₹149 | Headphones']"),wait_cond=ec.element_to_be_clickable)
assert head_element
