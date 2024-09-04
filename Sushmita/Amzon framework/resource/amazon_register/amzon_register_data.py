from selenium.webdriver.common.by import By

email_input="8150997102"
password="Arasu@102"
search_data='dresses for women'

acc_signin_loc=(By.XPATH,"//a[@id='nav-link-accountList']")
#new_customer=(By.LINK_TEXT, 'Start here.')
signin_loc=(By.XPATH,"//input[@type='email']")
#email_loc=(By.XPATH,"//input[@type='email']")
continue_loc=(By.XPATH,"//input[@type='submit']")
password_loc=(By.XPATH,"//input[@type='password']")
signin_button=(By.XPATH,"//input[@id='signInSubmit']")
search_loc=(By.XPATH,"//form[@id='nav-search-bar-form']//following::input[@type='text']")
search_button=(By.XPATH,"//input[@id='nav-search-submit-button']")
all_loc=(By.XPATH,"//a[@id='nav-hamburger-menu']")
account_loc=(By.XPATH,"//a[@class='hmenu-item'][normalize-space()='Your Account']")
adress_loc=(By.XPATH,"//span[normalize-space()='Edit addresses for orders and gifts']")
#best_seller=(By.XPATH,"//ul[@class='hmenu hmenu-visible']//a[@class='hmenu-item'][normalize-space()='Best Sellers']")
add_cart_ele=(By.XPATH,"//div[@class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_6']//div[@class='s-image-padding']")
amzon_basic=(By.XPATH,"//a[text()='AmazonBasics']")
