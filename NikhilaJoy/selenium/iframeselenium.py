import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as ec
#from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()

def get_element(locator):
    element = driver.find_element(*locator)
    return element
def ifram_practice():
    driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
    ifram_locator = By.XPATH,"//iframe[@name='globalSqa']"
    ele_ment = get_element(ifram_locator)
    driver.switch_to.frame(ele_ment)

    mob_togler=(By.XPATH,"//div[@id='mobile_menu_toggler']")
    mob_locator=get_element(mob_togler)
    mob_locator.click()

    cheetsheet_togler = (By.XPATH, "//div[@id='mobile_menu']//a[text()='CheatSheets']")
    cheet_locator = get_element(cheetsheet_togler)
    cheet_locator.click()

ifram_practice()



