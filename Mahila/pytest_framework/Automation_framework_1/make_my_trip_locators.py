from selenium.webdriver.common.by import By


close_pop_up_locator = (By.XPATH,"//span[@class='commonModal__close']")
click_from_locator = (By.XPATH,"//span[text()='From']")
send_from_locator = (By.XPATH,"//input[@placeholder='From']")
select_from_locator = (By.XPATH,f"//span[text()={'select_from_value'}]")
