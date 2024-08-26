from selenium.webdriver.common.by import By


#test_data




#test_locators

cancel_popup_loc = (By.XPATH, "span[@class='logSprite icClose']")
bus_link_loc = (By.XPATH, "//span[text()='Bus']//parent::a")
from_city_loc = (By.XPATH, "//input[@placeholder='Enter Source']")
#from_city_select_loc = (By.XPATH, "//span[text()='Vyttila, Ernakulam']")
dest_city_loc = (By.XPATH, "//input[@placeholder='Enter Destination']")
pic_a_date_loc = (By.XPATH, "//input[@placeholder='Pick a date']")
data_loc = (By.XPATH, "//span[text()='26']//parent::li")
search_butt_loc = (By.XPATH, "//button[text()='Search Bus']")

