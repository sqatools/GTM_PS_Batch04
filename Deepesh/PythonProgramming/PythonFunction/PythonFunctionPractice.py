def addition():
    num1 = 50
    num2 = 60
    num3 = num1 + num2
    print("addition :", num3)

#addition()
#addition()
#addition()
#addition()

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


# function with default param value
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
