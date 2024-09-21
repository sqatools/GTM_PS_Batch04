from selenium.webdriver.common.by import By

search_type_locator = (By.XPATH,"//input[@id='srchword']")
search_data = "bracelet"
click_search_locator = (By.XPATH,"//input[@class='newsrchbtn']")
product_locator = (By.XPATH,"//img[contains(@title,'Tiger Eye Crystal And Rudraksha Stretch')]")
pin_locator = (By.XPATH,"//input[@name='inputPincode']")
pin_value = "695141"
check_loc = (By.XPATH,"//span[@id='checkPinBtn']")
buy_now_loc = (By.XPATH, "//input[@value='Buy now']")
place_order_loc = (By.XPATH,"//input[@name='buynow']")