import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.goibibo.com/?utm_source=google&utm_medium=cpc&utm_campaign=DF-Brand-EM&utm_adgroup=Goibibo-Flight&utm_term=!SEM!DF!G!Brand!RSA!108599293!12768765973!654874673033!e!goibibo%20login!c!&gad_source=1&gclid=CjwKCAjwzIK1BhAuEiwAHQmU3nqgvTQxLJUbSaIi5gecutbcl6kSC5E68g5mE0ZQ33Z3zSGCpyXCjRoC4bEQAvD_BwE")
driver.find_element(By.XPATH,"//span[@class='logSprite icClose']").click()
driver.find_element(By.XPATH,"//span[@class='sc-12foipm-70 fPPRk']").click()
#driver.find_element(By.XPATH,"//p[text()='One-way']//preceding-sibling::span[@class='sc-12foipm-70 bWWMhV']").click()
#driver.find_element(By.XPATH,"//span[text()='From']//following-sibling::p[text()='Enter city or airport']").send_keys("Bengaluru")
#driver.find_element(By.XPATH,"//span[text()='To']//following-sibling::p[text()='Enter city or airport']").send_keys("Hyderbad")
driver.find_element(By.XPATH,"//div[text()='Student']//ancestor::label/div[1]").click()
driver.find_element(By.XPATH,"//div[@class='sc-12foipm-91 biWUTl']//parent::label[@for='SC']").click()




time.sleep(10)
driver.close()
