from selenium.webdriver.common.by import By

#testdata
phone_number_data = "7909175279"


#locator

close_pop_up_loc = (By.XPATH, "//div[@data-id='auth-flow-section']//child::span//span[@class='logSprite icClose']")
signin_loc = (By.XPATH,"//li[text()='Manage Your Trips']//following-sibling::li[1]")
phone_number_loc = (By.XPATH,"//input[@name='phone']")
