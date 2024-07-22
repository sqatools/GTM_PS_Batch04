"""
SINGLE INHERETENCE- if one class aquire the properties of another class then it is single inheretence.


"""

class father:   #superclass
    def __init__(self,fname,fbusiness,fhouse):
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse
    def show_father_name(self):
        print(f"Father  name is :{self.fname}")

    def show_father_business(self):
        print(f"Father business is :{self.fbusiness}")

    def show_father_house(self):
        print(f"Father house is :{self.fhouse}")
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

if __name__ == '__main__':
    obj=child('mohit','mohan','construction','villa')
    obj.show_son_name()
    obj.show_family_details()

