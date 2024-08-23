import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    # driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope='session')
def get_driver_session():
    driver = webdriver.Chrome()
    #driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=None, help="Browser to initiate the automation")
    parser.addoption("--headless", action="store", default=None, help="GUI execution option")
#-----without headless option------------
# @pytest.fixture(scope='class')
# def get_driver_with_browser(request, pytestconfig):
#     browser = pytestconfig.getoption("browser")
#     headless = pytestconfig.getoption("headless")
#     driver = None
#     if browser.lower()=="chrome":
#         driver=webdriver.Chrome()
#     elif browser.lower()=="firefox":
#         driver=webdriver.Firefox()
#     elif browser.lower()=="edge":
#         driver=webdriver.Edge()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
#     request.cls.driver=driver
#     yield
#     driver.close()

#----------with headless option-------------
@pytest.fixture(scope='class')
def get_driver_with_browser(request, pytestconfig):
    browser = pytestconfig.getoption("browser")
    headless = pytestconfig.getoption("headless")
    driver = None
    if browser is None:
        chr_option = Options()
        if headless:
            chr_option.add_argument('--headless')
        driver = webdriver.Chrome(options=chr_option)
    elif browser.lower() == "chrome":
        chr_option = Options()
        if headless:
            chr_option.add_argument('--headless')
        driver = webdriver.Chrome(options=chr_option)
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    request.cls.driver = driver
    yield
    driver.close()
