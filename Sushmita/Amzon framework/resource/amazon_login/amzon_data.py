from selenium.webdriver.common.by import By

email_input="8150997102"
password="Arasu@102"


acc_signin_loc=(By.XPATH,"//a[@id='nav-link-accountList']")
signin_loc=(By.XPATH,"//span[text()='Sign in']")
email_loc=(By.XPATH,"//input[@type='email']")
continue_loc=(By.XPATH,"//input[@type='submit']")
password_loc=(By.XPATH,"//input[@type='password']")
signin_button=(By.XPATH,"//input[@id='signInSubmit']")
