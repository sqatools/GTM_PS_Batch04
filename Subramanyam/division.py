# a = 40
# b =  50
# c = 30
#
# print("Average = ",(a+b+c)/3)
#
# # square and cube
#
# print("square of 9: ", 9**2)
# print("cube of 9: ", 9**3)
#
# # data inchange
#
# a =3
# b = 6
#
# a=b
# b=a
# print(a)
# print(b)
#
#
# x = 8
# y = 9
# x,y =y,x
# print("X value is :",x)
# print("Y value is :",y)
#
# # Pythagorous theorem
#
# a1 =4
# b1 =6
# c1 = a1**2+b1**2
#
# LHS=c1**2
# RHS = a1**2+b1**2
# print(LHS)
# print(RHS)
# print(c1)
#
# # middle number in list
#
# L = [45, 60, 61, 66, 70, 77, 80]
# lst = (len(L))/2
# print("median",L[int(lst)])
#
# # (a+b)2=a2+b2+2ab
#
# a2=5
# b2=3
#
# lhs = (a2+b2)**2
# rhs= a2**2+b2**2+2*a2*b2
#
# print(lhs)
# print(rhs)
#
# print("*"* 50)
#
# # (a-b)2=a2+b2-2ab
#
# a3=5
# b3=3
#
# lhs1 = (a3-b3)**2
# rhs2= a3**2+b3**2-2*a3*b3
#
# print(lhs1)
# print(rhs2)
#
#
# print("_"*100)
#
# for i in range(1500,2701):
#         if i%7 == 0 and i%5 == 0:
#             print(i, end=" ")

class school:
    name = "Emrald heights schools"
    _address = "Pune, Hinjewadi"
    __city = "Pune"

    def __init__(self, school_fee, school_time, school_rank):
        self.school_fee = school_fee
        self._school_time = school_time
        self.__school_rank = school_rank

    def show_school_name_and_fee(self):
        print("school name is :", self.name)
        print("school fee is :", self.school_fee)

    def _show_address_time(self):
        print("school address :", self._address)
        print("school time :", self._school_time)

    def __show_city_rank(self):
        print("school city name is :", self.__city)
        print("school rank is :", self.__school_rank)


if __name__ == '__main__':
    obj = school(1565,"8-9","5")
    obj.show_school_name_and_fee()
    obj._show_address_time()
    obj._school__show_city_rank()
