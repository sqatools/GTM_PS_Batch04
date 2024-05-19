#1 a^2-b^2=(a-b)(a+b)
a=3
b=2
LHS=a**2-b**2
print("LHS is:",LHS)
c=a-b
d=a+b
RHS=c*d
print("RHS is:",RHS)
RHS=a-b*a+b
print("RHS is:", RHS)
print("_"*50)
#2 a^2+b^2=(a+b)^2-2ab
a=3
b=2
LHS=a**2+b**2
print("LHS is:",LHS)
c=(a+b)**2
d=2*a*b
RHS=c-d
print("RHS is:",RHS)
print("-"*50)

#3 (a-b)^2=a^2+b^2-2ab

a=3
b=2
LHS=(a-b)**2
print("LHS is:",LHS)
RHS=a**2+b**2-(2*a*b)
print("RHS is:",RHS)

#4 (a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca

a=4
b=3
c=2
LHS=(a+b+c)**2
print("LHS is:",LHS)
RHS=a**2+b**2+c**2+2*a*b+2*b*c+2*c*a
print("RHS is:",RHS)

#5 (a-b-c)^2= a^2+b^2+c^2-2ab+2bc-2ca

a=8
b=4
c=2
LHS=(a-b-c)**2
print("LHS is:",LHS)
RHS=a**2+b**2+c**2-(2*a*b)+(2*b*c)-(2*c*a)
print("RHS is:",RHS)

