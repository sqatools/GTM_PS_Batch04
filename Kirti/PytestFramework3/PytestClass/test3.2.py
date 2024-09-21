from selenium.webdriver.common.by import By


class TestBooking3_2:
    def test_hotel_booking(self):
           self.river.find_element(By.ID, "destcity").send_keys("Kolkata")