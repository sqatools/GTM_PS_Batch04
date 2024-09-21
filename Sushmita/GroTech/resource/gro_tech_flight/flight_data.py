from selenium import webdriver
from selenium.webdriver.common.by import By
from_city="BLR - Bangalore, IN"
to_city="DEL - New Delhi, IN"
depart_date="31-08-2024"
return_date="02-09-2024"
adult_val="2"
children_val="1"

flight_flippop = (By.XPATH,
                  "//div[@class='elementor-element elementor-element-8968a3c elementor-flip-box--effect-flip elementor-flip-box--direction-up elementor-widget elementor-widget-flip-box']//div[@class='elementor-flip-box__layer elementor-flip-box__front']//div[@class='elementor-flip-box__layer__overlay']")
flight_readmore =(By.XPATH,"//a[@href='https://grotechminds.com/flights/']")
oneway_loc = (By.XPATH,"//input[@value='Round trip']")
from_loc=(By.XPATH,"//select[@name='From']")
To_loc=(By.XPATH,"//select[@name='To']")
Depart_loc=(By.XPATH,"//input[@name='Departon']")
return_loc=(By.XPATH,"//input[@name='Returnon']")
adult_loc=(By.XPATH,"//select[@name='Adults']")
children_loc=(By.XPATH,"//select[@name='Children']")
search_loc=(By.XPATH,"//input[@value='Search flights']")
