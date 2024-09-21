from selenium.webdriver.common.by import By

#data
enter_email_data = "mahila618mahesh@gmail.com"
enter_pass_data = "mAhIlA@123"
search_product_data = "Shoes"
shoe_size = "10 UK"


#locator

signin_click_loc = (By.XPATH, "//span[text()='Hello, sign in']")
enter_email_loc = (By.XPATH, "//input[@name='email']")   #clear and sendkey
continue_button_loc = (By.XPATH, "//input[@type='submit']")
enter_pass_loc = (By.XPATH, "//input[@id='ap_password']")   #sendkey
click_sign_in_loc = (By.XPATH, "//input[@id='signInSubmit']")
search_product_loc = (By.XPATH,"//label[text()='Search Amazon.in']//following-sibling::input") #send key
search_button_loc =(By.ID, "nav-search-submit-button")
delivery_day_loc = (By.XPATH,"//span[text()='Get It in 2 Days']//preceding::i[@class='a-icon a-icon-checkbox'][1]")
add_to_cart_loc = (By.XPATH,"//button[text()='Add to cart' and @id='a-autoid-117-announce']")
click_select_size_loc = (By.XPATH,"//span[@class='a-dropdown-prompt' and text()='9 UK']")
select_size_loc = (By.XPATH,f"//a[@class='a-dropdown-link' and text()='{shoe_size}']")
show_details_loc = (By.XPATH, "//a[text()='See all item details']")
buy_now_loc = (By.XPATH,"//input[@id='buy-now-button']")
change_pay_method_loc= (By.XPATH, "//a[@id='payChangeButtonId']")
click_card_loc =  (By.XPATH,"//input[@id='pp-4WgaPe-119']")
