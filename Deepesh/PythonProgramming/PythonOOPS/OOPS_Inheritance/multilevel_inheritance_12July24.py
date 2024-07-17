"""
multilevel inheritance : If we have three class A, B, C, then B class can access the property of class
A and class C can access the property of class A and B.
Class A -> CLass B -> Class C
"""


class GrandFather:
    def __init__(self, gf_name, gf_property):
        self.gf_name = gf_name
        self.gf_property = gf_property

    def show_grandfather_name(self):
        print(f"Grandfather name is : {self.gf_name}")

    def show_grandfather_property(self):
        print(f"GrandFather Owns Property: {self.gf_property}")


class father(GrandFather):
    def __init__(self, fname, fbusiness, fhouse, gf_name, gf_property):
        super().__init__(gf_name, gf_property)
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse

    def show_father_name(self):
        print(f"Father name is : {self.fname}")

    def show_father_business(self):
        print(f"Father is doing bussiness in : {self.fbusiness}")

    def show_father_house(self):
        print(f"Father own a house : {self.fhouse}")


class child(father):

    def __init__(self, child_name, fname, fbusiness, fhouse, gf_name, gf_property):
        super().__init__(fname, fbusiness, fhouse, gf_name, gf_property)
        self.child_name = child_name

    def show_son_name(self):
        print(f"The son name is : {self.child_name}")

    def show_family_details(self):
        self.show_grandfather_name()
        self.show_grandfather_property()
        self.show_father_name()
        self.show_father_business()
        self.show_father_house()
        self.show_son_name()

if __name__ == '__main__':
    obj = child('Mohit', 'Mr.Mohan', 'Construction', 'Villa', 'Mr.Dayaram', '200 Acr')
    obj.show_son_name()
    obj.show_grandfather_property()
    print("_"*40)
    obj.show_family_details()
