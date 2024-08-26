from selenium.webdriver.common.by import By

##### test data ####
dummy_website_url = "https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"
first_name_value = "Sangeetha"
last_name_value = "kokkonda"
From_city_value="chennai"
Destination_city="Kakinada"
billing_name="sangeetha"
billing_phone="9059993936"
billing_email="sangeetha123@gmail.com"
billing_address="No119,f4,sai homes,chennai"
post_code="600053"
street_address="Ambattur,chennai"

### locators #########

first_name_locator= (By.XPATH, "(//input[@name='firstname'])[1]")
last_name_locator = (By.XPATH, "(//input[@name='firstname'])[2]")
From_city_locator = (By.XPATH,"//input[@id='fromcity']")
Destination_city_locator= (By.XPATH,"//input[@id='destcity']")
billing_name_locator=(By.XPATH,"//input[@id='billing_name']")
billing_phone_locator=(By.XPATH,"//input[@id='billing_phone']")
billing_email_locator=(By.XPATH,"//input[@id='billing_email']")
billing_address_locator=(By.XPATH,"//input[@id='billing_address']")
post_code_locator=(By.XPATH,"//input[@id='postcode']")
street_address_locator=(By.XPATH,"//input[@id='street_address1']")

dob_locator = (By.ID, "birthday")
male_locator = (By.ID, "female")
addmore_passenger_dd_locator = (By.ID, "admorepass")
one_way_locator = (By.ID, "oneway")
departure_date_locator=(By.ID,"departdate")
return_date_locator=(By.ID,"returndate")
visa_date_locator=(By.ID,"visadate")
whatsapp_locator=(By.ID,"whatsapp")
country_locator=(By.ID,"billing_country")
checkbox_list_locator=(By.XPATH,"(//input[@type='checkbox'])[3]")
radio_button_locator=(By.XPATH,"(//input[@type='radio'])[2]")



