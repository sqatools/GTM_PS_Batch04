"""
pip install selenium
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
    # ID = "id"
    XPATH = "xpath"
    # LINK_TEXT = "link text"
    # PARTIAL_LINK_TEXT = "partial link text"
    # NAME = "name"
    # TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
"""

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
# ID Locator
driver.find_element(By.ID, "fromcity").send_keys("Mumbai")
driver.find_element(By.ID, "destcity").send_keys("Bangalore")

# TAG_NAME Locator
header_element = driver.find_element(By.TAG_NAME, "h1")
# text method help to print text of any specific element
print(header_element.text)


#driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
# LINK TEXT Locator
driver.find_element(By.LINK_TEXT, "Manual Testing").click()
# element_link_text = driver.find_element(By.LINK_TEXT, "Software Testing Methods")
#element_link_text.click()

# PARTIAL_LINK_TEXT
element_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Testing Methods")
element_link_text.click()


time.sleep(10)
driver.close()
