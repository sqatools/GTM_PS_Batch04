from selenium.webdriver.common.by import By

###test data
enter_form_city_data = "Trivandrum"
from_city_value = "Thiruvananthapuram, India"
enter_to_city_data = "Bengaluru"
to_city_value = "Bengaluru International Airport"
dep_date_value = "Sep 13"
enter_to_city_data2 = "Delhi"
to_city_value2 = "New Delhi, India"

#locator

close_pop_up_loc = (By.XPATH, "//div[@data-id='auth-flow-section']//child::span//span[@class='logSprite icClose']")
click_multi_city_loc = (By.XPATH, "//p[text()='Multi-city']//preceding-sibling::span")
click_from_trip_loc = (By.XPATH, "//p[text()='Enter city or airport']")
enter_form_city_loc = (By.XPATH, "//span[text()='From']//following-sibling::input")  #click and enter value
select_from_city_loc =(By.XPATH, f"//span[text()='{from_city_value}']")
enter_to_city_loc = (By.XPATH, "//span[text()='To']//following-sibling::input")  #enter value
select_to_city_loc =(By.XPATH, f"//p[text()='{to_city_value}']")
departure_date_click_loc =(By.XPATH, "//span[text()='Departure']//parent::div")
departure_date_select_loc = (By.XPATH, f"//div[contains(@aria-label,'{dep_date_value}')]")
select_adult_loc = (By.XPATH, "//p[text()='Adults']//following::span[3]")
select_child_loc = (By.XPATH,"//p[text()='Children']//following::span[3]")
select_infant_loc =(By.XPATH,"//p[text()='Infants']//following::span[3]")
select_travel_class_loc =(By.XPATH, "//ul//li[text()='business']")
done_loc = (By.XPATH, "//div//a[text()='Done']")
click_enter_to_city_loc = (By.XPATH, "//p[text()='Enter city or airport']")
enter_to_city_loc2 = (By.XPATH, "//p[text()='Enter city or airport']//following::input")
select_to_city_loc2 = (By.XPATH, f"//span[text()='{to_city_value2}']")
search_flight_loc = (By.XPATH, "//span[text()='SEARCH FLIGHTS']")