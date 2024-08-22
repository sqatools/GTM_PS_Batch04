import pytest
from selenium import webdriver
from resource.dummy_website.dummy_website_page_data import *
from resource.google_page.google_search_page_data import *

@pytest.fixture(scope="class")
def get_driver_dummy(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(dummy_website_url)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope="class")
def get_driver_google_search(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(google_search_url)
    request.cls.driver = driver
    yield
    driver.close()
