import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

#open website URL

driver.get("https://www.google.co.in")
driver.find_element(By.XPATH,"//*[@title='Search']").send_keys("Python Selenium")

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.find_element(By.XPATH,"(//input[@name='firstname'])[1]").send_keys("Sunita")
driver.find_element(By.XPATH,"(//input[@name='firstname'])[2]").send_keys("Chauhan")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@name='birthday']").send_keys("07-08-1993")
time.sleep(2)

driver.find_element(By.XPATH,"(//input[@id='female'])[1]").click()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='oneway']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@name='fromcity']").send_keys("Pune")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@name='destcity']").send_keys("Mumbai")
time.sleep(2)


driver.find_element(By.XPATH,"//input[@id='departdate']").send_keys("20-07-2024")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='returndate']").send_keys("28-07-2024")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='whatsapp']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='billing_name']").send_keys("Sunita")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='billing_phone']").send_keys("8902345670")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='billing_email']").send_keys("Sunita@gmail.com")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='billing_address']").send_keys("Pimpri,Pune")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@name='postcode']").send_keys("411018")
time.sleep(2)


driver.find_element(By.XPATH,"//input[@id='street_address1']").send_keys("Pimpri")
time.sleep(2)

def click_checkboxes():
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

    print("Current URL :", driver.current_url)
    print("Title of the website :", driver.title)

    element_list=driver.find_elements(By.XPATH,"//input[@type='checkbox']")

    for element in element_list:
        element.click()
        time.sleep(3)

