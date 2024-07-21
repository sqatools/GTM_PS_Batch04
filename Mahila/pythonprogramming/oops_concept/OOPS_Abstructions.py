"""
Abstruction : when we hide the detail information of the product and provide the required details to the user
instead of providing internal structure details is known as abstruction.

"""

class Animal:    #Abstract class
    def animal_voice(self):
        pass

    def animal_breed(self):
        pass

    def animal_age(self):
        pass

class Dog(Animal):                #normal class implementing the abstruct class

    def animal_voice(self):
        print("bark")

    def animal_breed(self):
        print("husky")

    def animal_age(self):
        print("5 years old")

class Lion(Animal):

    def animal_voice(self):
        print("Roar")

    def animal_breed(self):
        print("African")

    def animal_age(self):
        print("10 years")

#data hiding is a particular class is hiden, but here the entire impelemtation is hided.