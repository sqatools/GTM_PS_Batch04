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
# add_cart_ele=(By.XPATH,"//div[@class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_6']//div[@class='s-image-padding']")
# amzon_basic=(By.XPATH,"//a[text()='AmazonBasics']")

check_box_loc=(By.XPATH,"//li[@id='p_123/523267']//i[@class='a-icon a-icon-checkbox']")
slider_loc=(By.XPATH,"//div[@id='p_36/range-slider_slider-item']//following::input[@id='p_36/range-slider_slider-item_upper-bound-slider']")
go_price_loc=(By.XPATH,"//input[@aria-label='Go - Submit price range']")
L_loc=(By.XPATH,"//button[@value='L']")

Brand_loc=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/span[1]/div[1]/span[1]/div[1]/div[1]/div[3]/ul[1]/span[1]/span[5]/li[1]")
dress_loc=(By.XPATH,"//span[normalize-space()='Midi Dress | One Piece Dress | Beach Dress for Women']")
cart_loc=(By.XPATH,"//input[@id='add-to-cart-button']")
proceed_loc=(By.XPATH,"//input[@name='proceedToRetailCheckout']")
your_address_loc=(By.XPATH,"//div[@class='a-row panel-content']//div[3]//span[1]//div[1]//label[1]")
use_address_loc=(By.XPATH,"//input[@data-testid='Address_selectShipToThisAddress']")

