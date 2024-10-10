
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

time.sleep(10)

driver.find_element(By.XPATH,"(//input[@type='radio'])[4]").click() # How to scroll the page
driver.find_element(By.XPATH,"//input[@name='firstname'][1]").send_keys("Kirti Kaur")
driver.find_element(By.XPATH,"//input[@name='firstname'][2]").send_keys("Labana")
driver.find_element(By.XPATH,"//input[@id='birthday']").send_keys("20/05/1997")
driver.find_element(By.XPATH,"//input[@id='female']").click()
driver.find_element(By.XPATH,"//select/option[@value='2']").click()
driver.find_element(By.XPATH,"//input[@name='fromcity']").send_keys("Mumbai")
driver.find_element(By.XPATH,"//input[@name='destcity']").send_keys("Bangalore")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='departdate']").send_keys("30/07/2024")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='returndate']").send_keys("08/08/2024")
time.sleep(5)
#driver.find_element(By.XPATH,"//input[@id='departdate']").send_keys()# what will happen if input is not in sequance
driver.find_element(By.XPATH,"//input[@id='visadate']").send_keys("25/07/2024")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='eamil']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='billing_name']").send_keys("Kirti")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='billing_phone']").send_keys("9850286266")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='billing_email']").send_keys("Kirti.labana@gmail.com")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='billing_address']").send_keys("ABC")
# time.sleep(5)

# driver.find_element(By.XPATH,"  //select[@id='billing_country']/option[@value='UK']") Not working   //select[@id='billing_country']//option
# driver.find_element(By.XPATH,"//input[@name='postcode']").send_keys("421501")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='Prefecture']").send_keys("456897")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='street_address1']").send_keys("DFDF dfsdfds,dsfsdf dsfs")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='street_address2']").send_keys("sdfdsf, dfdsf,dsfdfsd")
time.sleep(5)



#driver.find_element(By.XPATH,"//select[@id='billing_country']/option[@value='UK']").click() its a dropdow will learn further

# city_list = ["Pune", "Indore", 'Hyderabad']
# for city in city_list:
#     driver.find_element(By.XPATH,f"//td[text()='{city}']//preceding-sibling::td/input").click() # Xpath not working


time.sleep(10)