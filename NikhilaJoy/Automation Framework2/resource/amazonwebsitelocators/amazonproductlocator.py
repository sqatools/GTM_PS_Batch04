from selenium.webdriver.common.by import By

search_data='women outfit'


search_field=(By.XPATH,"//input[@id='twotabsearchtextbox']")
search_button=(By.ID,"nav-search-submit-button")

size=(By.XPATH,"//button[@value='M']")

price_range=(By.XPATH,"//input[@aria-valuetext='₹1,200']")
go=(By.XPATH,"//input[@aria-label='Go - Submit price range']")