"""
Abstraction : When we hide the details information of the product and provide required details to
user instead provide internal structure details is known as abstraction.
"""

class animal:

    def animal_voice(self):
        pass

    def animal_bread(self):
        pass

    def animal_age(self):
        pass


class dog(animal):

    def animal_voice(self):
        print("Bark")

    def animal_bread(self):
        print("Husky")

    def animal_age(self):
        print("dog as is 5 years")

class Lion(animal):

    def animal_voice(self):
        print("Roar")

    def animal_bread(self):
        print("African Lion")

    def animal_age(self):
        print("Lion age is 10 years")

obj=dog()
obj.animal_voice()
obj=Lion()
obj.animal_age()
