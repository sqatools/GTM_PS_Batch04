def test_facebook_login():
    import time
    from datetime import datetime
    from selenium.webdriver.chrome.options import Options
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    from selenium.webdriver.common.alert import Alert

    option = Options()
    option.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()

    def get_wait(timeout=10):
        wait = WebDriverWait(driver, timeout)
        return wait

    def Randow_name():
        return datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    driver.get("https://www.facebook.com/login.php")
    time.sleep(2)
    var_name = Randow_name()
    driver.save_screenshot(f"C:\\Users\\subra\\OneDrive\\Desktop\\selenium\\Screenshot\\Facebook_Login{var_name}.png")
    username = get_wait().until(ec.element_to_be_clickable((By.NAME, "email")))
    username.send_keys("Testing01@gmail.com")
    time.sleep(5)
    driver.save_screenshot(f"C:\\Users\\subra\\OneDrive\\Desktop\\selenium\\Screenshot\\Facebook_login{var_name}.png")
    print("username is enable", username.is_enabled())

    password = get_wait(timeout=5).until(ec.presence_of_element_located((By.NAME, "pass")))
    password.send_keys("Test@1234")
    time.sleep(5)
    driver.save_screenshot(f"C:\\Users\\subra\\OneDrive\\Desktop\\selenium\\Screenshot\\Facebook_passwor{var_name}.png")
    print('password is displayed', password.is_displayed())
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@value='1']").click()
    driver.save_screenshot(f"C:\\Users\\subra\\OneDrive\\Desktop\\selenium\\Screenshot\\Facebook_home{var_name}.png")
    time.sleep(10)
    # alert=Alert(driver)
    # time.sleep(5)
    # alert.accept()
    print(driver.title)
    driver.close()

