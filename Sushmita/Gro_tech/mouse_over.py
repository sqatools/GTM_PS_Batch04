import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()


# driver.get("https://grotechminds.com/hoverable-dropdown/")
# drop_down = driver.find_element(By.XPATH, "//button[@class='dropbtn']//parent::div[@class='dropdown']")
# action_chain = ActionChains(driver)
# action_chain.move_to_element(drop_down)
# action_chain.perform()
# time.sleep(10)
# element = driver.find_element(By.XPATH, "//select[@id='outer-dropdown']")
#
# select = Select(element)
# select.select_by_visible_text("Drop2")


# select.select_by_value('2')
# //select[@id='outer-dropdown']

class GroTech():

    def select_value(self):
        driver.get("https://grotechminds.com/multi-level-dropdown/")
        element = driver.find_element(By.XPATH, "//select[@id='outer-dropdown']")
        select = Select(element)
        select.select_by_visible_text("Drop4")
        time.sleep(10)

        # ss=GroTech()
        # ss.select_value()
        # //input[@value='20']

    def slider_ele(self):
        driver.get("https://grotechminds.com/slider/")
        driver.maximize_window()
        ele = driver.find_element(By.XPATH, "//input[@value='20']")
        ActionChains(driver).drag_and_drop_by_offset(ele, 200, 0).perform()
        time.sleep(10)

    # se=GroTech()
    # se.slider_ele()

    def amzon_slider(self):
        driver.get("https://www.amazon.in/s?k=dress+for+women")
        driver.maximize_window()
        driver.execute_script('window.scrollBy(0,2000)', "")

        ele1 = driver.find_element(By.XPATH, "//input[@id='p_36/range-slider_slider-item_lower-bound-slider']")
        ActionChains(driver).drag_and_drop_by_offset(ele1, 200, 0).perform()
        time.sleep(10)

    # at = GroTech()
    # at.amzon_slider()

    def mouse_mover(self):
        driver.get("https://grotechminds.com/mousemover/")
        demo_link = driver.find_element(By.XPATH,
                                        "//div[@class='has_eae_slider elementor-element elementor-element-8e321a7 e-con-full e-flex e-con e-child']")
        action = ActionChains(driver)
        action.click(demo_link)
        action.perform()
        time.sleep(10)

    # mm = GroTech()
    # mm.mouse_mover()

    def hover_over(self):
        driver.get("https://grotechminds.com/hoverover/")
        demo_1 = driver.find_element(By.XPATH,
                                     "//div[@class='has_eae_slider elementor-element elementor-element-1857001 e-con-full e-flex e-con e-child']")
        action = ActionChains(driver)
        action.move_to_element(demo_1)
        prac = driver.find_element(By.XPATH,
                                   "//div[@class='has_eae_slider elementor-element elementor-element-1857001 e-con-full e-flex e-con e-child']//div[3]")
        action.click(prac)
        action.perform()

        time.sleep(10)

    # hh = GroTech()
    # hh.hover_over()

    def flight_appl(self):
        driver.get("https://grotechminds.com/automate-me/")

        flip_over = driver.find_element(By.XPATH,
                                        "//div[@class='elementor-element elementor-element-8968a3c elementor-flip-box--effect-flip elementor-flip-box--direction-up elementor-widget elementor-widget-flip-box']//div[@class='elementor-flip-box__layer elementor-flip-box__front']//div[@class='elementor-flip-box__layer__overlay']")
        action = ActionChains(driver)
        action.move_to_element(flip_over)
        action.perform()

        driver.find_element(By.XPATH, "//a[@href='https://grotechminds.com/flights/']").click()
        time.sleep(10)

    # fa = GroTech()
    # fa.flight_appl()

    def handle_alert(self):
        driver.get("https://grotechminds.com/alert/")
        alert = Alert(driver)
        ele=driver.find_element(By.XPATH, "//div[@class='elementor-element elementor-element-ad9960e elementor-widget elementor-widget-html']//button[@class='bbb'][normalize-space()='Received1']")
        ele.click()
        #print(alert.text)
        time.sleep(10)
        alert.accept()
       # print(alert.text)

# aa = GroTech()
# aa.handle_alert()

    def handle_alert1(self):
        driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
        alert = Alert(driver)
        ele=driver.find_element(By.XPATH, "//input[@value='Alert Box']")
        ele.click()
        print(alert.text)
        time.sleep(10)
        alert.accept()
       # print(alert.text)

ha=GroTech()
ha.handle_alert1()
