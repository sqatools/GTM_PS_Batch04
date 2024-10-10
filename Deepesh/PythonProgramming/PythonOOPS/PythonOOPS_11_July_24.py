class Car:
    car_country = "India"  # class variable

    def __init__(self, car_name, car_price, car_comp):
        self.car_name = car_name  # instance/object variable
        self.car_price = car_price
        self.car_company = car_comp

    #  # instance/object method
    def show_car_name(self):
        print("Car name is :", self.car_name)

    #  # instance/object method
    def show_car_price(self):
        print("Car price is :", self.car_price)

    #  # instance/object method
    def show_car_company(self):
        print("Car company name is :", self.car_company)

    def show_car_details(self):
        self.show_car_name()
        self.show_car_price()
        self.show_car_company()
        self.show_car_milege("30km/l")
        self.show_car_country()

    @classmethod
    def show_car_country(cls):
        print("Car country name :", cls.car_country)

    @staticmethod
    def show_car_milege(milege):
        print("Car milege is :", milege)


if __name__ == '__main__':
     obj = Car(car_name='XUV300', car_price="20 Lac", car_comp="Mahindra")
     obj.show_car_details()
     print(obj.__module__)

