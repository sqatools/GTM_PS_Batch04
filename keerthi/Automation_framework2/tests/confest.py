import pytest
from selenium import webdriver
from resource.goibibo_website.bus_booking_page_data import goibibo_url

@pytest.fixture(scope="class")
def get_driver_goibibo(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(goibibo_url)
    request.cls.driver = driver
    yield
    driver.close()