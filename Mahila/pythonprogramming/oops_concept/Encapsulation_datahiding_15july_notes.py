"""
Data hiding can be achieved with the help of data name prefix with single underscore and double underscore.(__)
#when we define any variable /methods with single or double  underscores as prefix those will not show in suggestion,
until the particular person go to the code and check it.

# if we defined any method/variable with single or double underscore as prefix, those will not show in suggestion list, but we can directly access with class object.

data hiding - we want to combine all the variables and method to avoiding accessing outside the class
#Python just show the intention I am not allowing to access it, but if u need access it  - data hiding
#used when we need to hide any method/variable
"""

class school:
    name = "Emrald heights school"  #class variable
    _address ="pune, Hinjewadi"
    __city =  "pune"

    def __init__(self,school_fee,schools_time, school_rank):   #define constructor
        self.school_fee = school_fee     #instance variable
        self._school_time = schools_time   #instanc evariable defined with underscore
        self.__school_rank = school_rank

    def show_school_name_and_fee(self):
        print("school name is :", self.name)
        print("School fee is : ", self.school_fee)

    def _show_address_and_time(self):
        print("school time :" , self._school_time)
        print("school address :" , self._address)

    def __show_city_rank(self):
        print("School city name is :", self.__school_rank)
        print("school rank is :", self.__school_rank)

if __name__ == '__main__' :
    obj = school("2 Lac/year","8AM-4PM","2ND RANK")
#when we define any variable /method with single or double  underscores as prefix those will not show in suggestion,
#until the particular person go to the code and check it.
#to access those variables/method , we need to copy from the top and paste.. it will not show in suggesion but we can access directly.
    obj._show_address_and_time()   #for single underscore we can access direcly. but for double underscore cant b accessed directly.
    #obj._class__method/variable , for double underscore --  obj.single underscore class name double underscore method/variable
    #variable is there without paranthesis, method is there then with paranthesis()
    obj._school__show_city_rank()

    print(dir(obj))  #-- > here it will show but the only difference is it will not suggest


