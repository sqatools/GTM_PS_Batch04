from selenium.webdriver.common.by import By
enter_from_city_data ="Bengaluru"
source_city_name = "Bengaluru, India"
to_city_data="Delhi"
Dest_city_name="New Delhi, India"
depart_date="sept 4 2024"

close_popup_link = (By.XPATH,"//span[@class='logSprite icClose']")
flight_link =(By.XPATH, "//span[text()='Flights']")
oneway = (By.XPATH,"//p[text()='One-way']//preceding-sibling::span")
enter_city = (By.XPATH,"//span[text()='From']//following-sibling::p[text()='Enter city or airport']")
click_input = (By.XPATH,"//span[text()='From']//following-sibling::input")
source_city = (By.XPATH, f"//span[text()='{source_city_name}']")
To_city=(By.XPATH,"//span[text()='To']//following-sibling::p[text()='Enter city or airport']")
to_city_input=(By.XPATH,"//span[text()='To']//following-sibling::input[@type='text']")
to_city_name= (By.XPATH,f"//span[text()='{Dest_city_name}']")
depart_date_click=(By.XPATH,"//span[text()='Departure']//parent::div")
departure_date_select_loc = (By.XPATH, "//div[@aria-label='Wed Sep 04 2024']")
traveller_class=(By.XPATH,"//span[text()='Travellers & Class']//parent::div")
adult_loc=(By.XPATH,"//p[text()='Adults']//following::span[3]")
children_loc=(By.XPATH,"//p[text()='Children']//following::span[3]")
Infant_loc=(By.XPATH,"//p[text()='Infants']//following::span[3]")
economy_loc=(By.XPATH,"//li[text()='premium economy']")
done_loc=(By.XPATH,"//a[text()='Done']")
search_loc=(By.XPATH,"//span[text()='SEARCH FLIGHTS']")
