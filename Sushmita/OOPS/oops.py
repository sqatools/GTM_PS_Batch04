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

class car: #class name
    car_country='India'   #class variable

    def __init__(self,car_name,car_price,car_comp):  #constructor
        self.car_name=car_name   #instance variable
        self.car_price=car_price
        self.car_comp=car_comp


    def show_car_name(self): #instance method
        print('car name is:',self.car_name)


    def show_car_price(self):
        print('car price is:',self.car_price)

    def show_car_comp(self):
        print('car company is:',self.car_comp)

    def show_car_country(cls): #class method
        print('car country:',cls.car_country)

    def show_car_milage(milage): #static method
        print('car milage is :',milage)

    def show_details(self):
        self.show_car_name()
        self.show_car_price()
        self.show_car_comp()
        self.show_car_country()
        car.show_car_milage("30km/l")

obj = car("Thar", "20 Lac", "Mahindra")  #object
# obj.show_car_name()
# obj.show_car_price()
# obj.show_car_comp()
# obj.show_car_country()
# car.show_car_milage("20km/l")


obj.show_car_comp()
print("_"*50)
obj.show_details()

print("class name :",  obj.__class__)
print("module name :", obj.__module__)

print("_"*60)
# update variable values of the class
print(obj.__getattribute__("car_name"))

obj.__setattr__("car_name", "Scorpio")
print(obj.__getattribute__("car_name"))
obj.show_car_name()

#print(dir(obj))

print('-'*50)

obj.show_details()
