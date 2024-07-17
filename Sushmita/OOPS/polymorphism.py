"""
Polymorphism : its mean one person can do multiple task
Method overriding : If two class connected with inheritance and have same method name in each class
                    then child method will override parent class method.
Method overloading : If one class have two method with same name, but different behavior
                     then it is known as method overloading, but Python does not support the method overload.
                     if defined same name method in python, then latest defined method will be considered.
"""

class father:

    def __init__(self,fname,fbusiness,fhouse):
        self.fname=fname
        self.fbusiness=fbusiness
        self.fhouse=fhouse

    def show_fname(self):
        print('father nmae is:',self.fname)

    def show_fbusiness(self):
        print(f'business name : {self.fbusiness}')

    def show_fhouse(self):
        print('father house name:',self.fhouse)

    def gretting(self):
        print("Father class method")
        print("good morning")

class child(father):

    def __init__(self,child_name,fname,fbusiness,fhouse):
        super().__init__(fname,fbusiness,fhouse)
        self.child_name=child_name

    def show_cname(self):
        print('child name is :',self.child_name)


    def gretting(self):
        print("child class method")
        print("Good evening")

if __name__ == '__main__':
    obj=child('arun','ravi','dooc','villa')
    obj.gretting()

# operator overloading

num1=10
num2=20

print("addition:",num1+num2)
print("addition:",num1.__add__(num2))

List1=[2,3,4,5]
list2=[1,1,1,1]
print('addition of list:',List1.__add__(list2))
