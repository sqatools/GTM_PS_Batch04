import time
import pytest

from selenium import webdriver


@pytest.mark.parametrize("browser,website",[(webdriver.Chrome(),"https://www.google.com"),
                                              (webdriver.Firefox(),"https://www.google.com/"),
                                              (webdriver.Edge(),"https://www.booking.com/")])
def test_lauch_site(browser,website):
    driver = browser
    driver.get(website)
    driver.maximize_window()
    time.sleep(5)

