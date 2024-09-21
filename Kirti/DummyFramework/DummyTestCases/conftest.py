from selenium import webdriver
import pytest
from Resource.DummyLocators import *

@pytest.fixture(scope="class")
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    request.cls.driver = driver
    yield
    driver.close()
















