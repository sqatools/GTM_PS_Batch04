from selenium.webdriver.common.by import By

#data
enter_email_data1 = "mahila618mahesh@gmail.com"
enter_email_data2 = "mahila618mahesh"
enter_pass_data1 = "mAhIlA@123"
enter_pass_data2 = "12"

#locator

signin_click_loc = (By.XPATH, "//span[text()='Hello, sign in']")
enter_email_loc = (By.XPATH, "//input[@name='email']")   #clear and sendkey
continue_button_loc = (By.XPATH, "//input[@type='submit']")
enter_pass_loc = (By.XPATH, "//input[@id='ap_password']")   #sendkey
click_sign_in_loc = (By.XPATH, "//input[@id='signInSubmit']")