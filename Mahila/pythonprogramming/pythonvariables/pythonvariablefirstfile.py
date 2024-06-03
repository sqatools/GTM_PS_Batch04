"""
var1=20
#print variable
print(var1)
#print what kind of data the variable holds
print(type(var1))
#print the address where the variable is stored
print(id(var1))

a1=100
print(a1)
print(modify(a1=200))


#string type
var2 = "good morning"
print(var2)
print(type(var2))

#multiple variable wtih same value,then there address will be same
a=10
b=10
print(id(a))
print(id(b))

#assign multiple values to multiple variables at a time
p, q, r = 50, 60, "hello"
print("value of q :", q)
print("value of r :", r)

print("-"*50)
#assign one value to multiple variable
x = y = z =100
print("value of z : ",z)
print("value of y : ",y)


print("_"*50)
print("hello"*8)

##Operators

#1)addition
print("-"*50)
a1=500
b1=400
c1=a1+b1
print("addition : ", c1)

#2)subtraction

print("-"*50)
p1=100
p2=50
print("subtract :", p1-p2)

#3)multiplication

print("-"*50)
x1 = 5
x2 = 6
print("multiplication : ",x1*x2)

print("-"*50)

#4)division with / and //

q1=50
q2=6

print("division : ", q1/q2)
print("division : ", q1//q2)

#5)reminder
print("-"*50)
V1=14
V2=5
print("reminder : ", V1%V2)

#6)power operator

print("-"*50)
print("power of 5 : ", 5**2)

print("-"*50)
"""
#7)equal operator ==
#not equal oeperator !=
V1=500
V2=600
V3=500
print("equals :", V1==V2)
print("equals :", V1==V3)
print("equals :", V1!=V2)

print("-"*50)

#(a+b)^2 = a^2 + 2ab + b^2 -- Quadratic equation
a=40
b=30

LHS = (a+b)**2
print("LHS Output: ",LHS)

RHS = a**2 + 2*a*b + b**2
print("RHS Output :",RHS)
print("-"*50)
#########################################################################################
"""
Python program to repeat a given string 5 times.
Input :
str1 = “SQATools”
Output :
“SQAToolsSQAToolsSQAToolsSQAToolsSQATools” 
"""
str1 = "SQATools"
print(str1*5)

print("-"*50)
"""
Python program to get the Average of given numbers.
Formula: sum of all the number/ total number
Input:
a = 40
b = 50
c = 30
Output :
Average = 40
"""
a = 40
b = 50
c = 30
print("average : ",(a+b+c)/3)

print("-"*50)

"""
Python program to get the median of given numbers.
Note: all the numbers should be arranged in ascending order
Formula : (n+1)/2
n = Number of values
Input : [45, 60, 61, 66, 70, 77, 80]
Output:  66
"""
"""
Python program to print the square and cube of a given number.
Input :
num1 = 9
Output :
Square = 81
Cube =   729
"""

num1=9
print("sqaure =", 9**2)
print("cube =", 9**3)

print("-"*50)
"""
Python program to interchange values between variables.
Input :
a = 10
b = 20
Output :
a = 20
b = 10
"""
a = 10
b = 20
a,b = b,a

print("value of a: ",a)
print("value of b: ",b)

print("-"*50)
"""
Python program to solve this Pythagorous theorem.
Theorem : (a2 + b2 = c2)
"""

"""
Python program to solve the given math formula.
Formula : (a – b)2 = a^2 + b^2 – 2ab
"""
a=10
b=20

LHS = ((a-b)**2)
print(LHS)

RHS =((a**2) + (b**2) - (2*a*b))
print(RHS)

print(LHS==RHS)

print("-"*50)

"""
Python program to solve the given math formula.
Formula : a2 – b2 = (a-b)(a+b)
"""
a=5
b=4

LHS = ((a**2)-(b**2))
print(LHS)

RHS =((a-b)*(a+b))
print(RHS)

print(LHS==RHS)

print("-"*50)

"""
Python program to solve the given math formula.
Formula : (a + b)3 = a3 + 3ab(a+b) + b3 
"""
a=10
b=20

LHS=((a+b)**3)
print(LHS)

RHS=((a**3)+((3*a*b)*(a+b))+(b**3))
print(RHS)

print(LHS==RHS)

print("-"*50)

"""
Python program to solve the given math formula.
Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3
"""
a=10
b=5
LHS =((a-b)**3)
print(LHS)

RHS =((a**3)-(3*(a**2)*b)+(3*a*(b**2))-(b**3))
print(RHS)

print(LHS==RHS)

"""
Python program to calculate the area of the square.
Formula : area = a*a
"""

#Python program to calculate compound interest

