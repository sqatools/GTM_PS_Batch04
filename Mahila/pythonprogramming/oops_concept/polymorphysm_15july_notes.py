"""
polymorphism : it means one person can do multiple task.
2 concepts : method overriding - if 2 class connected with inheritence and have same method name in each clss
                 then child class method will override the parent class method.
           : method overloading -> if 2 method in same class with same name with different behaviour is known as method overloading.
                                   python doesnot allow. Available in java. if we define same name method in python then the latest defined method will be considered.
           :operator overloading(not related to oops)
when we have 2 class, both inheritence and both have same name.
in below example we have 2 class both are having same method, so the child class method will override the parent class
#method- that concept is called overriding
"""
class father:   #superclass
    def __init__(self,fname,fbusiness,fhouse):   #constructor
        self.fname = fname                       #instamce variable
        self.fbusiness = fbusiness
        self.fhouse = fhouse
    def show_father_name(self):               #instance method
        print(f"Father  name is :{self.fname}")

    def show_father_business(self):
        print(f"Father business is :{self.fbusiness}")

    def show_father_house(self):
        print(f"Father house is :{self.fhouse}")

    def greeting(self):
        print("father class method")
        print("good morning")
#child class
class child(father):   #inside child class we need to initiate the constructor of the parent class as well.
#double click on the __init__ and click on bulb like symbol at left click add superclass call, automatically all the parent class will replicate in child class as well.
    def __init__(self, child_name, fname, fbusiness, fhouse):
        super().__init__(fname, fbusiness, fhouse)
        self.child_name = child_name

    def show_son_name(self):
        print(f"The son name is : {self.child_name}")

    def show_family_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_house()
        self.show_son_name()

    def greeting(self):
        print("Child class method")
        print("Good evening")

if __name__ == '__main__':
    obj=child('mohit','mohan','construction','villa')
    obj.greeting()     #Child class method
                       #Good evening
 #which ever obj we create the method will get priority
print("-"*800)
#####################OPERATOR OVERLOADING####################
#add method in list, string, int - behind the operator there is a magic method running in background.

# the plus operator overloaded with  __add__  method.
num1 = 40
num2 = 50

print("addition :" , num1+num2)
print("addition : ", num1.__add__(num2))

list_1 = [4,6,8]
list_2 = [2,4,5]
print("addition of list :", list_1.__add__(list_2))
print("str method : ", dir(str))

print("multiplication :", num1.__mul__(num2))

