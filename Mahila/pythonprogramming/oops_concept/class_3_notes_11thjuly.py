#access this class in other file - class 3_module import_11july,py

class car:
    car_country = "India"  # class variable

    def __init__(self, car_name, car_price, car_comp):  # parameter constructor
        self.car_name = car_name  # variable defined with self - instance variable
        self.car_price = car_price
        self.car_comp = car_comp

    def show_car_name(self):  # any method we call with self is - instance method
        print("car name is :", self.car_name)

    def show_car_price(self):
        print("car price is :", self.car_price)

    def show_car_company(self):
        print("car compnay :", self.car_comp)

    @classmethod  # use class method we neeed to use @classmethod decorator
    def show_car_country(cls):  # first parameter should be cls
        print("car country :", cls.car_country)

    @staticmethod
    def car_milege(milege):
        print("car milege: ", milege)

"""
obj = car(car_name = "XUV700",car_price = "32Lac", car_comp ="mahindra")
obj.show_car_name()
obj.show_car_price()
obj.show_car_company()
print(obj.__module__)
"""

"""
o/p:
car name is : XUV700
car price is : 32Lac
car compnay : mahindra
__main__

"""
if  __name__ == '__main__':
     obj = car(car_name = "XUV300",car_price = "20Lac", car_comp ="mahindra")
     obj.show_car_name()
     obj.show_car_price()
     obj.show_car_company()
     print(obj.__module__)

"""
car name is : XUV300
car price is : 20Lac
car compnay : mahindra
__main__

"""