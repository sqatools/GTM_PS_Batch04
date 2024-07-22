class father:
    def __init__(self,fname,fbusiness):
        self.fname=fname
        self.fbusiness=fbusiness
    def show_father_name(self):
        print("father name is:",self.fname)
class child1(father):
    def __init__(self,c1name,fname,fbusiness):
        super().__init__(fname, fbusiness)
        self.c1name=c1name
    def show_child1_name(self):
        print("child1 name is:",self.c1name)
        print("father name is:", self.fname)
class child2(father):
    def __init__(self,c2name,fname,fbusiness):
        super().__init__(fname,fbusiness)
        self.c2name=c2name
    def show_child2_name(self):
        print("child2 name is:",self.c2name)
        print("father name is:",self.fname)
obj1=child1("shilpa","Joy Mathew","Manager")
obj2=child2("Nikhila","Joy Mathew","Manager")
obj1.show_child1_name()
obj1.show_father_name()
obj2.show_child2_name()
obj2.show_father_name()