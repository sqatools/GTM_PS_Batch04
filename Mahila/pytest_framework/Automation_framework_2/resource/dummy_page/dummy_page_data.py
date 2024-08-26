from selenium.webdriver.common.by import By


#data file

first_name_data = "Mahila"
sec_name_data = "Mahesh"
dob_data = "23-08-1999"
no_of_add_pass_data = "Add 1 more passenger (100%)"
from_city_data = "Chennai"
dest_city_data = "Bengaluru"
dep_date_data = "23-08-2024"
ret_date_data = "23-10-2024"
app_date_data = "23-07-2024"
bill_name_data = "Mahila"
bill_phone_data = "7363738239"
bill_email_data = "mahila76728@gamail.com"
bill_add_data = "A128 Flemco Banglore"
bill_coun_data = "American Samoa"
post_code_data = "8776659"
prefecture_data = "34354667"
stree_add1_data = "A 128 flexing compo"
stree_add2_data = "Banglore,Karnataka"


#locator

radio_button_loc = (By.XPATH, "//input[@value='radio_678']")
first_name_loc = (By.XPATH, "//input[@id='firstname'][1]")
sec_name_loc = (By.XPATH, "//input[@id='firstname'][2]")
dob_loc = (By.ID, "birthday")
gender_loc = (By.XPATH, "//span[text()='Female']//preceding-sibling::input[@id='female']")
no_of_add_pass_loc = (By.ID, "admorepass")
travel_det_loc = (By.ID, "roundtrip")
from_city_loc = (By.ID, "fromcity")
dest_city_loc = (By.ID, "destcity")
dep_date_loc = (By.ID, "departdate")
ret_date_loc = (By.ID, "returndate")
app_date_loc = (By.ID, "visadate")
recieve_ticket_loc = (By.XPATH, "//span[text()='WhatsApp']//preceding-sibling::input[@id='whatsapp']")
bill_name_loc = (By.ID, "billing_name")
bill_phone_loc = (By.ID, "billing_phone")
bill_email_loc = (By.ID, "billing_email")
bill_add_loc = (By.ID, "billing_address")
bill_coun_loc = (By.ID, "billing_country")
post_code_loc = (By.XPATH, "//input[@id='postcode']")
prefecture_loc = (By.XPATH, "//input[@id='Prefecture']")
stree_add1_loc = (By.XPATH, "//input[@id='street_address1']")
stree_add2_loc = (By.XPATH, "//input[@id='street_address2']")
most_visit_city_loc = (By.XPATH,"//input[@type='checkbox']//following::input")