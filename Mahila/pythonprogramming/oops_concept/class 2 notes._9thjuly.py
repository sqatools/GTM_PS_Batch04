class car:
    def __init__(self,car_name,car_price,car_comp):  #parameter constructor
        self.car_name= car_name        #variable defined with self - instance/object variable
        self.car_price = car_price
        self.car_comp = car_comp


    def show_car_name(self):  #any method we call with self is - instance/object method
        print("car name is :", self.car_name)

    def show_car_price(self):
        print("car price is :", self.car_price)

    def show_car_company(self):
        print("car compnay :", self.car_comp)

obj = car("thar","20 lac","mahindra")
print(obj.car_name)
obj.show_car_name()
obj.show_car_price()
obj.show_car_company()

#by default every method is instance method.

#instance method - any method that we declare with self as first parameter then it is known as instance method

#class method  -
#class variable - declare in class level at top is known as class variable
#
#instance variable - declare with self

#EG::::::::::::::::::::::::::::::::::::::;;class method and class variable:::::::::::::::::::::::::::::::::::;;
class car:

    car_country = "India"   # class variable
    def __init__(self,car_name,car_price,car_comp):  #parameter constructor
        self.car_name= car_name        #variable defined with self - instance variable
        self.car_price = car_price
        self.car_comp = car_comp


    def show_car_name(self):  #any method we call with self is - instance method
        print("car name is :", self.car_name)

    def show_car_price(self):
        print("car price is :", self.car_price)

    def show_car_company(self):
        print("car compnay :", self.car_comp)

    @classmethod    #use class method we neeed to use @classmethod decorator
    def show_car_country(cls):   #first parameter should be cls
        print("car country :", cls.car_country)
print("-"*800)

obj1 = car("thar","20 lac","mahindra")
print(obj.car_name)
obj1.show_car_name()
obj1.show_car_price()
obj1.show_car_company()
obj1.show_car_country()

############STATIC METHOD##########################
#static method define with @staticmethod decorator,there is  no first parameter for static method
#static methos associated with class name, so no need to create object of class to access the static method
#we can directly call the static method with class name
#car.car_milege("20km/l")

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


print("-" * 800)
obj2= car
obj2.car_milege("20km/l")
car.car_milege("20km/l")
car.show_car_name(obj)



# when we declare static method, dont need to create obj of the class.. we can direcly access the static method with class.
#for static method only we can call with class, all other methods need obj to be declared

#self : nothing but the object of the class.
#if we want to call by class any of the instance method with the help of class name then we need to explicitly mention the obj as the parameter. self is nothing but the object of the class

print("-"*800)

#each python file is considered as python module
#every python folder which contains multiple file is considered as package
#once we place the cursor on folder- it will show folder- to convert in package we need to create a python file __init__
#- __init__ initialize the navigation inside the package

print("class name: ", obj.__class__)
print("module name :", obj.__module__) #by default module name is ""__main__"" for all the files

print("-"*800)

#update variable values of calss

print(obj.__getattribute__("car_name"))               #used to retrieve the value of a named attribute of an object

obj.__setattr__("car_name","scorpio")   #setting the value for an object attribute in python
print(obj.__getattribute__("car_name"))
obj.show_car_name()

---------------------------------------------------------------------------------------------------------------------------
#all methods of the defined class - USER DEFINED

print(dir(obj))

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
 '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 '__weakref__', 'car_comp', 'car_name', 'car_price', 'show_car_company', 'show_car_name', 'show_car_price']



