"""
multiple inheritance : If one class aquire the properties of two different class or not more class
then it is known as multiple inheritance

class A -> class B
Class C -> Class B
Class B(A, C)
"""
class mother:

    def __init__(self,mname,mbusiness):
        self.mname = mname
        self.mbusiness = mbusiness

    def show_m_name(self):
        print('enter mname:',self.mname)

    def show_m_business(self):
        print('enter mbusiness:',self.mbusiness)

class father:

    def __init__(self,fname,fbusiness,fhouse):

      self.fname=fname
      self.fbusiness=fbusiness
      self.fhouse=fhouse

    def show_fname(self):
        print(f"father nmae is:'{self.fname}")

    def show_fbusiness(self):
        print(f'business name : {self.fbusiness}')

    def show_fhouse(self):
        print('father house name:',self.fhouse)

class child(mother,father):

    def __init__(self, cname, mname, mbusiness, fname, fbusiness, fhouse):

        super().__init__(mname, mbusiness)
        self.cname = cname
        self.fobj = father(fname, fbusiness, fhouse)


    def show_c_name(self):
        print(f"enter cname:' {self.cname}")

    def show_family_details(self):
        self.show_m_name()
        self.show_m_business()
        self.show_c_name()
        self.show_fname()
        self.show_fbusiness()
        self.show_fhouse()



if __name__ == '__main__':
   obj=child('sush','annapurna','housewife','ramesh','contractor','villa')
   obj.show_family_details()
