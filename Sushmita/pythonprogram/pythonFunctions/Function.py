def addition():
    num1 = 50
    num2 = 60
    num3 = num1 + num2
    print("addition :", num3)

addition()

def addition_values(num1=60, num2=70):
    #num3 = num1 + num2
    print("addition of values :", num1+num2)

# pass by value
#addition_values(40, 50)

# pass by reference
x = 600
y = 700
#addition_values(x, y)

# p  = int(input("Enter first value :"))
# q  = int(input("Enter second value :"))
# addition_values(p, q)

# addition_values()  # 130

def multiplication(n1, n2=5):
    print("n1 :", n1)
    print("n2 :", n2)
    print("multiplication :", n1*n2)

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
def function_a(var1=5, var2=7):
    print("addition :", var1 + var2)

function_a(30,20)
function_a(3,2)
function_a()

def function_b():
    x=10
    y=20
    print('additoon:',x+y)

function_b()


###############################
##### * args : args parameter accept the n number values and can be consider.

def functon_c(a1,a2,a3,a4,a5):
    print('multiplication:',a1*a2*a3*a4*a5)

functon_c(1,2,3,4,5)
#functon_c(1,2,3,4,5,6) TypeError: functon_c() takes 5 positional arguments but 6 were given

print("_" * 50)


def function_d(*args):
    print(args)
    #print("addition  of values :", sum(args))
    for val in  args:
        print(val)

function_d(2,3)
function_d(3,4,5,6)

def args_multiply(*sushmita):
    multival=1
    for val in sushmita:
        multival=multival*val

    print('output:',multival)
#args_multiply(3,4)
args_multiply()
args_multiply(1,2,3,4)

#################################
# use of **kwargs : This parameter accepts the values in the key value pair

def get_user_details(**kwargs):
    print("kwargs :", kwargs)

#get_user_details(name='sushmita')
    for key, val in kwargs.items():
        print(key, ":", val)

get_user_details(username='Rahul', email='rahul@gmail.com', phone=534543543, address="Mumbai")

print("_"*50)

def get_user_details_number(*args, **kwargs):
    print('kwargs:',kwargs)

    for k,v in kwargs.items():
        print(k,':',v)

    print(args)

get_user_details_number(2,3,4,5,name='sush',age=34,phone_nu='234566')

print("_" * 50)


############### Return statement in function #########
# return statement : return statement provide functionality to the function to return
#                     any value that can store in any variable

def addition_data(v1, v2):
    return v1+v2
output = addition_data(40, 50)
print("addition :", output)

print('_'*50)

def multiplication_data(v1,v2,v3):
    output=addition_data(v1,v2)
    return output *v3

result=multiplication_data(4,5,8)
print('result:',result)

def divide_data(n1,n2):
    return n1/n2

result1=divide_data(result,8)
print('result1:',result1)

print('_'*50)

def muliple_values(a,b,c):
    add=a+b
    multi=b * c
    div=a/c
    return add,multi,div

v1,v2,v3=muliple_values(30,20,10)
print('add:',v1)
print('mul:',v2)
print('div:',v3)

result=muliple_values(40,20,10)
print('result:',result)
print("result :", result[2])  #4.0
