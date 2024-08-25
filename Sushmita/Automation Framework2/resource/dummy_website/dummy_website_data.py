from selenium.webdriver.common.by import By

first_name_value="sai"
last_name_value="sree"
dob_value='07-09-2024'
no_of_pass="Add 1 more passenger (100%)"
from_city_value='Bangalore'
dest_city_value='Delhi'

depart_value='26-08-2024'
return_value='27-08-2024'
delivery_date_value="27-08-2024"
billing_name='John'
billing_phone='345698'
billing_email='john@gmail.com'
billing_street='Rani chowk'
billing_country='United Kingdom'
billing_postcode='56789'
billing_prefectue='20'


#locator
first_name_locator=(By.XPATH,"(//input[@id='firstname'])[1]")
last_name_locator=(By.XPATH,"(//input[@id='firstname'])[2]")
dob_locator=(By.ID,"birthday")
click_locator=(By.ID,"female")
Num_passanger_locator=(By.ID,"admorepass")
travel_details_locator=(By.ID,"roundtrip")
from_city_locator=(By.ID,"fromcity")
dest_city_locator=(By.ID,"destcity")
depart_locator=(By.NAME,"departdate")
return_locator=(By.NAME,"returndate")
delivery_option_locator=(By.ID,"visadate")
dummy_radio_locator=(By.ID,'whatsapp')
billing_name_locator=(By.ID,'billing_name')
billing_phone_locator=(By.ID,'billing_phone')
billing_email_locator=(By.ID,'billing_email')
billing_adress_locator=(By.ID,'billing_address')
billing_country_locator=(By.ID,"billing_country")
billing_postcode_locator=(By.ID,"postcode")
billing_prefecture_locator=(By.ID,"Prefecture")
city_locator=(By.XPATH,"//td[text()='6002']//preceding-sibling::td")




