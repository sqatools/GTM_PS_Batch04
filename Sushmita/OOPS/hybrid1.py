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


class brother(father):

    def __init__(self, ch1_name, fname, fbusiness, fhouse):
        super().__init__(fname, fbusiness, fhouse)
        self.ch1_name = ch1_name
        # self.ch2_business = ch2_business

    def child1_name(self):
        print(f"child1 name is:' {self.ch1_name}")

    # def child1_business(self):
    #      print('child1 business:', self.ch1_business)

    def show_child_details(self):
        self.show_fname()
        self.show_fbusiness()
        self.show_fhouse()
        self.child1_name()


class sister(father):

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


class mother(brother):

    def __init__(self, mname, ch1_name, ch2_name, ch2_business,fname,fbusiness, fhouse):
        super().__init__(ch1_name,fname,fbusiness, fhouse)
        self.mname = mname
        self.sobj = sister(ch2_name, ch2_business,fname,fbusiness, fhouse)

    def show_m_name(self):
        print(f"enter mname:' {self.mname}")

    def show3_details(self):
        self.show_m_name()
        self.sobj.show_child2_details()
        self.show_child_details()


obj1 = brother('arun', 'ravi', 'co', 'villa')
obj2 = sister('lavnya', 'doctor', 'ravi', 'co', 'villa')
obj3 = mother('yash', 'arun', 'lavnya', 'doctor','ravi', 'co', 'villa')

obj3.show3_details()
