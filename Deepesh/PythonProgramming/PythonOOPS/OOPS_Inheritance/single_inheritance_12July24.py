"""
single inheritance : One class aquare the properties of another class, then it is single inheritance
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

class child(father):

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



# if __name__ == '__main__':
#     obj = child('Mohit', 'Mr.Mohan', 'Construction', 'Villa')
#     obj.show_son_name()
#     obj.show_family_details()

