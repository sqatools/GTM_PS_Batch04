from selenium.webdriver.common.by import By

##### Test data ######
goibibo_url = "https://www.goibibo.com/"
enter_city_name = "Mumbai, India"
To_city_name = "Bengaluru, India"
Departure_Date = "26"
Adult="1"



###### Locators ######
login_popup_close = (By.XPATH, "//span[@class='logSprite icClose']")
flight_booking_page_link = (By.XPATH, "//span[@class='Flights']//parent::a")
flight_booking_header=(By.XPATH,"//h2[@class='Domestic and international Flights']")
flight_oneway_button= (By.XPATH,"//button[class()='oneway']")
from_enter_city_name = (By.XPATH,"//span[text='from']//following-sibling::p[text()='Enter city or airport']")
from_city_input_field = (By.XPATH, "//span[text()='From']//following-sibling::input")
To_city_input_field = (By.XPATH, "//span[text()='To']//following-sibling::input")

calender_locator=(By.XPATH, "//span[text()='Departure']//parent::div}")

travellers_class_loc = (By.XPATH, "//span[text()='Travellers & Class']//parent::div")

add_adults_icon = (By.XPATH, "//p[text()='Adults']//parent::div")