from selenium.webdriver.common.by import By

close_pop_button = (By.XPATH, "//span[@class='logSprite icClose']")
from_enter_city_loc = (By.XPATH, "//span[text()='From']//following-sibling::p[text()='Enter city or airport']")
from_city_input_field = (By.XPATH, "//span[text()='From']//following-sibling::input")
source_city_name = "Mumbai, India"
to_city_input_field = (By.XPATH, "//span[text()='To']//following-sibling::input")
target_city_name = "Bengaluru, India"

cal_locator = (By.XPATH, "//span[text()='Departure']//parent::div")
depart_date = "Aug 04 2024"

travellers_class_loc = (By.XPATH, "//span[text()='Travellers & Class']//parent::div")

add_adults_icon = (By.XPATH, "//p[text()='Adults']//following-sibling::div/span[3]")
add_children_icon = (By.XPATH, "//p[text()='Children']//following-sibling::div/span[3]")
add_infants_icon = (By.XPATH, "//p[text()='Infants']//following-sibling::div/span[3]")

travel_class_type = "business"
travel_class_done_button = (By.XPATH, "//a[text()='Done']")
search_button = (By.XPATH, "//span[text()='SEARCH FLIGHTS']")

