class ABC:
    country="India"
    def __init__(self,x,y):
        print("initial memory")
        self.x=x
        self.y=y
        self.greeting()
    def greeting(self):
        print("good morning")

    def addition(self,num1,num2):
        print("addition: ",num1+num2)

    def multiplication(self):
        print("multiplication of instance var value:",self.x*self.y)


# obj=ABC(70,80)
# obj.greeting()
# obj.addition(5,4)
# obj.multiplication()


class car():
    car_country="India"

    def __init__(self,car_name,car_price,car_comp):
        self.car_name=car_name
        self.car_price=car_price
        self.car_comp=car_comp

    def show_carname(self):
        print("car name is : ",self.car_name)

    def show_carprice(self):
        print("car price is: ",self.car_price)

    def show_carcomp(self):
        print("car company is: ",self.car_comp)

    def car_details(self):
        self.show_carname()
        self.show_carprice()
        self.show_carcomp()
        self.show_car_country()
        self.show_car_millege("60kml")

    @classmethod
    def show_car_country(cls):
        print("car country name is: ",cls.car_country)

    @staticmethod
    def show_car_millege(millege):
        print("car millege is: ",millege)





obj=car("x7",2565445,"BMW")
# obj.show_carcomp()
# obj.show_carprice()
# obj.show_carname()
# obj.show_car_country()
# obj.show_car_millege("45kml")
# print("_"*100)
# obj.car_details()

car.show_carname(obj)
car.show_car_millege("45kml")
obj.show_car_country()

print("class name: ",obj.__class__)
print("module name is: ",obj.__module__)


print(obj.__getattribute__("car_name",))


obj.__setattr__("car_name","Scorpio")
print(obj.__getattribute__("car_name"))


obj.show_carname()