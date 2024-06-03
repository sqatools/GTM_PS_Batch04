"""
#Python Program to add two integer values.

#direct print without assigning third variable
a=1
b=4
print(a+b)

#with third variable

a=2
b=7
c=a+b
print("addition : ", c)


#Python Program to subtract two integer values.

a=50
b=100
print(a-b)

#Python program to multiply two numbers

m1=50
m2=100
print(m1*m2)



#Python program to repeat a given string 5 times.

str1="sqlTOOLS"
print(str1*5)

#Python program to get the Average of given numbers

a,b,c =40,50,30
d=(a+b+c)/3
print("average : " ,d)


########################################################################################################
#A median is the middle number in a sorted list of numbers (either ascending or descending) used in statistical studies
#Program to get the median of given numbers -- > (n+1)/2

list = [55,34,67,89,10]
list.sort()                #list sort() function is an in-built function in Python, that is used to sort the values of a list in ascending or descending order.
print(list)
median =(len(list))/2
print("median : ", list[int(median)])


#########################################################################################################


# Python program to print the square and cube of a given number.

num = int(input("Enter a number :"))
print("square :", num**2)
print("cube : " , num**3)

#Python program to interchange values between variables

a=10
b=50
a,b = b,a    #use = assigning operator
print("value of a :" ,a)
print("value of b :" ,b)

#pythegores theorem a² + b² = c².

import math
side1=3
side2=4
hype=side1**2 + side2**2
side3= math.sqrt(hype)
print(side3)


import math
side1=3
side2=4
side3=math.sqrt(side1**2+side2**2)
print(side3)


#Python program to solve the given math formula.
#Formula : (a + b)2 = a^2 + b^2 + 2ab

a=10
b=20
LHS = (a+b)**2
print("LHS :" ,LHS)
RHS=((a**2)+(b**2)+2*a*b)
print("RHS :", RHS)

print (LHS == RHS)

#Python program to solve the given math formula.
#Formula : (a – b)2 = a^2 + b^2 – 2ab

a=4
b=8
L=(a-b)**2
print(L)
R=a**2+b**2-2*a*b
print(R)
print(L==R)



# program to solve the given math formula.
#Formula : a2 – b2 = (a-b)(a+b)

a=100
b=30
L=a**2-b**2
print(L)
R=(a-b)*(a+b)
print(R)
print(L==R)



#Python program to solve the given math formula.
#Formula : (a + b)3 = a3 + 3ab(a+b) + b3

a=100
b=30

L=(a+b)**3
print(L)
R= (a**3)+(3*a*b*(a+b))+(b**3)
print(R)
print(L==R)



#Python program to solve the given math formula.
#Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3

a=100
b=50
l=(a-b)**3
print(l)
r=(a**3)-(3*a**2*b)+(3*a*b**2)-(b**3)
print(r)
print(l==r)

#Python program to calculate the area of the square

side = int(input("Enter value :"))
area = side*side
print("area of the square :" , area)

# Python program to calculate the area of a circle.
#Formula = PI*r*r
#r = radius
#PI = 3.14


radius = int(input("Enter value :"))
area= 3.14*radius**2
print("area of circle: ", area)


#Python program to calculate the area of a cube.
#Formula = 6*a*a

a =(int(input("Enter side of cube : ")))
area = 6*a**2
print("area of cube : ", area)



#Python program to calculate the area of the cylinder.
#Formula = 2*PI*r*h + 2*PI*r*

r = int(input("Enter value for r:"))
h= int(input("Enter value for h :"))
area = 2*3.14*r*h + 2*3.14*r**2
print("area of cylinder :" , area)

#Python program to calculate simple interest.
#Formula = P+(P/r)*t
#P = Principle Amount
#r = Anual interest rate
#t = time

p=1000
r=10
t=2

SI=p+(p/r)*t
print("Simple interest =", SI )


#Python program to calculate compound interest
#p((1+r/100)**n)

p= int(input("Enter value for p : "))
r= int(input("Enter value for r : "))
n= int(input("Enter value for n : "))

CI = p*((1+r/100)**n)
print("Compound Interest : ", CI)


#Python program to check year is a leap year.
#(year%400 == 0 or year%100 != 0) and year%4 == 0.

year = int(input("Enter a year: "))

if (year%400 == 0 or year%100 != 0) and year%4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


"""





