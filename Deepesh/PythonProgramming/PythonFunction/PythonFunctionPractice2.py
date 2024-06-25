# documentation of function

def factorials(n: int):
    """
    This function will provide the factorials any given number.
    e.g fact of 5 = 5*4*3*2*1
    :param n: This the value need to pass to get the factorial
    :return:
    """
    fact = 1
    for i in range(n, 0, -1):
        fact = fact * i

    print(f"factorials of given number :{n} {fact}")


# factorials(6)
# factorials("Hello")
#
# print(factorials.__doc__)
#
# str1 = "Hello"
# str1.upper()


"""
Variables scope:
Local variable : we define local variable inside the function and scope of local variable is 
                 limited to that particular function only. 
Global variable : The variable we declare out side of the function, it is kwon as global variable
                  and the scope of global variable is across the modules.
                  
                  
Notes : 
      - If we defined same name variable inside the function as global variable then
        that variable will be consider as local variable and limited to that function only.
        
      - If we want to change the global variable value inside the function then we have to user
         `global` keyword, and changes will available across the modules.
          

Non-local variable :
"""

var_x = 100  # global variable


def function1():
    print("-----Function1-------")
    global var_x
    var_y = 200  # local variable
    var_x = 600
    print("global variable var_x :", var_x)
    print("local variable var_y :", var_y)


def function2():
    print("-----Function2-------")
    var_z = 300  # local variable
    print("global variable var_x :", var_x)
    print("local variable var_z :", var_z)


# function2()
# function1()
# function2()


#########################################

var_p = 200  # global variable


def outer_function():
    var_q = 300  # non local variable

    def inner_function1():
        print("_______inner_function1______\n")
        global var_p
        nonlocal var_q
        var_r = 400  # local variable
        var_p = 250
        var_q = 700

        print("global variable var_p :", var_p)
        print("Non local variable var_q :", var_q)
        print("local variable var_r :", var_r)

    def inner_function2():
        print("_______inner_function2______\n")
        var_s = 500  # local variable
        print("global variable var_p :", var_p)
        print("Non local variable var_q :", var_q)
        print("local variable var_s :", var_s)

    inner_function2()
    inner_function1()
    inner_function2()


outer_function()
