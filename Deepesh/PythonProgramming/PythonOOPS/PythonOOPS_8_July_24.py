"""
# Python OOPS concepts

-> class : class is nothing but the blueprint of the object is being created,
           where we defined all the properties/method/attribute and feature and functionality
           can be access by object.
-> object : object is a physical entity through which we can access all properties
          and attribute of the class.

-> method : When we defined any function in the class, then it becomes method.
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


class ABC:

    country = "India"  # class variable

    # # constructor
    # def __init__(self, x, y):
    #     print("Initializing the memory of object")
    #     self.x_var = x  # Instance variable
    #     self.y_var = y  # Instance variable
    #     self.greeting()

    # method/ instance method
    def greeting(self):
        print("Good Morning")

    # method/ instance method
    def addition(self, num1, num2):
        print("addition :", num1 + num2)

    # instance method
    def multiplication(self):
        print("multiplication of instance var value :", self.x_var*self.y_var)

    # constructor
    def __init__(self, x, y):
        print("Initializing the memory of object")
        self.x_var = x  # Instance variable
        self.y_var = y  # Instance variable
        self.greeting()

'''
obj = ABC()
obj.greeting()

print("_"*50)
obj1 = ABC()
obj1.greeting()

print("_"*50)
obj2 = ABC()
obj2.greeting()
obj2.addition(50, 60)
'''


print("_"*50)
var1 = int(input("please enter value for var1 :"))
var2 = int(input("please enter value for var2 :"))
#obj_a = ABC(7, 8)
obj_a = ABC(var1, var2)
obj_a.greeting()
obj_a.addition(50, 20)
obj_a.multiplication()
