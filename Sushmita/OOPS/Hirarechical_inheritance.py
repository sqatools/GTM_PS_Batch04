"""
Hierarchical Inheritance
"""


class father:

    def __init__(self, fname, fbusiness, fhouse):
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse

    def show_fname(self):
        print('father nmae is:', self.fname)

    def show_fbusiness(self):
        print(f'business name : {self.fbusiness}')

    def show_fhouse(self):
        print('father house name:', self.fhouse)


class child1(father):

    def __init__(self, ch1_name, fname, fbusiness, fhouse):
        super().__init__(fname, fbusiness, fhouse)
        self.ch1_name = ch1_name
        # self.ch2_business = ch2_business

    def child1_name(self):
        print(f"child1 name is:' {self.ch1_name}")


# def child1_business(self):
#     print('child1 business:', self.ch1_business)


class child2(father):

    def __init__(self, ch2_name, ch2_business, fname, fbusiness, fhouse):
        super().__init__(fname, fbusiness, fhouse)
        self.ch2_name = ch2_name
        self.ch2_business = ch2_business

    def child2_name(self):
        print('child2 name is:', self.ch2_name)

    def child2_business(self):
        print('child2 business:', self.ch2_business)

    def show_child2_details(self):
        self.show_fname()
        self.show_fbusiness()
        self.show_fhouse()
        self.child2_name()
        self.child2_business()

    def show_child_details(self):
        self.show_fname()
        self.show_fbusiness()
        self.show_fhouse()
        self.child1_name()

    # self.child1_business()
    def child1_name(self):
        pass


obj1 = child2("purna", "Doctor", "ramesh", "contractor", "villa")
obj2 = child1("akash", "ramesh", "contractor", "villa")

obj1.show_child2_details()
obj2.show_fbusiness()
#obj2.show_child_details()
