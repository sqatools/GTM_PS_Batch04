import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
header_element = driver.find_element(By.TAG_NAME,"h1")  # TAG NAME LOCATOR
print(header_element.text)                                    #.text - will print the text corresponding to the tag

driver.find_element(By.XPATH,"//input[@value='radio_123']").click()
driver.find_element(By.XPATH,"//input[@name='firstname'][1]").send_keys("Mahila")
driver.find_element(By.XPATH,"//input[@name='firstname'][2]").send_keys("Mahila")
driver.find_element(By.XPATH,"(//input[@type='date'])[1]").send_keys("21-05-1999")
driver.find_element(By.XPATH,"//input[@id='female'][1]").click()
driver.find_element(By.XPATH,"//select[@id='admorepass']").send_keys("add one more passenger -100%")
element = driver.find_element(By.NAME,"fromcity").send_keys("Banglore")    #Name locator
element = driver.find_element(By.NAME,"destcity").send_keys("Trivandrum")   #Name Locator
driver.find_element(By.XPATH,"//input[@id='departdate']").send_keys("24-08-2024")
driver.find_element(By.XPATH,"//input[@id='returndate']").send_keys("23-09-2024")
driver.find_element(By.XPATH,"//input[@id='visadate']").send_keys("25-07-2024")
driver.find_element(By.XPATH,"//input[@id='eamil']").click()
element = driver.find_element(By.ID,"billing_name").send_keys("A-128 Souparnika Feminco Old fort Road Banglore")   #ID LOCATOR
driver.find_element(By.XPATH,"//input[@id='billing_phone']").send_keys("7909175279")
driver.find_element(By.XPATH,"//input[@id='billing_email']").send_keys("mahila618mahesh@gmail.com")
driver.find_element(By.XPATH,"//input[@id='billing_address']").send_keys("A-128 Banglore")
driver.find_element(By.XPATH,"//select[@id='billing_country']").send_keys("INDIA")
driver.find_element(By.XPATH,"//input[@name='postcode']").send_keys("695615")
driver.find_element(By.XPATH,"//input[@name='prefecture']").send_keys("123456")
driver.find_element(By.XPATH,"//input[@id='street_address1']").send_keys("A-128 Sowparnika Fleminco")
driver.find_element(By.XPATH,"//input[@id='street_address2']").send_keys("Old fort road Banglore")
driver.find_element(By.XPATH,"//tr/td/input[@type='checkbox'][2]").click()


# driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")        #LINK_TEXT
# element_link_text = driver.find_element(By.LINK_TEXT,"Software Testing Methods").click()
#
# driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")        #PARTIAL_ LINK_TEXT
# element_link_text = driver.find_element(By.PARTIAL_LINK_TEXT,"Testing Methods").click()

time.sleep(10)
driver.close()



