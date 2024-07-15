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





if __name__=="__main__":
    obj=car("x7",2565445,"BMW")
    car.show_carname(obj)
    car.show_car_millege("45kml")
    obj.show_car_country()
    print(obj.__module__)




