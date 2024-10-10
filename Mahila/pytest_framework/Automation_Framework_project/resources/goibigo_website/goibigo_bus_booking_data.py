from selenium.webdriver.common.by import By

###test data

from_city_data = "Trivandrum"
select_from_city_data ="Thiruvananthapuram (Trivandrum), Kerala"
to_city_data = "Bengaluru"
travel_date = "19"
dep_time_data = "12 noon - 6 PM"
boarding_point_data = "Alamcode Bus Stop"

#locator

close_pop_up_loc = (By.XPATH, "//div[@data-id='auth-flow-section']//child::span//span[@class='logSprite icClose']")
select_bus_loc = (By.XPATH,"//span[text()='Bus']//parent::a")
From_city_loc = (By.XPATH,"//input[@name='autosuggestBusSRPSrcHomeName']")
select_from_city_loc = (By.XPATH, f"//div[@id='downshift-1-item-0']//span[text()='{select_from_city_data}']")
To_city_loc = (By.XPATH, "//input[@placeholder='Enter Destination']")
select_to_city_loc = (By.XPATH,"//div[@id='downshift-2-item-0']//span[text()='Bangalore (Bengaluru), Karnataka']")
click_travel_date_loc =(By.XPATH,"//input[@placeholder='Pick a date']")
select_travel_date_loc = (By.XPATH ,f"//label[text()='Travel Date']//following::span[text()='{travel_date}']")
search_bus_loc = (By.XPATH,"//button[text()='Search Bus']")
bus_type_selection_loc = (By.XPATH,"//span[text()='Bus Type']//following::div[text()='Sleeper']")
dep_time_selection_loc = (By.XPATH,"//span[text()='Arrival Time']//preceding::div[text()='12 noon - 6 PM']")
boarding_point_loc = (By.XPATH,"//span[@title='Alamcode Bus Stop']//preceding-sibling::span")
operator_sele_loc = (By.XPATH,"//span[@title='A1 Travels']//preceding-sibling::span")
select_seat_loc = (By.XPATH,"//span[text()='SELECT SEAT'][1]")
boarding_point_sele_loc = (By.XPATH,"//p[text()='Boarding Point']//following::span[@class='RadioButtonstyles__Checkmark-sc-wz601o-1 bFGqGl'][4]")