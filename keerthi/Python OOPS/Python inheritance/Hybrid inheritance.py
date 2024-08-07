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

class childA(father):

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

class childB(father):

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


class childC(father):

    def __init__(self, child_name, fname, fbusiness, fhouse):
        super().__init__(fname, fbusiness, fhouse)
        self.child_name = child_name

    def show_son_name(self):
        print(f"The son name is : {self.child_name}")


    def show_family_details(self):
        self.show_father_name()
        self.show_son_name()
        self.show_father_business()
        self.show_father_house()


if __name__ == '__main__':
    obj = childA('Mohit', 'Mr.Mohan', 'Construction', 'Villa')
    # obj.show_son_name()
    obj.show_family_details()

    print()

    obj = childB('kalyan', 'Mr.Mohan', 'Architect', 'Villa')
    # obj.show_son_name()
    obj.show_family_details()

    print()

    obj = childC('Raju', 'Mr.Mohan', 'Manufacturer', 'Villa')
    # obj.show_son_name()
    obj.show_family_details()