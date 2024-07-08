# execute the exception code without raising it, which does not affect further code execution

# def multiply():
#  try:
#     a=10
#     b="world"
#     c=a*b
#     c=a+b
#     print("multiply:", c)
#     print("addition:", c)
#  except Exception as e:
#     print(e)
#     print("cannot multiply string with integer")
#     print("cannot add string with integer")
#
# multiply()
#
# # when we execute and raise the exception, then further code execution will stop working
#
# def addition_with_raise():
#     try:
#         x = 60
#         y = 'Hello'
#         z = x + y
#         print("addition :", z)
#     except Exception as e:
#         print("Can not add string with integer")
#         raise e
# addition_with_raise()

#need some clarification
def operations_with_raise():
  try:
    m=10
    n=5
    p=m+n
    q=m-n
    r=m*n
    print("addition:",p)
  except Exception as e:
    print(e)
    raise(e)
  print("multiplication:", r)
  print("subtraction:",q)
operations_with_raise()

######## try -except- else #######
# else section code only executes, when there is no exception.

def try_except_else_condition(num1, num2):
    try:
        c = num1 + num2
        print("adddition :", c)
    except Exception as e:
        print(e)
        print("Both the variable should have int value")
    else:
        multiplication = num1 * num2
        print(" multiply :", multiplication)


#try_except_else_condition(50, 2)
#try_except_else_condition(50, "hello")

#whatever we will give in the print it will display not link with code.
print("Goodevening")



######## try -except- else - finally #######
# finally : finally code block always executes the code, if there is exception or no exception.
def try_except_else_finally_condition(num1, num2):
    try:
        c = num1 + num2
        print("addition :", c)
    except Exception as e:
        print(e)
        print("Both the variable should have int value")
    else:
        multiplication = num1 * num2
        print(" multiply :", multiplication)
    finally:
        print("_____finally coded block______")
        for i in range(1, 11):
            print(num1, "*", i, ":", num1*i)


#try_except_else_finally_condition(6, "Python")
#try_except_else_finally_condition(6, 5)

def code_with_multiple_exception(num1 : int, num2 : int, num3: int):
    try:
        add = num1+num2
        print("addition :", add)
        division = num2//num3
        print("Division :", division)
        power_multiply = num2**num3
        print("power value of num2 and num3 :", power_multiply)
        var = "Hello"
        print(float(var))

    except ValueError:
        print("both variable should have correct value")
    except ZeroDivisionError:
        print("Can not divide any number with zero")
    except TypeError:
        print("Required data is not provide")
    except Exception as e:
        print(e)

code_with_multiple_exception( 2,  0,  "hello")
#Required data is not provide

code_with_multiple_exception( 5,  0,  7)
#addition : 5
#Division : 0
#power value of num2 and num3 : 0
#both variable should have correct value

code_with_multiple_exception(30, 10, 2)
#addition : 40
#Division : 5
#power value of num2 and num3 : 100
#both variable should have correct value-->Need to check

###### Nested exception condition ######

def nested_exception_condition(num1, num2, num3):
    try:
        print("addition :", num1+num2)
        try:
            print("multiply :", num2//num3)
        except Exception as e:
            print(e)
            print("Can not divide number by zero")

    except Exception as e:
        print(f"Can not add string with int : {e}")

nested_exception_condition(4, 1, "python")
'''
addition : 5
unsupported operand type(s) for //: 'int' and 'str'
Can not divide number by zero
'''

nested_exception_condition(2, 6, 0)
#addition : 8
#integer division or modulo by zero
#Can not divide number by zero

nested_exception_condition("hello", 6, 0)
#Can not add string with int : can only concatenate str (not "int") to str








