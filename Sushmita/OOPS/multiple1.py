class father:
    def __init__(self, fnaame, fbusiness):
        self.fname = fnaame
        self.fbusiness = fbusiness

    def show_fname(self):
        print('father name:', self.fname)

    def show_fbusiness(self):
        print('father business:', self.fbusiness)


class mother:

    def __init__(self, mname, mbusiness):
        self.mname = mname
        self.mbusiness = mbusiness

    def show_m_name(self):
        print(f"mother name: {self.mname}")

    def show_m_business(self):
        print('business name:', self.mbusiness)


class child(father, mother):

    def __init__(self, cname, fname, fbusiness, mname, mbusiness):
        super().__init__(fname, fbusiness)
        self.cname = cname
        self.mobj = mother(mname, mbusiness)

    def show_cname(self):
        print('child name is:', self.cname)

    def show_family_details(self):
        self.show_cname()
        self.show_fname()
        self.show_fbusiness()
        self.show_m_name()
        self.show_m_business()


obj = child('amith', 'gouda', 'doctor', "priya", 'engineer')
obj.show_family_details()
