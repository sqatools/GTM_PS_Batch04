from selenium.webdriver.common.by import By

class TestBooking3_1:
    def test_hotel_booking(self):
        self.driver.find_element(By.ID, "fromcity").send_keys("Mumbai")



