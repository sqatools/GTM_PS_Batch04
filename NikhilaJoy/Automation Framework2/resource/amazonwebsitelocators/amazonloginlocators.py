from selenium.webdriver.common.by import By


email="joynikhila98@gmail.com"
password="testamazon"




login=(By.XPATH,"(//a[@class='nav-a nav-a-2   nav-progressive-attribute'])[1]")
login_email=(By.XPATH,"//input[@id='ap_email_login']")
login_submit=(By.XPATH,"//input[@class='a-button-input']")
login_password=(By.XPATH,"//input[@id='ap_password']")
login_signin=(By.XPATH,"//input[@id='signInSubmit']")

