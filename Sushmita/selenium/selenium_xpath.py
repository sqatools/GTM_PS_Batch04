import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
#driver.get("https://www.google.co.in/")

#Absolute Xpath
# driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea").send_keys("python")
# #driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()
# driver.find_element(By.NAME,"btnK")

#Relative Xpath

#driver.find_element(By.XPATH,"//textarea[@name='q']").send_keys("python selenium")
#driver.find_element(By.XPATH,"//*[@name='q'']")
#driver.find_element(By.XPATH,"//*[@class='gLFyf']").send_keys("python selenium")


driver.get("https://automationbysqatools.blogspot.com/p/home.html")
driver.find_element(By.XPATH,"//div[text()=' Dummy Website ']").click()
driver.find_element(By.XPATH,"//input[@value='radio_558']").click()
driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Rahul")
driver.find_element(By.XPATH,"//input[@name='firstname'][2]").send_keys("gupta")
driver.find_element(By.XPATH,"//*[@id='birthday']").send_keys("22-07-2024")
driver.find_element(By.XPATH,"//*[@id='female']").click()
driver.find_element(By.XPATH,"//*[@id='roundtrip']").click()
driver.find_element(By.XPATH,"//*[@name='fromcity']").send_keys("Lingasugur")
driver.find_element(By.XPATH,"//*[@name='destcity']").send_keys("Raichur")
driver.find_element(By.XPATH,"//*[@name='departdate']").send_keys("22-07-2024")
driver.find_element(By.XPATH,"//*[@name='returndate']").send_keys("22-07-2024")
driver.find_element(By.XPATH,"//*[@name='visadate']").send_keys("22-07-2024")
driver.find_element(By.XPATH,"//span[text()='Both']").click()
driver.find_element(By.XPATH,"//*[@id='billing_name']").send_keys("Rahul")
driver.find_element(By.XPATH,"//*[@id='billing_phone']").send_keys("23456")

driver.find_element(By.XPATH,"//*[@id='billing_email']").send_keys("23456@gmail.com")
driver.find_element(By.XPATH,"//*[@id='billing_address']").send_keys("shivanagar")
driver.find_element(By.XPATH,"//*[@id='postcode']").send_keys("560010")
driver.find_element(By.XPATH,"//*[@id='Prefecture']").send_keys("560010")
driver.find_element(By.XPATH,"//*[@id='street_address1']").send_keys("560010")
driver.find_element(By.XPATH,"(//input[@type='checkbox'])[5]").click()
driver.find_element(By.XPATH,"//a[@class='home-link']").click()

time.sleep(10)
driver.close()
