"""
Data hiding can be achieved with the help of data name prefix with single underscore (_) and double
under score (__).

-> when we define any variable/method with single or double underscore as prefix, those
   will not show in suggestion.

-> If we defined any method or variable with single under as prefix then those method/.variable
   will not show in suggestion list, but we can directly with class obj.

"""

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
    obj = school("2 Lac/Year", "8AM-4PM", "2 rank")
    obj._show_address_time()
    # obj._classname__method/variable
    obj._school__show_city_rank()
    print(dir(obj))
