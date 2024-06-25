def factiorial(n: int):
    """
    This function will provide the factorials any given number.
    e.g fact of 5 = 5*4*3*2*1
    :param n: This the value need to pass to get the factorial
    :return:
    """
    fact = 1
    for i in range(n, 0, -1):
        fact = fact * i
    print(f'factiorial of given number:{n} {fact}')


factiorial(4)
# factorial("Hello")

# print(factiorial.__doc__)

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

var_x = 100


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
#############################

var_a = 100  # global variable


def outer_function():
    var_b = 200  # non local variable

    def inner_function1():
        global var_a
        print('----inner function 1\n')
        var_c = 300  # local varible
        var_a = 400
        var_b = 500

        print('Global variable:', var_a)
        print('local variable:', var_c)
        print('non local :', var_b)

    def inner_function2():
        var_d = 600  # local variable
        print('----inner function 1')
        print('Global variable:', var_a)
        print('local variable:', var_d)
        print('non local :', var_b)

    inner_function2()
    inner_function1()
    inner_function2()
