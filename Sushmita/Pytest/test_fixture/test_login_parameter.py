import time
from selenium import webdriver
import pytest
from data_file import *


@pytest.mark.parametrize("username , password ", [('user1', 'pass1'),
                                                  ('user2', 'pass2'),
                                                  ('user3', 'pass3'),
                                                  ('user4', 'pass4')])
def test_login(username, password):
    print("credentials :", username, password)


@pytest.mark.parametrize("username , password ", param_data)
def test_login2(username, password):
    print("credentials :", username, password)


@pytest.mark.parametrize("username, password", excel_data)
def test_login_3(username, password):
    print("credentials :", username, password)


@pytest.mark.parametrize("username, password", bulk_data)
def test_login_4(username, password):
    print("credentials :", username, password)

# @pytest.mark.parametrize("browser , website", [
#     (webdriver.Chrome(), 'https://www.facebook.com'),
#     (webdriver.Firefox(), 'https://www.google.co.in'),
#     (webdriver.Edge(), 'https://www.goibibo.com/')
# ])
# def test_launch_website(browser,website):
#     driver=browser
#     driver.get(website)
#     driver.maximize_window()
#     time.sleep(5)
