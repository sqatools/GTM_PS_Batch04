"""
# Python OOPS concepts

-> class : class is nothing but the blueprint of the object is being created,
           where we defined all the properties/method/attribute and feature and functionality
           can be access by object.
-> object : object is a physical entity through which we can access all properties
          and attribute of the class.

-> method : When we defined any function in the class, then it becomes method.
            1.  class method : the method which only deals with class variable, is known as
                               class method, we declare class method with @class_method
                               decorator.
            2.  static method : static method we define with @staticmethod decorator, there is
                                first parameter for static method.
                                -> static method associated with class name, so no need to create
                                   object of class to access the static method.
                                -> We can directly call the static method with class name.

            3.  instance method : Any method that we declare with self as first parameter, then
                it is known as instance method.

-> self : self is nothing but the object of the same class is being created, self is also known instance of
          the class

-> variable : if we define any variable in the class, then it is class member variable
            -> Instance variable : when we declare any variable with self, then it
               is known as instance variable

            -> class variable : If we defined the variable on the class level, then
               the variable is known as class variable

-> constructor : Constructor which initialize the memory of the object of current class.
             -> Default constructor:
                Default constructor will be called once we initialize the object of the class.

             -> Parametrize constructor:
                Parametrize constructor include the parameter to be passed while initializing
                the object of the class

"""


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


obj = Car("Thar", "20 Lac", "Mahindra")
# print(obj.car_name)
# obj.show_car_name()
# obj.show_car_price()
# obj.show_car_company()
# obj.show_car_country()
#
# obj.show_car_milege("20km/l")

Car.show_car_milege("30km/l")
Car.show_car_name(obj)

obj.show_car_company()
print("_"*50)
obj.show_car_details()

print("_"*60)
# class name

print("class name :",  obj.__class__)
print("module name :", obj.__module__)

print("_"*60)
# update variable values of the class
print(obj.__getattribute__("car_name"))

obj.__setattr__("car_name", "Scorpio")
print(obj.__getattribute__("car_name"))
obj.show_car_name() # Scorpio

# all method of the class
print(dir(obj))

"""
'car_company', 'car_country', 'car_name', 
'car_price', 'show_car_company', 'show_car_country', 
'show_car_details', 'show_car_milege', 'show_car_name', 
'show_car_price'
"""

str1 = "Hello"
str1.upper()
