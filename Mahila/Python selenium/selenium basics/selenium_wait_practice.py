"""
2 type of waits:
1)implicit wait
2)explicit wait + fluent wait
3)static wait
4)
"""

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait  #webdriverwait is a class through which we can initiate the explicit wait.
from selenium.webdriver.support import expected_conditions as ec  #excepted condition renamed as ec so when ever needed we can easily use ec.
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
#implicit wait applies on all the elements of the web page by default
#driver.implicitly_wait(10)

#explicit wait -  we need to create an object for explicit wait as we have initialized the class above webdriverwait
#explicit wait applies on specific element of the webpage with conditon. tp use condition we need to import - from selenium.webdriver.support import expected_conditions as ec

#create the object(wait)
wait = WebDriverWait(driver,15)   # 2 parameters - manager driver and timeout

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
#any variable that want to get it we can do with condition

#to get particular element

#element= wait.until(ec.condition)

t1 = time.time()    #to understand how much time taken before

try:  #exception handling, so in case of error it should not fail our pgm
   element = wait.until(ec.presence_of_element_located((By.ID, 'billing_name')))  #provide the combinations, entire locator combination in form of tuple. locator and value
   element.send_keys("MahilaMahesh")
except Exception as e:
    print(e)
#presence of the element - element should be present
#visibility_of_the _element
#text_to_be_present_in_element
#lot many conditions

t2= time.time()           #to understand how much time taken after
print("total time taken1:" , t2-t1)           #to understand how much time taken difference


a1 = time.time()
try:
    phone = driver.find_element(By.ID,"billing_phone")
    phone.send_keys("7909175279")
except Exception as e:


    print(e)

a2 = time.time()
print("total time taken2:" ,a2-a1)
driver.close()

#together with implicit and explicit wait it took araound 21 sec = that is the sum of implicit wait and some time of explicit wait. if there is invalid locator value mentioned
#if valid value mentioned it will take less time only
#now we can exeute with explicit wait alone.  #total time taken: 15.18576979637146
#as it is taking sum use any one of the waits, either implicit/explicit waits
#most of times we use explicit waits in project

#syntax - wait.until(expected_condition.presence_of_element_located((By.ID,"Bbilling_name")))

#flent wait == assume the total time 15 sec driver actually do there is period specific time, in between specific time it will check again and again and again for the element is there or not
#if the element is find in 5th sec it will only confuse 5 sec only, time interval between each check is the fluent wait.
#default value is 0.5 that means in 15 sec it will check for 30 times for the element.

