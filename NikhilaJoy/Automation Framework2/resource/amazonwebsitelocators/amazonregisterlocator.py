from selenium.webdriver.common.by import By


email="joynikhila98@gmail.com"
name="Nikhila Joy"
password="testamazon"


first_n_lname=(By.XPATH,"//input[@placeholder='First and last name']")
register_email=(By.XPATH,"//input[@id='ap_email']")
reg_password=(By.XPATH,"//input[@id='ap_password']")
recheck_password=(By.XPATH,"//input[@id='ap_password_check']")
submit=(By.XPATH,"//span[@class='a-button a-button-normal a-button-span12 a-button-primary']")
