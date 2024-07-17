"""
Abstraction : When we hide the details information of the product and provide required details to
user instead provide internal structure details is known as abstraction.
"""

from abc import abstractmethod

class Animal:
    def animal_voice(self):
        pass

    @abstractmethod
    def animal_bread(self):
        pass

    def animal_age(self):
        pass

class Dog(Animal):

    def animal_voice(self):
        print("Bark")

    def animal_bread(self):
        print("Husky")

    def animal_age(self):
        print("dog as is 5 years")

class Lion(Animal):

    def animal_voice(self):
        print("Roar")

    def animal_bread(self):
        print("African Lion")

    def animal_age(self):
        print("Lion age is 10 years")


obj = Dog()
obj.animal_voice()

obj2 = Lion()
obj2.animal_voice()
