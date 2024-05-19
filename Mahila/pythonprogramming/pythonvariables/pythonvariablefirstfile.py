var1=20
#print variable
print(var1)
#print what kind of data the variable holds
print(type(var1))
#print the address where the variable is stored
print(id(var1))

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
print("-"*50)
a1=500
b1=400
c1=a1+b1
print("addition : ", c1)

print("-"*50)
p1=100
p2=50
print("subtract :", p1-p2)

print("-"*50)
x1 = 5
x2 = 6
print("multiplication : ",x1*x2)

print("-"*50)
#division with /

q1=50
q2=6
q3=7
print("division : ", q1/q2)
print("division : ", q1//q2)

print("-"*50)
V1=14
V2=5
print("reminder : ", V1%V2)

print("-"*50)
print("power of 5 : ", 5**2)

print("-"*50)

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






