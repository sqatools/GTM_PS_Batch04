#example 1
# class MyClass:
#      def myfun(self):
#          pass
#      def display(self,name):
#          print(name)
# mc1=MyClass()
# mc1.myfun()
# mc1.display("sangeetha")

#example2
# class MyClass:
#     def m1(self):
#         print("this is instance method")
#     @staticmethod #annotation
#     def m2(self,num):
#         print(num)
# mc=MyClass()
# mc.m1()
# mc.m2(100,200)
# MyClass.m2(10,30)

#example:3
# class MyClass:
#     a,b=10,20 #class variable
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
# mc=MyClass()
# mc.add()
# mc.mul()

#example:4
#
# i,j=15,25 #global variables
# class MyClass:
#     a,b=10,20 #class variables
#     def add(self,x,y):
#         print(x+y)  #x,y are local variables
#         print(self.a+self.b) # a,b are class variables
#         print(i+j) #i,j are global variables
# mc=MyClass()
# mc.add(100,200)

#example:5

# a,b=15,25 #global variables
# class MyClass:
#     a,b=10,20 #class variables
#     def add(self,a,b):
#         print(a+b) #local
#         print(self.a+self.b) #class
#         print(globals()['a']+globals()['b']) #global variables
# mc=MyClass()
# mc.add(100,200)

#example :6 one class can have multiple objects
# class MyClass:
#     def display(self,name):
#         print("this is display method")
#         print(name)
# obj1=MyClass()
# obj1.display("sagar")
#
# obj2=MyClass()
# obj2.display("sangeetha")

#example:7 using constructor

class Car:
    def __init__(self, car_name, car_price, car_company):
        self.car_name=car_name
        self.car_price=car_price
        self.car_company=car_company
    def show_car_name(self):
        print("car name is :", self.car_name)
    def show_car_price(self):
        print("car price is:" ,self.car_price)
    def show_car_company(self):
        print("car company name is :",self.car_company)

    def show_car_details(self):
        self.show_car_name()
        self.show_car_price()
        self.show_car_company()


obj=Car("thar","20 lac","mahindra")
obj.show_car_name()
obj.show_car_price()
obj.show_car_company()
obj.show_car_details()


#Python oops program to create a class with the constructor


class MyClass:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)

obj = MyClass("sangeetha")
obj.display_name()

#Python oops program to create a class with an instance variable.
class MyClass:
    def __init__(self):
        self.instance_var = 50
obj = MyClass()
print(obj.instance_var)

#Python oops program to create a class with Instance methods.





