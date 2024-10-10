"""
Decorator : decorator is a external function which decorate the existing code without modifying the
functionality of existing code.
"""

def decorate(func):
    def inner():
        print("*"*20)
        func()
        print("*"*20)
    return inner


@decorate
def greeting():
    print("Good Morning")

#greeting()

@decorate
def addition():
    num1 = 40
    num2 = 60
    print("Addition of values :", num1+num2)

#addition()


def mul_decorate(func):
    def inner(*args):
        print("*"*20)
        func(*args)
        print("*"*20)
    return inner


@mul_decorate
def multi(x, y):
    print("multiplication :", x*y)


var1 = 60
var2 = 50
multi(var1, var2)


@mul_decorate
def addition_with_params(p, q, r):
    print("addition of params :", p+q+r)


addition_with_params(40, 50, 60)



# write a python program to get all even between 1 to 50

def range_decor(func):
    def inner(param):
        if param > 50:
            param = 50
            func(param)
            print("execution is successful")
        else:
            func(param)
            print("execution is successful")
    return inner


@range_decor
def get_even_number(range_val):
    for i in range(range_val):
        if i%2 ==0:
            print(i, end=" ")
        else:
            continue

get_even_number(3000)
