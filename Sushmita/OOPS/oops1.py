class car:

    car_country ='India'

    def __init__(self,car_name,car_price,car_comp):
         self.car_name=car_name
         self.car_price=car_price
         self.car_comp=car_comp


    def show_car_name(self):
        print('car name is:',self.car_name)

    def show_car_price(self):
        print('car price is:',self.car_price)

    def show_car_comp(self):
        print('car company is:',self.car_comp)

    def show_car_country(cls):
        print('car country is:',cls.car_country)

    def show_car_milage(milage):
        print('car milage is:',milage)

    def show_car_details(self):
        self.show_car_name()
        self.show_car_price()
        self.show_car_comp()
        self.show_car_country()
        car.show_car_milage("30km/h")


if __name__ =='__main__' :
   obj=car(car_name='Xuv',car_price='30lac',car_comp='mahindra')
   obj.show_car_details()
   print(obj.__module__)
