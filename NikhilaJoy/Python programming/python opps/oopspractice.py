#1). Python oops program to create a class with the constructor.
"""
class outfit():
    def __init__(self,outfit_name,outfit_colour,outfit_price):
         self.o_n=outfit_name
         self.o_c=outfit_colour
         self.o_p=outfit_price
    def show_out_name(self):
        print("outfit name is ",self.o_n )

    def update_name(self, new_name):
        self.o_n = new_name
outf=outfit("saree","red",30)
print(outf.o_n)
outf.show_out_name()
outf.update_name("kurtha")
outf.show_out_name()
"""
#9). Python class with Single Inheritance and multilevel inheritance
"""
class grandfather:
    def __init__(self,gname,gocupation,ghouse):
        self.gname=gname
        self.gocupation=gocupation
        self.ghouse=ghouse
    def show_grandfather_name(self):
        print("Grandfather name is:",self.gname)
class father(grandfather):
    def __init__(self,fname,fbusiness,fhouse,gname,gocupation,ghouse):
        super().__init__(gname, gocupation, ghouse)
        self.fname=fname
        self.fbusiness=fbusiness
        self.fhouse=fhouse
    def show_father_name(self):
        print("father name is :",self.fname)
class child(father):
    def __init__(self,cname,cage,fname,fbusiness,fhouse,gname,gocupation,ghouse):
        super().__init__(fname,fbusiness,fhouse,gname,gocupation,ghouse)
        self.cname = cname
        self.cage = cage
    def show_child_name(self):
        print("Daughters name is:",self.cname)
    def show_family_details(self):
        self.show_grandfather_name()
        self.show_father_name()
        self.show_child_name()
        

obj=child("Nikhila Joy",26,"Joy Mathew","Stock market","Villa","Mathai","Farmer","Farmvilla")
obj.show_child_name()
obj.show_family_details()
"""

#multiple inheritance

class father:
    def __init__(self,fname,fbusiness,fhouse):
        self.fname=fname
        self.fbusiness=fbusiness
        self.fhouse=fhouse
    def show_father_name(self):
        print("father name is :",self.fname)
class mother:
    def __init__(self,mname,moccupation,mhouse):
        self.mname=mname
        self.moccupation=moccupation
        self.mhouse=mhouse
    def show_mother_name(self):
        print("mother name is:",self.mname)

class child(father,mother):
    def __init__(self,cname,cage,fname,fbusiness,fhouse,mname,moccupation,mhouse):
        super().__init__(fname,fbusiness,fhouse)
        self.cname = cname
        self.cage = cage
        self.mobj=mother(mname,moccupation,mhouse)
    def show_child_name(self):
        print("Daughters name is:",self.cname)
    def show_family_details(self):
        self.show_father_name()
        self.mobj.show_mother_name()
        self.show_child_name()


obj=child("Nikhila Joy",26,"Joy Mathew","Stock market","Villa","Mini","Teacher","villa")
#obj1=child2("Shilpa Joy",32,"Joy Mathew","Stock market","Villa")
obj.show_child_name()
obj.show_family_details()
obj.mobj.show_mother_name()
