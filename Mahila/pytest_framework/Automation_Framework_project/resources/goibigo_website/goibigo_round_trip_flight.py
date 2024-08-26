from selenium.webdriver.common.by import By

###test data
enter_form_city_data = "Trivandrum"
from_city_value = "Thiruvananthapuram, India"
enter_to_city_data = "Bengaluru"
to_city_value = "Bengaluru International Airport"
dep_date_value = "Sep 13"
#locator

close_pop_up_loc = (By.XPATH, "//div[@data-id='auth-flow-section']//child::span//span[@class='logSprite icClose']")
click_round_trip_loc = (By.XPATH, "//p[text()='Round-trip']//preceding-sibling::span")
click_from_trip_loc = (By.XPATH, "//p[text()='Enter city or airport']")
enter_form_city_loc = (By.XPATH, "//span[text()='From']//following-sibling::input")  #click and enter value
select_from_city_loc =(By.XPATH, f"//span[text()='{from_city_value}']")
enter_to_city_loc = (By.XPATH, "//span[text()='To']//following-sibling::input")  #enter value
select_to_city_loc =(By.XPATH, f"//p[text()='{to_city_value}']")
departure_date_click_loc =(By.XPATH, "//span[text()='Departure']//parent::div")
departure_date_select_loc = (By.XPATH, f"//div[contains(@aria-label,'{dep_date_value}')]")
travel_and_class_loc = (By.XPATH, "//span[text()='Travellers & Class']//parent::div")
adult_button_loc = (By.XPATH, "//p[text()='Adults']//following::span[3]")
child_button_loc = (By.XPATH, "//p[text()='Children']//following::span[3]")
premium_economy_loc = (By.XPATH, "//ul//li[text()='premium economy']")
done_loc = (By.XPATH, "//a[text()='Done']")
search_flight_loc = (By.XPATH ,"//span[text()='SEARCH FLIGHTS']")