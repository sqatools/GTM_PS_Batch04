from selenium.webdriver.common.by import By

#test data
enter_email_data = "amifoot1992@gmail.com"
enter_mobile_num_data= "790917527"
name_data = "Ami"
pass_data = 'mAhIlA@567'


#locator

signin_click_loc = (By.XPATH, "//span[text()='Hello, sign in']")    #CLICK
enter_email_loc = (By.XPATH, "//input[@name='email']")   #clear and then sendkeys
continue_button_loc = (By.XPATH,"//span[@id='continue']")   #click
enter_mobile_num_loc = (By.XPATH, "//input[@placeholder='Mobile number']")   #send key
name_loc = (By.XPATH, "//input[@placeholder='First and last name']")  #clear and send keys
pass_loc = (By.XPATH, "//input[@id='ap_password']") #clear and sendkeys
verify_mob_no = (By.XPATH, "//input[@class='a-button-input']")   #click