from selenium.webdriver.common.by import By

source_city = "Bengaluru"

close_popup_link = "//span[@class='logSprite icClose']"
flight_link = "//span[text()='Flights']"
oneway = "//p[text()='One-way']//preceding-sibling::span"
enter_city = "//span[text()='From']//following-sibling::p[text()='Enter city or airport']"
click_input = "//span[text()='From']//following-sibling::input"
source_city = "//span[text()='{source_city_name}"
