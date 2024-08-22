from selenium.webdriver.common.by import By

##### test data ####
dummy_website_url = "https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"
first_name_value = "John"
last_name_value = "Jenny"

#### locators ######
first_name_locator = (By.XPATH, "(//input[@name='firstname'])[1]")
last_name_locator = (By.XPATH, "(//input[@name='firstname'])[2]")

dob_locator = (By.ID, "birthday")
male_locator = (By.ID, "male")
addmore_passenger_dd_locator = (By.ID, "admorepass")
one_way_locator = (By.ID, "oneway")
from_city_locator =(By.ID, "fromcity")
dest_city_locator = (By.ID, "destcity")
checkboxes_list_locator = (By.XPATH, "//input[@type='checkbox']")
