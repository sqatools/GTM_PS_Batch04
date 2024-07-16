#import math
#
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def calaulate_area(self):
#         return math.pi*self.radius**2
#
# circle=Circle(10)
# area=circle.calaulate_area()
# print(area)
#
# class rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#
#     def Area_rectangle(self):
#         return self.length*self.width
#
#     def perimeter_rectangle(self):
#         return 2*(self.length+self.width)
#
# Rectangle=rectangle(5,13)
# area=Rectangle.Area_rectangle()
# perimeter=Rectangle.perimeter_rectangle()
# print(area)
# print(perimeter)
#
#
# class parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show_details(self):
#         print("parent name is: ",self.name)
#         print("parent age is: ",self.age)
#
# Parent=parent("subbu",30)
# Parent.show_details()
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def print_details(self):
#         print("name: ",self.name)
#         print("Age: ",self.age)
#
# class Student(person):
#     def __init__(self, studentid, grades, name, age):
#         super().__init__(name, age)
#         self.studentid=studentid
#         self.grades=grades
#
#     def print_details(self):
#         super().print_details()
#         print("studentid",self.studentid)
#         print("grade: ",self.grades)
# student=Student(56,["A","A+"],"Raju",65)
# student.print_details()

# class Animal:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#
#     def print_details(self):
#         print("Animal name: ",self.name)
#         print("Animal color: ",self.color)
#
# class dog(Animal):
#     def __init__(self, breed, weight, name, color):
#         super().__init__(name, color)
#         self.breed=breed
#         self.weight=weight
#     def print_details(self):
#         super().print_details()
#         print("Animal breed is: ",self.breed)
#         print("Animal weight is: ",self.weight)
# Dog=dog("Streetdog",18,"racis","black")
# Dog.print_details()


class BankAccount:
    def __init__(self,acc_number,balance):
        self.acc_number=acc_number
        self.balance=balance
    def deposit(self,Amount):
        self.balance +=Amount
        print("Deposit of ",Amount,"Successful. New balance:",self.balance)

    def withdraw(self,Amount):
        if self.balance>=Amount:
            self.balance-=Amount
            print("withdraw of ", Amount, "Successful. New balance:", self.balance)
        else:
            print("Insiffcuent funds. withdrawal dinied")

Account=BankAccount("5698745213",15000)
Account.deposit(15000)
Account.withdraw(25000)