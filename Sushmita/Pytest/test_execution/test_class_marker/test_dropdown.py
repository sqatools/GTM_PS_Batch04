import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.usefixtures('get_driver')
class TestDropDown:

    @pytest.mark.smoke
    def test_add_passenger(self):
        self.driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
        add_pass=self.driver.find_element(By.ID,'admorepass')
        s_obj=Select(add_pass)
        s_obj.select_by_visible_text('Add 1 more passenger (100%)')
        time.sleep(10)

    @pytest.mark.smoke
    def test_appoint_date(self):
        self.driver.find_element(By.ID,'visadate').send_keys('09-07-2027')
        time.sleep(10)

    @pytest.mark.smoke
    def test_country(self):
        country=self.driver.find_element(By.ID,'billing_country')
        s_obj=Select(country)
        s_obj.select_by_visible_text('United Kingdom')

    # def test_actionchain(self):
    #     self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    #     ebook=self.driver.find_element(By.XPATH,"//div[@id='menu']//a[text()='Free Ebooks']")
    #     action=ActionChains(self.driver)
    #     action.move_to_element(ebook)
    #     action.perform()
