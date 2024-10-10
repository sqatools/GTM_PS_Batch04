from selenium.webdriver.common.by import By

class TestBooking3_3:
    def test_flight_booking(self):
        self.driver.find_element(By.ID, "billing_name").send_keys("John")
        self.driver.find_element(By.ID, "billing_phone").send_keys("5646456456456")

