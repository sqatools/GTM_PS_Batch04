# class father:
#     def __init__(self,fname,fproperty,fsupport):
#         self.fname=fname
#         self.fproperty=fproperty
#         self.fsupport=fsupport
#
#     def show_father_name(self):
#         print(f'father name is {self.fname}')
#
#     def show_father_property(self):
#         print(f'father property {self.fproperty}')
#
#     def show_father_support(self):
#         print(f"father support {self.fsupport}")
#
#
# class son(father):
#     def __init__(self, son_name, fname, fproperty, fsupport):
#         super().__init__(fname, fproperty, fsupport)
#
#         self.sname=son_name
#
#     def show_son_name(self):
#         print(f'son name is {self.sname}')
#
#     def show_son_father(self):
#         self.show_son_name()
#         self.show_father_name()
#         self.show_father_property()
#         self.show_father_support()
#
# class daughter(father):
#     def __init__(self, dname, fname, fproperty, fsupport):
#         super().__init__(fname, fproperty, fsupport)
#         self.dname=dname
#
#     def show_daughter_name(self):
#         print(f'daughter name is {self.dname}')
#
#     def show_daughter_father(self):
#         self.show_daughter_name()
#         self.show_father_name()
#         self.show_father_property()
#         self.show_father_support()


# obj=son("Ram","jayaram","100 arc","yes")
# obj2=daughter("radha","jayaram","100 arc","no")
# obj.show_son_father()
# print("_"*100)
# obj2.show_daughter_father()

class grandfather:
    def __init__(self,gfname,gfproperty):
        self.gfname=gfname
        self.gfproperty=gfproperty

    def show_grandfather_name(self):
        print(f'grandfather name is {self.gfname}')

    def show_grandfather_property(self):
        print(f'grandfather property {self.gfproperty}')




class father(grandfather):
    def __init__(self, f_name,f_business, gfname, gfproperty):
        super().__init__(gfname, gfproperty)
        self.fname=f_name
        self.fbusiness=f_business

    def show_father_name(self):
        print(f'father name is {self.fname}')

    def show_father_business(self):
        print(f'father business is {self.fbusiness}')

    # def show_father_grandfather(self):
    #     self.show_father_name()
    #     self.show_grandfather_name()
    #     self.show_grandfather_property()
    #     self.show_father_business()

class daughterinlaw(grandfather):
    def __init__(self, dname,dbusiness, gfname, gfproperty):
        super().__init__(gfname, gfproperty)
        self.dname=dname
        self.dbusiness=dbusiness

    def show_dil_name(self):
        print(f'DIL name is {self.dname}')

    def show_dil_business(self):
        print(f"DIl business is {self.dbusiness}")

    # def show_daughter_father(self):
    #     self.show_dil_name()
    #     self.show_dil_business()
    #     self.show_grandfather_name()
    #     self.show_grandfather_property()
class grandson(father):
    def __init__(self, son_name, f_name, f_business, gfname, gfproperty, dname, dbusiness):
        super().__init__(f_name, f_business, gfname, gfproperty)
        self.sname=son_name
        self.dobj=daughterinlaw(dname,dbusiness, gfname, gfproperty)

    def show_grand_son_name(self):
        print(f'grandson name is {self.sname}')

    def complete_famliy_details(self):
        self.show_grand_son_name()
        self.show_grandfather_name()
        self.show_grandfather_property()
        self.show_father_name()
        self.show_father_business()
        self.dobj.show_dil_name()
        self.dobj.show_dil_business()

obj=grandson("Kumar","Mohan","contractor","muthu kumar","10 arc","priya","own shop")
obj.complete_famliy_details()
