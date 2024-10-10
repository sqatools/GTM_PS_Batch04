# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
#
# driver=webdriver.Chrome()
# driver.maximize_window()
# def get_element(locator,wait_time=10):
#     wait=WebDriverWait(driver,timeout=wait_time)
#     element=wait.until(ec.presence_of_element_located(locator))
#     return element
#
# def select_dropdown_value(locator,value):
#     element=get_element(locator)
#     select=Select(element)
#     select.select_by_visible_text(value)
#
# def handle_dd_value():
#     driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
#     country_DD_List=(By.ID,"billing_country")
#     country_DD_ele=get_element(country_DD_List)
#     select_obj=Select(country_DD_ele)
#     #select_obj.select_by_visible_text("Åland Islands")
#     #select_obj.select_by_index(7)
#     select_obj.select_by_value("AI")
#     time.sleep(5)
#
# handle_dd_value()
# driver.close()
# test_my_module.py

import unittest
from my_module import add

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add(-1, -1)
        self.assertEqual(result, -2)

    def test_add_mixed_numbers(self):
        result = add(-1, 1)
        self.assertEqual(result, 0)

    def test_add_zero(self):
        result = add(0, 0)
        self.assertEqual(result, 0)

    def test_add_large_numbers(self):
        result = add(123456789, 987654321)
        self.assertEqual(result, 1111111110)


if __name__ == '__main__':
    unittest.main()
