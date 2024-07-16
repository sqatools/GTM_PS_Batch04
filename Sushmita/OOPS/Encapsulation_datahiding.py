"""
Data hiding can be achieved with the help of data name prefix with single underscore (_) and double
under score (__).

-> when we define any variable/method with single or double underscore as prefix, those
   will not show in suggestion.

-> If we defined any method or variable with single under as prefix then those method/.variable
   will not show in suggestion list, but we can directly with class obj.

"""


class school:
    name = 'AGS school'
    _city = 'Raichur'
    __adress = 'Lingasugur'

    def __init__(self, school_fee, school_time, school_rank):
        self.school_fee = school_fee
        self._school_time = school_time
        self.__school_rank = school_rank

    def show_School_name_fee(self):
        print("school name:,", self.name)
        print("school fee:", self.school_fee)

    def _show_school_city_time(self):
        print("school city:,", self._city)
        print("school time:", self._school_time)

    def __show_school_adress_rank(self):
        print('school adress:', self.__adress)
        print('school rank:', self.__school_rank)


#print('adress:', __adress)
obj = school('10l', '8AM-4PM', '3rd')
obj._show_school_city_time()
# obj._classname__method/variable
# obj._school__show_school_adress_rank()
obj._school__show_school_adress_rank()
obj._school__adress
