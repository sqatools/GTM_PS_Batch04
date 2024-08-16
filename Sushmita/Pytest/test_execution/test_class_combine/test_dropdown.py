import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("get_driver_session")
class TestDummyWebsite:

    @pytest.fixture(autouse=True)
    def setup(self, get_driver_session):
        self.driver = get_driver_session


    def test_country(self):
        ele=self.driver.find_element(By.ID,"billing_country")
        s_obj=Select(ele)
        s_obj.select_by_visible_text("United Kingdom")

    def test_link(self):
        ele1=self.driver.find_element(By.LINK_TEXT,'Manual Testing')
        ele1.click()
        text=self.driver.find_element(By.XPATH,'//h3[@itemprop="name"]')
        print(text.getText())
