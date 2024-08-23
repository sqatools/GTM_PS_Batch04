from selenium.webdriver.common.by import By

##### Test data ######
goibibo_url = "https://www.goibibo.com/"
src_city_name = "Mumbai, Maharashtra"
dest_city_name = "Bangalore, Karnataka"
travel_date = 26
bus_name = "Ravina Travels (Regd)"


###### Locators ######
login_popup_close = (By.XPATH, "//span[@class='logSprite icClose']")
bus_booking_page_link = (By.XPATH, "//span[text()='Bus']//parent::a")
enter_source_field_locator = (By.XPATH, "//input[@placeholder='Enter Source']")
enter_destination_field_locator = (By.XPATH, "//input[@placeholder='Enter Destination']")
calender_locator = (By.XPATH, "//input[@data-testid='openCheckinCalendar']")
date_locator = (By.XPATH, "//span[text()='24']//parent::li")
search_bus_button = (By.XPATH, "//button[text()='Search Bus']")
select_seat_button = (By.XPATH, "(//p[text()='RESHMA TOURISTS'])[1]//parent::div//following-sibling::div[2]//button")
boarding_point_location = (By.XPATH, "//p[text()='Boarding Point']//parent::div//label[contains(@class, 'LocationPoints')][1]")
dropping_point_location = (By.XPATH, "//p[text()='Dropping Point']//parent::div//label[contains(@class, 'LocationPoints')][1]")
select_first_upper_seat = (By.XPATH, "(//span[text()='UPPER']//parent::aside//following-sibling::aside//div[contains(@class, 'SeatWithTooltips')])[1]")
select_seat_continue_button = (By.XPATH, "//button[text()='CONTINUE']")
review_booking_header = (By.XPATH, "//header[text()='Review your Booking']")
