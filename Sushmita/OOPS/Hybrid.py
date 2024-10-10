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
    def show1_details(self):
        self.show_fname()
        self.show_fbusiness()
        self.show_bname()
        self.show_businessname()

class sister(father):
    def __init__(self, sname, fname, fbusiness):
        super().__init__(fname, fbusiness)
        self.sname = sname

    def show_sname(self):
        print(f"sister name is: {self.sname}")

    def show2_details(self):
        self.show_fname()
        self.show_fbusiness()
        self.show_sname()

class mother(brother):

    def __init__(self, mname, bname, Bbusiness, sname, fname, fbusiness ):
        super().__init__(bname, Bbusiness,fname, fbusiness)
        self.mname = mname
        self.sobj = sister(sname,fname, fbusiness)

    def show_mname(self):
        print(f"mother name : {self.mname}")

    def show3_details(self):
        self.show_mname()
        self.sobj.show_sname()
        self.show_businessname()
        self.show_bname()
        self.show_fname()
        self.show_fbusiness()



obj1 = brother('arun', 'doctor', 'amith', 'contractor')
obj2 = sister('pooja', 'amith', 'contractor')
obj3 = mother('priya', 'arun', 'doctor', 'pooja', 'amith', 'contractor')

obj3.show3_details()
