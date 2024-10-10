from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome()
driver.maximize_window()
#def get_element(locator,timeout=15):
#    wait=WebDriverWait(driver,timeout)
# element=wait.until(ec.presence_of_element_located(locator))
#   return element

def get_resturant_link():
    driver.get("https://www.getbento.com/blog/best-restaurant-websites-design/")
    ele_ment=driver.find_elements(By.XPATH,"//div[@class='my-8 md:my-16']//div[@class='prose md:prose-lg']//h2//a")
    #resto_locator=(By.XPATH,"//div[@class='my-8 md:my-16']//div[@class='prose md:prose-lg']//h2")
    #ele_ment=get_element(locator=resto_locator)
    #for i in ele_ment:
    #     print(i.text)
    #    print(i.get_attribute("href"))

    for i in range(len(ele_ment)):
        ele_text=driver.find_elements(By.XPATH,f"//div[@class='my-8 md:my-16']//div[@class='prose md:prose-lg']//h2{i}//a")
        print(ele_text.text)
        ele_link=driver.find_elements(By.XPATH,f"//div[@class='my-8 md:my-16']//div[@class='prose md:prose-lg']//h2//a{i}")
        print(ele_link.get_attribute("href"))
get_resturant_link()