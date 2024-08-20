from selenium.webdriver.common.by import By

##### test data ####
dummy_website_url = "https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"
first_name_value = "John"
last_name_value = "Jenny"

#### locators ######
first_name_locator = (By.XPATH, "(//input[@name='firstname1'])[1]")
last_name_locator = (By.XPATH, "(//input[@name='firstname'])[2]")
