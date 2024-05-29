var1 = 50
print(var1)
print(type(var1))
print(id(var1))
print("_"*50)

var2 = "Happy Sunday"
print(var2)
print(type(var2))
print(id(var2))
print("_"*50)

# multiple variable with same value then their address will be same
a=50
b=100
print(id(a))
print(id(b))

print("_"*50)
# assign multiple values to multiple variables at a time
p,q,r=50,50,"Smera"
print("Value of p:",p, id(p))
print("Value of q:",q, id(q))
print("value of r:",r, id(r))

p, q, r =50, 50, "Smera"
print("Value of p:", p, id(p))
print("Value of q:", q, id(q))
print("value of r:", r, id(r))

print("_"*50)
# Assign one value to multiple variables
x=y=z=100
x= y= z= 100
print("Value of x:", x, id(x))
print("Value of y:", y, id(y))
print("Value of z:", z, id(z))

print("_"*50)
# plus operator(+)
a = 10
b = 30
c = a+b
print("Addition-", c)

print("_"*50)
# Minus operator(-)
a = 10
b = 30
c = a-b
print("Substraction-", c)
print("Substraction-", b-a)

print("_"*50)
# Multiplication operator(*)
a = 10
b = 30
c = a*b
d = "Smera "
print("Multiplication-", c)
print("Multiplication-", d*a)

print("_"*50)
# Reminder operator(%)
a = 10
b = 31
print("Reminder-", b%a)

print("_"*50)
# Power operator(**)
print("Square of 5 is :", 5**2)
print("Cube of of 5 is :", 5**3)

print("_"*50)
# Equal to operator(==)
a = 100
b = 200
c = 100
print("Compare a and b:", a==b)
print("Compare c and b:", c==b)
print("Compare a and c:", a==c)

print("_"*50)
#(a+b)^2 = a^2 + b^2 + 2ab
a = 2
b = 3
LHS = (a+b)**2
print("LHS is :", LHS)
RHS = a**2+b**2+2*a*b
print("RHS is :", RHS)

print("_"*50)
#(a/b)+(c/d)=(ad+bc)/bd
a = 8
b = 4
c = 7
d = 5
LHS = (a/b)+(c/d)
RHS = (a*d+b*c)//(b*d)
print("LHS is :", LHS)
print("RHS is :", RHS)