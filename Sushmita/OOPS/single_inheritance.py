"""
single inheritance : One class aquare the properties of another class, then it is single inheritance
"""

class father:

    def __init__(self,fname,fbusiness,fhouse):
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

    def __init__(self,child_name,fname,fbusiness,fhouse):
        super().__init__(fname,fbusiness,fhouse)
        self.child_name=child_name

    def show_cname(self):
        print('child name is :',self.child_name)

    def show_family_details(self):
        self.show_cname()
        self.show_fname()
        self.show_fhouse()
        self.show_fbusiness()

obj=child('eshwar','ramesh','contractor','villa')
obj.show_family_details()
