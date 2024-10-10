class father:
    def __init__(self,fname,fbusiness,fhouse):
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse

    def show_fname(self):
        print(f'faather name is {self.fname}')

    def show_fbusiness(self):
        print(f'father business is {self.fbusiness}')

    def show_fhouse(self):
        print(f'father having {self.fhouse}')

class mother:
    def __init__(self,m_name,m_business):
        self.mname=m_name
        self.mbusiness=m_business


    def show_mother_name(self):
        print(f'mother name is {self.mname} ')

    def show_mother_business(self):
        print(f'mother business is {self.mbusiness}')

class chlid(mother,father):
    def __init__(self, cname, m_name, m_business,fname,fbusiness,fhouse):
        super().__init__(m_name, m_business)
        self.c_name=cname
        self.obj1=father(fname,fbusiness,fhouse)

    def show_chlid_name(self):
        print(f'chlid name is {self.c_name}')

    def show_family_details(self):
        self.show_chlid_name()
        self.obj1.show_fname()
        self.show_mother_name()
        self.obj1.show_fbusiness()
        self.show_mother_business()
        self.obj1.show_fhouse()

obj=chlid("kasim","Subbamma","home maker","subbaiah","Dhobi","own house")
obj.show_chlid_name()
obj.obj1.show_fhouse()

obj.show_mother_name()
obj.show_family_details()