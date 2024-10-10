import pytest
from selenium.webdriver.chrome import webdriver


@pytest.fixture(scope='session')
def session_fix():
    driver = webdriver.Chrome()
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

@pytest.fixture(scope='function', autouse=True)
def wb_driver(session_fix):
    driver = session_fix
    return driver
