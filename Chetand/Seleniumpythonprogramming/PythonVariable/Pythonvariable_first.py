var1 = 10
print(var1)
print(type(var1))
print(id(var1))

#############################

var2 = "Good Morning"
print(var2)
print(type(var2))
print(id(var2))

# Multiple variable with same value then their  address will be same

a = 15
b = 15
print(id(a)) # 140734774211816
print(id(b)) # 140734774211816

#  assign multiple values to multiple variable at a time

p, q, r = 50, 60, "Hello"
print("value of p :", p)
print("value of q :", q)
print("value of r :", r)

#### Math opertaion with numbers ####
"""
+ : Plus operator
- : Minus operator
* : Multiplication operator
/ : Division operator
//: Division operator
** : Power operator
== : Equal to operator
= : Assignment operator
"""
print("_"*50)
# + :  Plus operator

a1 = 400
b1 = 700
c1 = a1+b1
print("addition:",c1)


# - :  Minus operator

a1 = 422
b1 = 567
c1 = a1-b1
print("Minus:",c1)
print("Substraction :", a1-b1)

# * :  Multiplication operator

a1 = 12
b1 = 51
c1 = a1*b1
print("Multiplication:",c1)
print("Multiplication:", a1*b1)