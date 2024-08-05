from selenium.webdriver.common.by import By

popup_close = (By.XPATH,"//span[@class = 'logSprite icClose']")
from_destiny_click = (By.XPATH,"//span[text()='From']//following-sibling::p")   #no need to click for TO once fromis typed it will autpmatically go to To

from_destiny_text = (By.XPATH,"//span[text()='From']//following-sibling::input[@type='text']")
from_destiny_name="Mumbai, India"

To_destiny_text = (By.XPATH,"//span[text()='To']//following-sibling::input[@type='text']")
To_destiny_name = 'Bengaluru, India'