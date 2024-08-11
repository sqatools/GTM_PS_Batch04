import pytest
from selenium.webdriver.common.by import By


def test_manual(driver):
     driver.find_element(By.LINK_TEXT,'Manual Testing').click()
     print('Title:',driver.title)


@pytest.mark.usefixtures('session_fix')
class ManualTesting:
    pass
