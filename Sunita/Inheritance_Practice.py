#Hierarchial Inheritance


class child:

    def __init__(self,child_name):
        self.child_name=child_name

    def show_child_name(self):
        print(f"Child name : {self.child_name}")

class Father(child):

    def __init__(self,fname,child_name):
        super().__init__(child_name)
        self.fname=fname

    def show_father_name(self):
        print(f"Father name is : {self.fname}")

    def show_father_child_details(self):
        self.show_father_name()
        self.show_child_name()

class Mother(child):

    def __init__(self,mname,child_name):
        super().__init__(child_name)
        self.mname=mname

    def show_Mother_name(self):
        print(f"Mother name is : {self.mname}")

    def show_Mother_child_details(self):
        self.show_Mother_name()
        self.show_child_name()

if __name__=='__main__':
    obj1=Father('Mohan','Yuvan')
    obj1.show_father_child_details()
    obj2=Mother('Rita','Yuvan')
    obj2.show_Mother_child_details()


####Hybrid Inheritance

class child:

    def __init__(self,child_name):
        self.child_name=child_name

    def show_child_name(self):
        print(f"Child name : {self.child_name}")

class Father(child):

    def __init__(self,fname,child_name):
        super().__init__(child_name)
        self.fname=fname

    def show_father_name(self):
        print(f"Father name is : {self.fname}")

    def show_father_child_details(self):
        self.show_father_name()
        self.show_child_name()

class Mother(child):

    def __init__(self,mname,child_name):
        super().__init__(child_name)
        self.mname=mname

    def show_Mother_name(self):
        print(f"Mother name is : {self.mname}")

    def show_Mother_child_details(self):
        self.show_Mother_name()
        self.show_child_name()

class Grandfather(Mother,Father):

    def __init__(self,Gname,mname,fname):
        super().__init__(mname)
        self.Gname=Gname
        self.fobj=Father(fname)

    def Grandfather_name(self):
        print(f"Grandfather name : {self.Gname}")

    def Grandfather_Family_details(self):
        self.Grandfather_name()
        self.show_Mother_child_details()
        self.show_father_child_details()

if __name__=='__main__':
    obj=Grandfather('Dayanand','Rita','Mohan')
    obj.Grandfather_Family_details()
    obj.show_father_child_details()
    obj.show_Mother_child_details()









