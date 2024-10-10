"""
multilevel inheritance : If we have three class A, B, C, then B class can access the property of class
A and class C can access the property of class A and B.
Class A -> CLass B -> Class C
"""

class grand_father:

    def __init__(self,gf_name,gf_property):
        self.gf_name=gf_name
        self.gf_property=gf_property

    def show_gf_name(self):
        print('grand father name:',self.gf_name)

    def show_gf_property(self):
        print('GF property:',self.gf_property)

class father(grand_father):

    def __init__(self,fname,fbusiness,fhouse,gf_name,gf_property):
      super().__init__(gf_name,gf_property)
      self.fname=fname
      self.fbusiness=fbusiness
      self.fhouse=fhouse

    def show_fname(self):
        print('father nmae is:',self.fname)

    def show_fbusiness(self):
        print(f'business name : {self.fbusiness}')

    def show_fhouse(self):
        print('father house name:',self.fhouse)

class child(father):

    def __init__(self,child_name,fname,fbusiness,fhouse,gf_name,gf_property):
        super().__init__(fname,fbusiness,fhouse,gf_name,gf_property)
        self.child_name=child_name

    def show_cname(self):
        print('child name is :',self.child_name)

    def show_family_details(self):
        self.show_gf_name()
        self.show_gf_property()
        self.show_cname()
        self.show_fname()
        self.show_fhouse()
        self.show_fbusiness()

if __name__ == '__main__':
    obj = child('Mohit', 'Mr.Mohan', 'Construction', 'Villa', 'Mr.Dayaram', '200 Acr')
    obj.show_family_details()
