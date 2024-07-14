"""
Hybrid Inheritance
"""


class father:
    def __init__(self, fname, fbusiness):
        self.fname = fname
        self.fbusiness = fbusiness

    def show_fname(self):
        print('father name:', self.fname)

    def show_fbusiness(self):
        print('father business:', self.fbusiness)


class brother(father):

    def __init__(self, bname, Bbusiness, fname, fbusiness):
        super().__init__(fname, fbusiness)
        self.bname = bname
        self.Bbusiness = Bbusiness

    def show_bname(self):
        print(f"brother name is: {self.bname}")

    def show_businessname(self):
        print(f"bro business name: {self.Bbusiness}")


class sister(father):
    def __init__(self, sname, fname, fbusiness):
        super().__init__(fname, fbusiness)
        self.sname = sname

    def show_sname(self):
        print(f"sister name is: {self.sname}")


class mother(brother, sister):

    def __init__(self, mname, bname, Bbusiness, sname, fname, fbusiness, kwargs=None):
        super().__init__(**kwargs)
        self.mname = mname
        self.sobj = sister(sname)

    def show_mname(self):
        print(f"mother name : {self.mname}")

    def show1_details(self):
        self.show_fname()
        self.show_fbusiness()
        self.show_bname()
        self.show_businessname()

    def show2_details(self):
        self.show_fname()
        self.show_fbusiness()
        self.show_sname()

    def show3_details(self):
        self.show_mname()
        self.show_sname()
        self.show_businessname()
        self.show_bname()


obj1 = brother('arun', 'doctor', 'amith', 'contractor')
obj2 = sister('pooja', 'mahesh', 'lawyer')
obj3 = mother('priya', 'arun', 'doctor', 'pooja', 'amith', 'contractor')

#obj1.show1_details()
if __name__ == '__main__':
    obj3.show_sname()
