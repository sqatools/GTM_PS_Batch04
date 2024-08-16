import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('get_driver')
class ActionChain:

    def test_action_chain(self):
        tester_ele = self.driver.find_element(By.XPATH, "//div[@id='menu']//a[text()='Tester’s Hub']")
        action: ActionChains = ActionChains(self.driver)
        action.move_to_element(tester_ele)
        action.perform()
