def addition():
    num1 = 50
    num2 = 60
    num3 = num1 + num2
    print("addition :", num3)







# addition()
# addition()
# addition()
# addition()

def addition_values(num1=60, num2=70):
    # num3 = num1 + num2
    print("addition of values :", num1 + num2)


# pass by value
# addition_values(40, 50)

# pass by reference
x = 600
y = 700


# addition_values(x, y)

# p  = int(input("Enter first value :"))
# q  = int(input("Enter second value :"))
# addition_values(p, q)


# addition_values()  # 130


# function with default param value
def multiplication(n1, n2=5):
    print("n1 :", n1)
    print("n2 :", n2)
    print("multiplication :", n1 * n2)


multiplication(4)
multiplication(4, 6)
multiplication(n2=7, n1=6)
multiplication(n2="Hello", n1=6)

"""
function concept
1. function can be defined without any parameter.
2. With out calling the function, code will not execute.
3. We can assign value to Function with parameter with 2 ways
   - Pass by value  e.g. addition(40, 50)
   - Pass by reference  e.g. addition(x, y)
4. Function parameter can have default value.
   - If param has default, then no need to pass value while calling function.
   - If New value has assign to default param while calling function, 
     then default value will be overwrite.
   - If One function has two params one is default param and second non default param
     then default params always follows the non default params
"""

print("_" * 50)


def function_a(var1=5, var2=7):
    print("addition :", var1 + var2)


function_a(40, 30)
function_a(50, 80)
function_a(41, 33)
function_a()


def function_b():
    var1 = 500
    var2 = 600
    print("addition of value :", var1 + var2)


function_b()
function_b()
function_b()


###############################
##### * args : args parameter accept the n number values and can be consider.

def function_c(a1, a2, b3, b4, b5):
    print("multiply :", a1 * a2 * b3 * b4 * b5)


# function_c(5, 7, 8, 2)
# TypeError: function_c() missing 1 required positional argument: 'b5'

# function_c(4, 7, 2, 8, 1, 14, 56)
# TypeError: function_c() takes 5 positional arguments but 7 were given

print("_" * 50)


def function_d(*args):
    print(args)
    # print("addition  of values :", sum(args))
    for val in args:
        print(val)


# function_d(5, 6)
# function_d(15, 16, 12)
# function_d(12, 26, 35, 67)
# function_d(4.5, (4, 5, 6), 'Python', [3, 6, 1, 2], {'a': 123, 'b' : 345})


def args_multiply(*keerthi):
    mul_val = 1
    for val in keerthi:
        mul_val = mul_val * val

    print("output :", mul_val)


args_multiply(4, 5)
args_multiply(12, 26, 35)
args_multiply(12, 26, 35, 11, 22)

print("_" * 50)


#################################
# use of **kwargs : This parameter accepts the values in the key value pair

def get_user_details(**kwargs):
    print("kwargs :", kwargs)

    for key, val in kwargs.items():
        print(key, ":", val)


get_user_details(username='Rahul', email='rahul@gmail.com', phone=534543543, address="Mumbai")

print("_" * 50)


def get_user_details_numbers(*args, **kwargs):
    print("kwargs :", kwargs)

    for key, val in kwargs.items():
        print(key, ":", val)

    print(args)


get_user_details_numbers(5, 6, 22, 77, 12, name="Chetan", lastname="karu", phone=3543534534, email='chetan@gmail.com')

print("_" * 50)


############### Return statement in function #########
# return statement : return statement provide functionality to the function to return
#                     any value that can store in any variable


def addition_data(v1, v2):
    return v1 + v2


output = addition_data(40, 50)
print("addition :", output)


# write a python function to add first two variables and multiply by third variable
def multiplication_data(v1, v2, v3):
    output = addition_data(v1, v2)
    return output * v3
#print("Good morning")

def divide_data(n1, n2):
    return n1/n2

result = multiplication_data(5, 6, 7)
print("result :", result)

divide_result = divide_data(result, 5)
print("Divide result :", divide_result)


print("_"*50)
# return statement with multiple return values
def math_operation(v1, v2, v3):
    add = v1+v2
    mul = v2*v3
    divide = v3/v1
    return add, mul, divide

a, b, c = math_operation(20, 30, 40)
print("addition :", a)  # 50
print("multiplication :", b) # 1200
print("Division :", c)

result = math_operation(50, 70, 90)
print("result :", result)  # (120, 6300, 1.8)
print("result :", result[2])  # 1.8



