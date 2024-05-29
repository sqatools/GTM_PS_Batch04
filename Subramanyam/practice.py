# Median of given list
lst = [45,60,61,66,70,77,80]

lst.sort()

a = (len(lst))/2

print(lst[int(a)])


# (a2 + b2 = c2)

''' a =2
b = 3
c =a+b

L = a**2+b**2
R = c**2
print(L==R,L,R)
'''

import math
s1 = 2
s2 = 3

hypo = s1**2+s2**2
print("Hypotenious side: ",math.sqrt(hypo))

# (a + b)2 = a^2 + b^2 + 2ab

a = 4
b= 5

y= a**2+b**2+2*a*b
x=(a+b)**2
print("(a + b)2 = a^2 + b^2 + 2ab",x==y,"\nvalve of (a+b)2 is :",x,"\nvalve of a2+b2+2ab is :",y )

print("$"*100)

# (a - b)2 = a^2 + b^2 - 2ab

a = 4
b= 5

y= a**2+b**2-2*a*b
x=(a-b)**2
print("(a - b)2 = a^2 + b^2 - 2ab valve is :",x==y)

print("&"*100)

# (a + b)3 = a3 + 3ab(a+b) + b3

x = (a+b)**3
y = a**3+b**3+3*a*b*(a+b)

print("(a + b)3 = a3 + 3ab(a+b) + b3 valve is :",x==y)

print("@"*100)
# (a – b)3 = a3 – 3a2b + 3ab2 – b3

x = (a-b)**3

y = a**3-3*a**2*b+3*a*b**2-b**3

print("(a + b)3 = a3 + 3ab(a+b) + b3 valve is equal?:",x==y," x valve is ",x, "y vale is ",y)


# area = a*a
'''
area = a*a

print(area)

num = float(input(" Enter the valve for area :"))

print("Area of a given :",num**2)

""" Formula = PI*r*r
r = radius
PI = 3.14 """

r = int(input("Enter the valve of radius"))
A = 3.14*r*r
print("Area of given radius 3,14*r2: ", A)

# Python program to calculate the area of a cube.
# Formula = 6*a*a

C = int(input("Enter the cube valve: "))
cube = 6*C*C

print("Area the cube valve is :", cube)

# Python program to calculate the area of the cylinder.
# Formula = 2*PI*r*h + 2*PI*r*r

ri = int(input("Enter the radius of the cylinder: "))
hi = int(input("Enter the hight of the cylinder: "))

area = (2*3.14*ri*hi)+(2*3.14*ri*ri)

print("Area of cylinder of given diamentions:",area)

#  given number is an Armstrong number or not.
# Example: 153 = 1*1*1 + 5*5*5 + 3*3*3

Ar= ab = int(input(" Enter the number "))
rev = 0

while ab>0:
    rem= ab%10
    rev=rev +rem**3
    ab =ab//10

if rev ==Ar:
    print("It is a armstrong number")
else:
    print("It is not a armstrong number")
'''
# Python program to calculate simple interest.
# Formula = P+(P/r)*t
#  P = Principle Amount
# r = Anual interest rate
# t = time

p =4250000
r= 12
t=20

amount = p+(p/r)*t
print('Amount :',amount)
# Python program to print the current date in the given format
# Output: 2023 Jan 05

import datetime
date = datetime.datetime.now()

print (date.strftime (" %Y %b %d "))

#  Python program to calculate days between 2 dates.
# Input date : (2023, 1, 5) (2023, 1, 22)

from datetime import date


d1 = date(1993,12,3)
d2 = date(2024,5,21)

result1 = (d2 - d1).days
print ("Number of Days between the given Dates are: ", result1, "days")

result2 = ((d2 - d1).days)//30
print ("Number of Days between the given Dates are: ", result2, "months")

result3 = ((d2 - d1).days)/365
print ("Number of Days between the given Dates are: ", result3, "years")


#  Python program to get the factorial of the given number.
'''
num =n= int(input("Enter the number: "))
fact = 1

while n >0:
    fact *= n
    n -=1

print(f"factorial of {num}:{fact}")
'''
''' Python program to reverse a given number.

num = int(input("Enter the number : "))

reverse = str(num)

print('Reverse :',reverse[::-1])
print("_"*50)

'''

# Python program to get the Fibonacci series between 0 to 50.
'''
n1 = 0
n2 = 1

count =0

print("sequence in:  ",end="\n ",)
while count<50:
    print(n1,end=" ")
    n3 = n1+n2
    n1=n2
    n2=n3
    count +=1

print("Bye")

'''



#  Python program to check given number is palindrome or not.
'''
n= num =int(input("Enter the number :"))

rev = 0

while n>0:
    rem = n%10
    rev = rev *10 +rem
    n=n//10

if num==rev:
    print("given number is a palindrome number")
else:
    print("given number is a not palindrome number")

'''
#  Python program to calculate compound interest.
# formula p((1+r/100)**n).

'''
p = int(input("Enter principle amount: "))
r = float(input("Enter interest rate: "))
n = int(input("Enter number of years: "))

amount = p*((1+r/100)**n)

print("Compoud interest: ",amount) '''

print("#"*100)

# Python program to check the prime number.
'''
num1 = int(input("enter the valve :"))
count = 0

for i in range(1,num1+1):
    if num1%i == 0:
        count+=1

if count == 2:
    print(f"{num1} is a prime number")
else:
    print(f"{num1} is not a prime number")
'''
# Python program to check leap year.


year = int(input("Enter a year: "))

if (year%400 == 0 or year%100 != 0) and year%4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")