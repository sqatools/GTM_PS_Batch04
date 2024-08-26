
from  selenium.webdriver.common.by import By


#testdata



#locator

one_way_check_loc = (By.XPATH,"//p[text()='One-way']//preceding-sibling::span")
from_city_loc = (By.XPATH, "//span[text()='From']//following-sibling::p")
from_city_sel_loc = (By.XPATH, "//p[text()='Trivandrum International Airport']//parent::div")
To_city_loc = (By.XPATH, "//span[text()='To']//following-sibling::input")
to_city_sel_loc = (By.XPATH, "//p[text()='Bengaluru International Airport']//parent::div")
dep_data_loc = (By.XPATH, "//p[contains(text(),'25 Aug')]")
dep_date_sel_loc = (By.XPATH, "//p[text()='29']//parent::div")
travel_class_loc = (By.XPATH, "//p[text()='1 Adult']")
