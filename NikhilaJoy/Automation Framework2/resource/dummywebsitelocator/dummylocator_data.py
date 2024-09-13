from selenium.webdriver.common.by import By

fname="Nikhila"
lname="Joy"
dob="02-07-1998"

passanger=3
fcity="Banglore"
dcity="Bali"

ddate="09-10-2024"
rdate="17-10-2024"



first_name=(By.XPATH,"//input[@name='firstname1'][1]")
last_name=(By.XPATH,"//input[@name='firstname'][2]")

date_ofbirth=(By.ID,"birthday")
radio_button=(By.XPATH,"(//input[@id='female'])[1]")

add_passanger=(By.ID,"admorepass")
tripdetails=(By.ID,"roundtrip")
f_city=(By.ID,"fromcity")
d_city=(By.ID,"destcity")
d_date=(By.ID,"departdate")
r_date=(By.ID,"returndate")