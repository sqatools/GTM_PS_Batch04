from selenium.webdriver.common.by import By
city_name='Bangalore, Karnataka, India'

#close_popup_link = (By.XPATH,"//span[@class='logSprite icClose']")
radio_button = (By.XPATH,"//input[@type='radio']")
landmark_loc = (By.XPATH,"//span[text()='Where']//following::div[1]")
select_landmark=(By.XPATH,"//span[text()='Where']//following::input[@placeholder='e.g. - Area, Landmark or Property Name']")
checkin_date=(By.XPATH,"//div[@data-testid='openCheckinCalendar']")
select_checkin_date=(By.XPATH,"//span[@data-testid='date_1_8_2024']")
