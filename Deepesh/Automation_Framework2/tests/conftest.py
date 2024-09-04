import pytest
from selenium import webdriver
from resource.dummy_website.dummy_website_page_data import dummy_website_url
from resource.google_page.google_search_page_data import google_search_url
from resource.goibibo_website.bus_booking_page_data import goibibo_url
from base.web_driver_factory import WebdriverFactory

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=None, help="Browser to initiate the automation")
    parser.addoption("--headless", action="store", default=None, help="GUI execution option")


@pytest.fixture(scope="class")
def get_driver_dummy(request, pytestconfig):
    browser = pytestconfig.getoption("browser")
    headless = pytestconfig.getoption("headless")
    wd = WebdriverFactory(browser, headless)
    driver = wd.get_driver()
    driver.maximize_window()
    driver.get(dummy_website_url)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope="class")
def get_driver_google_search(request, pytestconfig):
    browser = pytestconfig.getoption("browser")
    headless = pytestconfig.getoption("headless")
    wd = WebdriverFactory(browser, headless)
    driver = wd.get_driver()
    driver.maximize_window()
    driver.get(google_search_url)
    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture(scope="class")
def get_driver_goibibo(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(goibibo_url)
    request.cls.driver = driver
    yield
    driver.close()
