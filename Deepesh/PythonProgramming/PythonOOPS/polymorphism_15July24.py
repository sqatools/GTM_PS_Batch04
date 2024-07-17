"""
Polymorphism : its mean one person can do multiple task
Method overriding : If two class connected with inheritance and have same method name in each class
                    then child method will override parent class method.
Method overloading : If one class have two method with same name, but different behavior
                     then it is known as method overloading, but Python does not support the method overload.
                     if defined same name method in python, then latest defined method will be considered.
"""


class father:
    def __init__(self, fname, fbusiness, fhouse):
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse

    def show_father_name(self):
        print(f"Father name is : {self.fname}")

    def show_father_business(self):
        print(f"Father is doing bussiness in : {self.fbusiness}")

    def show_father_house(self):
        print(f"Father own a house : {self.fhouse}")

    def greeting(self):
        print("father class method")
        print("Good morning")

class child(father):

    def __init__(self, child_name, fname, fbusiness, fhouse):
        super().__init__(fname, fbusiness, fhouse)
        self.child_name = child_name

    def show_son_name(self):
        print(f"The son name is : {self.child_name}")

    def show_son_name(self, son_name: str):
        print(f"The child name is : {son_name}")


    def show_family_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_house()
        self.show_son_name()

    def greeting(self):
        print("child class method")
        print("Good evening")


if __name__ == '__main__':
    obj = child('Mohit', 'Mr.Mohan', 'Construction', 'Villa')
    obj.greeting()
   #obj.show_son_name(123)


# operator overloading

num1 = 40
num2 = 50

# + operator is overloaded with __add__ method.
print("addition :", num1+num2)
print("addition :", num1.__add__(num1))

list1 = [4, 6, 8]
list2 = [3, 7, 81]
print("addition of list :", list1.__add__(list2))
print("str methods :", dir(str))

# * operator is overloaded by __mul__method
print("multiplication :", num1.__mul__(num2))
