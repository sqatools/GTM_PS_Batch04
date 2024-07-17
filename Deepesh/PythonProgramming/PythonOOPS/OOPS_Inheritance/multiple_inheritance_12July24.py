"""
multiple inheritance : If one class aquire the properties of two different class or not more class
then it is known as multiple inheritance

class A -> class B
Class C -> Class B
Class B(A, C)
"""


class Mother:
    def __init__(self, m_name, m_business):
        self.m_name = m_name
        self.m_business = m_business

    def show_mother_name(self):
        print(f"The mother name is : {self.m_name}")

    def show_mother_business(self):
        print(f"The mother is doing :{self.m_business}")

class father:
    def __init__(self, fname, fbusiness, fhouse):
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse

    def show_father_name(self):
        print(f"Father name is : {self.fname}")

    def show_father_business(self):
        print(f"Father is doing bussiness in : {self.fbusiness}")

    def show_father_house(self):
        print(f"Father own a house : {self.fhouse}")

# MRO : Method Resolution Order
# which ever will define first in inheritance, then that class methods will get priority
# to access the constructor with super keyword.
class child(Mother, father):

    def __init__(self, child_name, m_name, m_business, fname, fbusiness, fhouse):
        super().__init__(m_name, m_business)
        self.child_name = child_name
        self.fobj = father(fname, fbusiness, fhouse)

    def show_son_name(self):
        print(f"The son name is : {self.child_name}")

    def show_family_details(self):
        self.fobj.show_father_name()
        self.fobj.show_father_business()
        self.fobj.show_father_house()
        self.show_mother_name()
        self.show_mother_business()
        self.show_son_name()

if __name__ == '__main__':
    obj = child('Mohit', 'Mrs.Pooja', 'Fashion Business', 'Mr.Mohan', 'Construction', 'Villa')
    obj.show_son_name()
    print("_"*40)
    obj.show_family_details()
