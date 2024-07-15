def addition():
    try:
        a=2
        b=2.25
        c= a + b
        print("addition: ",c)
    except Exception as e:
        print(e)
        print("can not add string with integer")
#addition()


def addition_raise():
    try:
        a=10
        b='hello'
        c=a+b
        print("addition: ",c)
    except Exception as e:
        print("can not add string with integer")
        raise e

#addition_raise()

def try_raise_else_condition(num1,num2):
    try:
        num3=num1+num2
        print("addition: ",num3)
    except Exception as e:
        print(e)
        print("can not add string with integer")
    else:
        multiplication=num1*num2
        print(multiplication)

#try_raise_else_condition("hel",5)
#try_raise_else_condition(5,6)

def try_raise_else_finally_condition(num1,num2):
    try:
        num3=num1+num2
        print("addition: ",num3)
    except Exception as e:
        print(e)
        print("can not add string with integer")
    else:
        multiplication=num1*num2
        print(multiplication)
    finally:
        for i in range(1,11):
            print(num1,'*',i,"=",num1*i)

#try_raise_else_finally_condition(5,5)

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

#code_with_multiple_exception(5,6,3)


def nested_execption_condition(num1,num2,num3):
    try:
        print("addition: ",num1+num2)
        try:
            print("divide: ",num2//num3)
        except Exception as e:
            print(e)
            print("can not divide any number with zero")

    except Exception as e:
        print(f'can not add string with int : {e}')

nested_execption_condition(5,6,0)




