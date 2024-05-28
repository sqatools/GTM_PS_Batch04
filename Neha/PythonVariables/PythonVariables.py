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

print("_"*50)
# Assign one value to multiple variables
x=y=z=100
