from selenium.webdriver.common.by import By

####### test data ############
goibibo_url = "https://www.goibibo.com/"
from_city_name = "Chennai (MAA)"
to_city_name = "Mumbai (BOM)"
departure_date = "Aug 30 2024"
travel_class_type = "business"
flight_name="IndiGo"


######### Locators #########
close_pop_button = (By.XPATH, "//span[@class='logSprite icClose']")
flight_booking_page_link = (By.XPATH, "//span[@class='Flights']//parent::a")
flight_booking_header=(By.XPATH,"//h2[@class='Domestic and international Flights']")
flight_oneway_button= (By.XPATH,"//button[class()='oneway']")
from_enter_city_loc = (By.XPATH, "//span[text()='From']//following-sibling::p[text()='Enter city or airport']")
from_city_input_field = (By.XPATH, "//span[text()='From']//following-sibling::input")
To_city_input_field = (By.XPATH, "//span[text()='To']//following-sibling::input")
cal_locator = (By.XPATH, "//span[text()='Departure']//parent::div")
travellers_class_loc = (By.XPATH, "//span[text()='Travellers & Class']//parent::div")
add_adults_icon = (By.XPATH, "//p[text()='Adults']//following-sibling::div/span[3]")
add_children_icon = (By.XPATH, "//p[text()='Children']//following-sibling::div/span[3]")
add_infants_icon = (By.XPATH, "//p[text()='Infants']//following-sibling::div/span[3]")
travel_class_done_button = (By.XPATH, "//a[text()='Done']")
search_button = (By.XPATH, "//span[text()='SEARCH FLIGHTS']")


