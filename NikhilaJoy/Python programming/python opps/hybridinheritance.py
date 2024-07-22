#hybrid inheritance
class grandfather:
    def __init(self,gname,gbusiness):
        self.gname=gname
        self.gbusiness=gbusiness
    def show_grandfather_name(self):
        print("Grandfather name is:",self.gname)
class father(grandfather):
    def __init__(self,fname,fbusiness,fhouse,gname,gbusiness):
        super().__init__(gname,gbusiness)
        self.fname=fname
        self.fbusiness=fbusiness
        self.fhouse=fhouse
    def show_father_name(self):
        print("father name is :",self.fname)
        self.show_grandfather_name()
class mother(grandfather):
    def __init__(self,mname,moccupation,mhouse,gname,gbusiness):
        super().__init__(gname,gbusiness)
        self.mname=mname
        self.moccupation=moccupation
        self.mhouse=mhouse
    def show_mother_name(self):
        print("mother name is:",self.mname)
        self.show_grandfather_name()

fobj=father("Joy Mathew","stock market","Mathai","Farmer","Farmvilla")
m1obj=mother("Mini","Teacher","Mathai","Farmer","Farmvilla")
fobj.show_father_name()
m1obj.show_mother_name()

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
