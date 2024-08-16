import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='class')
def get_driver(request):
     driver=webdriver.Chrome()
     driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
     driver.maximize_window()
     driver.implicitly_wait(10)
     request.cls.driver=driver
     yield
     driver.close()
