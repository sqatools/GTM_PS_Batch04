from selenium.webdriver.common.by import By

city_name = "Bangalore"

close_popup_link=(By.XPATH,"//span[@class='sc-jlZhew inxprl']")

navigate_bus_link=(By.XPATH,"//span[text()='Bus']//parent::a")
source_link=(By.XPATH,"//input[@placeholder='Enter Source']")
