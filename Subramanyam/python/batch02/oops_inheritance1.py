class grandfather:
    def __init__(self,gf_name,gf_property):
        self.gfname=gf_name
        self.gfproperty=gf_property

    def grand_father_name(self):
        print(f'grandfather name is {self.gfname}')

    def grand_father_property(self):
        print(f'grandfather is having {self.gfproperty} ')

class father(grandfather):
    def __init__(self, fname, fbusiness, fhouse, gf_name, gf_property):
        super().__init__(gf_name, gf_property)
        self.fname=fname
        self.fbusiness=fbusiness
        self.fhouse=fhouse

    def show_fname(self):
        print(f'faather name is {self.fname}')

    def show_fbusiness(self):
        print(f'father business is {self.fbusiness}')

    def show_fhouse(self):
        print(f'father having {self.fhouse}')


class chlid(father):
    def __init__(self, chlid_name, fname, fbusiness, fhouse, gf_name, gf_property):
        super().__init__(fname, fbusiness, fhouse, gf_name, gf_property)
        self.chlidname=chlid_name

    def show_chlidname(self):
        print(f'chlid name is {self.chlidname}')

    def famliy_details(self):
        self.show_fname()
        self.show_fbusiness()
        self.show_fhouse()
        self.grand_father_name()
        self.grand_father_property()
        self.show_chlidname()

obj=chlid("krishna","ramesh","Driver","Reoops_inheritance.pynted house","krishnaiah","10 cows")
obj.show_chlidname()
obj.show_fbusiness()
obj.famliy_details()