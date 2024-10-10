import time

from selenium import webdriver # from selelium package importing the webdriver class ?
from selenium.webdriver.common.by import By

browser = "Chrome" # Provide value in which browser you need to execute

if browser == "Chrome":
    driver = webdriver.Chrome()
elif browser ==  "Firefox":
    driver = webdriver.Firefox()
elif browser == "Edge":
    driver = webdriver.Edge()


#driver = webdriver.Chrome() # driver is a variable which has assigned value of ?
#driver = webdriver.Firefox()
#driver = webdriver.Edge()

driver.maximize_window() # variable. Method (Maximize_window()) of webdriver class
driver.implicitly_wait=(10)  # implicitly_wait is a method of webdriver class
#driver.get("https://www.amazon.in/s?k=one+plus+11R&crid=14FQSBEQ3U3E6&sprefix=one+plus+11%2Caps%2C247&ref=nb_sb_noss") #vairable. get() is a parameterized method/function
# driver.get("https://www.google.co.in")
# driver.find_element(By.NAME,"q").send_keys("Python")
# time.sleep(10)
# driver.find_element(By.NAME,"btnK").click()
# time.sleep(10)

driver.get("https://www.google.co.in")
driver.find_element(By.NAME,"q").send_keys("amazon registration")
time.sleep(10)
driver.find_element(By.NAME,"btnK").click()
time.sleep(10)
#driver.find_element(By.XPATH,"//a[@aria-label='Amazon Registration']").click()
driver.find_element(By.XPATH,"//a[@href='https://www.amazon.com/newuser']").click()
#driver.find_element(By.XPATH, "(//h3[@class='LC20lb MBeuO DKV0Md' and text()='Amazon Registration'])[1]").click()
time.sleep(10)
#driver.find_element(By.NAME,"email").send_keys("Kirtilabanax@gmail.com")
driver.find_element(By.NAME, "customerName").send_keys("Kirti Labana")
time.sleep(10)
#driver.find_element(By.XPATH,"//input[@type='email']").send_keys("987654312")
driver.find_element(By.ID,"ap_email").send_keys("9850191877")
time.sleep(10)
driver.find_element(By.XPATH,"//input[@id='ap_password']").send_keys("XYZ@123")
time.sleep(10)
driver.find_element(By.XPATH,"//input[@id='ap_password_check']").send_keys("XYZ@123")
time.sleep(10)
driver.find_element(By.XPATH,"//input[@id='continue']").click()
time.sleep(10)

driver.close()
