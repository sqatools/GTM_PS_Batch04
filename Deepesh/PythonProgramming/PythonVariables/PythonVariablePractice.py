var1 = 10
print(var1)
print(type(var1))
print(id(var1))

###############################
var2 = "Good Morning"
print(type(var2))
print(var2)
print(id(var2))

# multiple variable with same value then their address will be same
a = 15
b = 15
print(id(a)) # 140714657074040
print(id(b)) # 140714657074040

# assign multiple values to multiple variables at a time

p, q, r = 50, 50, "Hello"
print("value of p :", p, id(p))
print("value of q :", q, id(q))
print("value of r :", r, id(r))

print("_"*50)
# Assign one value to multiple variables
x = y = z = 100
print("value of x :", x, id(x))
print("value of y :", y, id(y))
print("value of z :", z, id(z))

# Rules to declare variable
# 1. There should not be space in variable name

# var name = 100 : invalid
var_name = 400
var_name_variable_value = 500

# 2. special character are not allowed in variable name

# city%name = 'Mumbai' # invalid
# cit_name  : valid
# my&name = 'Rahul' # invalid
# my_name # valid

# 3. Number is not allowed in the begining of variable name

# 123var = 500 # invalid
# var_123 = 600 # valid

# 4. There is no limitation for variable name, we can declare any length variable
# abc_pqr_xyz_trtretireitreopitroeitr = 600 : valid

# 5. The variable are case sensitive

name = 'Rahul'
NAME = 'Mohit'
Name = 'Rohit'

print("name :", name)
print("NAME :", NAME)
print("Name :", Name)

# 6. variable name declaration should start from begining of any line
#    can not add space and then declare variable name.


##### Math operations with numbers ####
# """ : triple quote we use for multiline comments
"""
+ : plus operator
- : minus operator
* : multiplication operator
/ : division operator
// : division operator
%  : Remainder operator
** : power operator
== : equal to operator
= : Assignment operator
!= : not equal to operator
"""

print("_"*50)
# + : plus operator

a1 = 500
b1 = 600
c1 = a1+b1
print("addition :", c1)


# - : minus operator
p1 = 500
p2 = 300
p3 = p1 - p2
print("subtraction :", p3)
print("subtraction :", p1-p2)

# * : multiplication operation
x1 = 5
x2 = 50
x3 = "Hello"
print("multiplication :", x1*x2) # 250
print("Repeat string :", x3*x1) # HelloHelloHelloHelloHello

# division with single / and double //

q1 = 50
q2 = 6
q3 = 7
print("division with single / :", q1/q2) # 8.333333333333334
print("division with double // :", q1//q3) # 7


# % : remainder operator

var1 = 14
var2 = 5
print("remainder value :", var1%var2) # 4

# ** power operator
print("square of 5 :", 5**2) # 25
print("cube of 6 :", 6**3) # 216

# == : equal to operator
v1 = 500
v2 = 600
v3 = 500
print("compare and v1 and v2 :", v1 == v2) # False
print("compare and v1 and v3 :", v1 == v3) # True
print("compare and v1 and v3 :", v1 != v2) # True


# solve the equation
#(a+b)^2 = a^2 + b^2 + 2ab
a = 40
b = 30

LHS = (a+b)**2
print("LHS output :", LHS)

RHS = a**2 + b**2 + 2*a*b
print("RHS output :",RHS)

