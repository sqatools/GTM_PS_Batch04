import os.path
import time
import logging
import pytest
from selenium.webdriver.common.by import By

log = logging.getLogger(__name__)


# log.info()
# log.warning()
# log.error()
# log.critical()
# log.exception()


@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:

    @pytest.mark.regression
    def test_booking_info(self):
        from_city_locator = (By.ID, "fromcity")
        from_city_value = "Mumbai"
        log.info(f"{from_city_locator}: {from_city_value}")
        self.driver.find_element(*from_city_locator).send_keys(from_city_value)

        dest_locator = (By.ID, "destcity")
        dest_value = "Pune"
        log.info(f"{dest_locator}: {dest_value}")
        try:
            self.driver.find_element(*dest_locator).send_keys(dest_value)
        except Exception as e:
            file_path = os.path.join(os.path.curdir, "logs\\element_not_found.png")
            log.info(f"saved screenshot : {file_path}")
            self.driver.save_screenshot(file_path)
            log.error(e)

    @pytest.mark.regression
    def test_billing_details(self):
        billing_name_locator = (By.ID, "billing_name")
        billing_name_value = "John"
        log.info(f"{billing_name_locator}: {billing_name_value}")
        self.driver.find_element(*billing_name_locator).send_keys(billing_name_value)

        billing_phone_locator = (By.ID, "billing_phone")
        billing_phone_value = "75667546546"
        log.info(f"{billing_phone_locator} : {billing_phone_value}")
        self.driver.find_element(*billing_phone_locator).send_keys(billing_phone_value)
