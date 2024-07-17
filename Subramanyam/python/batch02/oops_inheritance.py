class father:
    def __init__(self,fname,fbusiness,fhouse):
        self.fathername=fname
        self.fatherbusiness=fbusiness
        self.fatherhouse=fhouse

    def show_father_name(self):
        print("father name is: ",self.fathername)

    def show_father_business(self):
        print("father businees is: ",self.fatherbusiness)

    def show_father_house(self):
        print("father house is: ",self.fatherhouse)

class chlid(father):
    def __init__(self, child_name,fname, fbusiness, fhouse):
        super().__init__(fname, fbusiness, fhouse)
        self.cname=child_name

    def show_chlid_name(self):
        print("chlid name is: ",self.cname)

    def family_details(self):
        self.show_chlid_name()
        self.show_father_house()
        self.show_father_business()
        self.show_father_name()

# obj=chlid("naveen","raju","farmer","own house")
# obj.show_father_name()
# obj.show_father_business()
