import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datafile import param_data
from datafile import excel_data
from datafile import bulk_data


@pytest.mark.parametrize("username , password",[('user1','pass1'),
                                                 ('user2','pass2'),
                                                 ('user3','pass3'),
                                                ('user4','pass4')] )
def test_login(username,password):
    print("credentials :",username,password)

@pytest.mark.parametrize("username, password", param_data)
def test_login_2(username, password):
    print("credentials :", username, password)

@pytest.mark.parametrize("username, password", excel_data)
def test_login_3(username, password):
    print("credentials :", username, password)

@pytest.mark.parametrize("username, password", bulk_data)
def test_login_4(username, password):
    print("credentials :", username, password)

"""@pytest.mark.parametrize("browser, website",[(webdriver.Chrome(),"https://www.google.com"),
                                             (webdriver.Firefox(), "https://www.facebook.com"),
                                             (webdriver.Edge(), "https://www.instagram.com")
                                             ])
def test_launchwebsite(browser , website):
    driver=browser
    driver.get(website)
    driver.maximize_window()
    time.sleep(5)
"""
