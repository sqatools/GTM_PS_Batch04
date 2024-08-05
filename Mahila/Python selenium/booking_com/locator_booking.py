from selenium.webdriver.common.by import By

one_way = (By.XPATH,"//div[text()='One-way']//parent::span")

seat_type =(By.XPATH,"//select[@name='sr_cabin_class']")

from_destiny =(By.XPATH,"//button[@class='ShellButton-module__btn___tCJzz']")
from_destiny_type = (By.XPATH,"//input[@placeholder='Airport or city']")
from_destiny_select = 'Cochin International Airport'

To_destiny =(By.XPATH,"//span[text()='Where to?']")
To_destiny_type =(By.XPATH,"//input[@placeholder='Airport or city']")
To_destiny_select = 'Kempegowda International Airport'

Departure_date = (By.XPATH,"//button[@placeholder='Choose departure date']")
Departure_date_select = (By.XPATH,"//span[@data-date='2024-09-04']")

add_members = (By.XPATH,"//span[text()='1 adult']")
adding_adult_plus = (By.CSS_SELECTOR,"[data-ui-name='button_occupancy_adults_plus']")

adding_children = (By.CSS_SELECTOR,"[data-ui-name='button_occupancy_children_plus']")
select_child_age_drop =(By.XPATH,"//select[@name='sr_occupancy_children_age_0']")
select_child_age=(By.XPATH,"//select[@name='sr_occupancy_children_age_0']")
Done_selector = (By.XPATH,"//button[@type='button']//child::span[text()='Done']")

submit_selector =(By.XPATH,"//span[text()='Search']")
