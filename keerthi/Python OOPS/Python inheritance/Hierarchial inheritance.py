class father:
    def __init__(self, fname = None, fbusiness= None
                 ,fhouse = None, fbusiness1 = None, fhouse1 = None):
        self.fname = fname
        self.fbusiness = fbusiness
        self.fbusiness1 = fbusiness1
        self.fhouse = fhouse
        self.fhouse1 = fhouse1

    def show_father_name(self):
        print(f"Father name is : {self.fname}")

    def show_father_business(self):
        print(f"Father is doing business in : {self.fbusiness}")



    def show_father_house(self):
        print(f"Father own a house : {self.fhouse}")

    def show_father_business1(self):
        print(f"Father is doing business in : {self.fbusiness1}")

    def show_father_house1(self):
        print(f"Father own a house : {self.fhouse1}")

class child1(father):

    def __init__(self, child1_name, fname, fbusiness, fhouse):
        super().__init__(fname, fbusiness, fhouse,)
        self.child1_name = child1_name

    def show_son_name(self):
        print(f"The son name is : {self.child1_name}")

    def show_family_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_house()
        # self.show_son_name()


class child2(father):

    def __init__(self, child2_name, fname, fbusiness1, fhouse1):
        super().__init__(fname, fbusiness1, fhouse1)
        self.child2_name = child2_name

    def show_daughter_name(self):
        print(f"The daughter name is : {self.child2_name}")


    def show_family_details1(self):
        self.show_father_name()
        self.show_father_business1()
        self.show_father_house1()
        # self.show_daughter_name()


if __name__ == '__main__':
    obj = child1(child1_name='Mohit', fname='Mr.Mohan', fbusiness='Construction',  fhouse='villa')
    obj.show_son_name()
    obj.show_family_details()
    print()
    obj1 = child2(child2_name='priya', fname='Mr.Mohan', fbusiness1='Architect', fhouse1='flat' )
    obj1.show_daughter_name()
    obj1.show_family_details1()


