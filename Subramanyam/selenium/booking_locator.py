from selenium.webdriver.common.by import By
url="https://www.booking.com/flights/index.en-gb.html?aid=2369661&label=msn-HiTydpHndf_KligNqm9Sgw-79852220055838%3Atikwd-79852393960302%3Aloc-90%3Aneo%3Amte%3Alp149155%3Adec%3Aqsbooking.com&sid=3260e6e44599da2c2d28352189dbaaf6&from=booking&"
one_way_flight=(By.XPATH,"//div[text()='One way']//parent::span")
flight_class=(By.XPATH,"//select[@name='sr_cabin_class']")
premium_class=(By.XPATH,"//div[text()='Premium economy']")
From=(By.XPATH,"//button[@data-ui-name='input_location_from_segment_0']")
cancel_already_one=(By.XPATH,"//span[@class='Tags-module__text___E+6Qz']//following-sibling::span")
from_airport=(By.XPATH,"//input[@placeholder='Airport or city']")
from_city_in_list=(By.XPATH,"//ul[@id='flights-searchbox_suggestions']")

To=(By.XPATH,"//span[text()='Where to?']")
to_airport=(By.XPATH,"//input[@placeholder='Airport or city']")
to_city_in_list=(By.XPATH,"//ul[@id='flights-searchbox_suggestions']")
Choose_departure_date=(By.XPATH,"//button[@placeholder='Choose departure date']")
next_month=(By.XPATH,"//div[@data-ui-name='calendar_body']//button")
Aug_14=(By.XPATH,"//span[contains(@aria-label,'14 Oct')]")
Adult=(By.XPATH,"//span[text()='1 adult']")
add_adult=(By.CSS_SELECTOR,"[data-ui-name='button_occupancy_adults_plus']")
Done_button=(By.XPATH,"//span[text()='Done']")
search_button=(By.CSS_SELECTOR,"[data-ui-name='button_search_submit']")