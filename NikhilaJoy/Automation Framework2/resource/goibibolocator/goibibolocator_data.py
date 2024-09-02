from selenium.webdriver.common.by import By


fcity="PVRD"
from_station_name = "Piravom Road Railway Station"

dcity="KRIS"
dest_station_name = "Krishnarajapuram Railway Station"



train=(By.XPATH,"(//li[@class='sc-1f95z5i-1 hiUlsg']//child::a[@class='sc-1f95z5i-2 hXZcJL'])[2]")

close=(By.XPATH,"//span[@class='logSprite icClose']")
f_city=(By.XPATH,"//p[text()='From']//following-sibling::p[1]")
f_city_input_field = (By.XPATH, "//span[text()='From']//following-sibling::input")

d_city=(By.XPATH,"//p[text()='To']//following-sibling::p[1]")
d_city_input_field=(By.XPATH,"//span[text()='To']//following-sibling::input")

f_suggestion=(By.XPATH,"//span[text()='Piravom Road Railway Station']")
d_suggestion=(By.XPATH,"//span[text()='Krishnarajapuram Railway Station']")