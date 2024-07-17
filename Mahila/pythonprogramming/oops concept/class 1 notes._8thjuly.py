"""
Object-Oriented Programming (OOP) is a programming paradigm
 that organizes code into objects, allowing developers to model
 real-world entities and their interactions.
"""
#to define class
#first we need to add class and then class name anything,inside class we can def methods.previously
# the function we declared outside will now become method.

#simple good morning.

class ABC:           #class
    def greeting(self):       #method
        print("Good morning")
#if u want to access this particular class we need to create object

obj = ABC()    #obj is nothing but a variable      #used to access the method
obj.greeting() # if u want to access method of any particular class then we have to create object of that particular class

print("-"*80)

"""
#class ---> class is nothing but the blueprint/architecture of the object is being created,where we define all the properties/methods/attribute and 
feature and functionality can be access by object.

#object ---> object is an physical entity through which we can access all the properties and attributes of the class.

#method ---> when we define any function inside the class it will become method.

#variable ---> If we define any variable in the class, then it is class member variable.

#constructor ---> is nothing but the initiator, will initiate the memory of the object.
by default for any class constructor is going to work, -->default constructor
--->WHEN EVER WE CREATE A OBJECT OF A CLASS A CONSTRUCTOR IS GOING TO INITIALIZE. compilementry with each object
__init__  --- is the inbuild object, 

2 types of constructor : constructor which initialize the memory of the object of current class.
1)default constructor - will be called once we initialize the object of the class.
2)parameters constructor - includes the parameter to be passed while initializing the object of the class



there is no use for class if the object is not created. class will not work without the object.
we can create n number of object in the same class
like obj1.greeting()
obj2.greeting()    both will print the same method #good morning

"""

class BCD:           #class
    def greeting(self):       #method
        print("Good morning")

    def addition(self,num1,num2):
        print("addition ",num1+num2)

obj=BCD()
obj.greeting()

obj1=BCD()
obj1.greeting()

obj.addition(100,200)
obj1.addition(100,200)

print("-"*800)

#constructor
#default constructor
class CDE:
    def __init__(self):     #DEFINE CONSTRUCTOR (DEFAULT CONSTRUCTOR)  #if it is not defined also it will run in background
        print("Initialize the memory of the object")
    def greeting(self):       #method
        print("Good morning")

    def addition(self,num1,num2):
        print("addition ",num1+num2)

obj=CDE()
obj.greeting()
print("-"*800)
obj1=CDE()
obj1.addition(3,4)

print("-"*8000)
#parameter constructor
#instance variable

class XYZ:
    def __init__(self,x,y):    #WE OUT THIS INSTANCE VARIABLE WE CANT USE X AND Y VALUES IN ANY OF THE METHOD
        print("initializing the memory")
        self.x_var = x    #instance variable - declare any variable with self is known as instance variable, we can use accross the class
        self.y_var = y
        self.greeting()  #method initialization
    def greeting(self):
        print("Hello world")

    def addition(self,num1,num2):    #LIMITIED TO THIS METHOD ALONE
        print("addition :", num1+num2)

    def mul(self):    ##instance method
        print("multi of instance variable :" , self.x_var*self.y_var)

obj_a = XYZ( 70, 10)   #initializing the memory
                               #Hello world
obj_a.greeting()
obj_a.mul()
#where ever we define the constructor, first constructor only will work first.
#instance means nothing but the objec tof the class.






