# Python program to check whether the given character is lowercase or not.

a = "H"
if a.islower():
    print("True")
else:
    print("false")

# Python program to check whether the given number is an integer or not.

x=9
if x.is_integer():
    print("integer")
else:
    print("not integer")

x1="ij"
if type(x1)==int:
    print("integer")
else:
    print("not integer")

# Python program to check whether the given number is float or not.

y =98
if type(y)==float:
    print("float")
else:
    print("Not float")

#Python program to check whether the given input is a string or not.

str1 = 56
if type(str1)==str:
    print("True")
else:
    print("False")

# Python program to print all the numbers from 10-15 except 13

for i in range(10,16):
    if i==13:
        continue

    print(i)


for i in range(10,16):
    if i!=13:
        print(i)

''' Python program to find the electricity bill. According to the following conditions:
Up to 50 units rs 0.50/unit
Up to 100 units rs 0.75/unit
Up to 250 units rs 1.25/unit
above 250 rs 1.50/unit
an additional surcharge of 17% is added to the bill'''

units=int(input("Enter the units: "))
bill = 0
if units<=50:
    print("bills is ",units*0.50)
    bill=bill+units*0.50
elif units>50 and units<=100:
    print("bills is ",units*0.75)
    bill=bill+units*0.75
elif units>100 and units<=250:
    bill = bill + units * 1.25
else:
    bill = bill + units * 1.5

total_bill = bill + bill*(17/100)
print("total bill amount :", total_bill)


total_unit =int(input("Enter the unit as per meter: "))
bill_amount=0

for bill_unit in range(1, total_unit+1):
    if bill_unit <= 50:
        bill_amount = bill_amount + 0.50
    elif bill_unit >50 and bill_unit <= 100:
        bill_amount = bill_amount + 0.75
    elif bill_unit > 100 and bill_unit <= 250:
        bill_amount = bill_amount + 1.25
    elif bill_unit > 250:
        bill_amount = bill_amount + 1.5

bill_sur = bill_amount + bill_amount * (17/100)
print("Bill amount with surcharges",bill_sur)

'''
total_unit = int(input("Total units Consumed="))
bill_amount = 0

# If each unit we will add to rate amount in total bill amount
for bill_unit in range(1, total_unit+1):
    if bill_unit <= 50:
        bill_amount = bill_amount + 0.50
    elif bill_unit > 50 and bill_amount <= 100:
        bill_amount = bill_amount + 0.75
    elif bill_unit > 100 and bill_amount <= 250:
        bill_amount = bill_amount + 1.25
    elif bill_unit > 250:
        bill_amount = bill_amount + 1.5

# Addition 17% surcharge on total bill amount
bill_amount_sur = bill_amount + bill_amount * (17/100)
print("Bill amount with surcharge :", bill_amount_sur)
'''

# Python program to check whether a given year is a leap or not.Inin

n= 2001

if (n%400==0 or n%100!=0) and n%4==0 :
    print("leap year")
else:
    print("non leap year")

# Python Python program to check whether the input number if a multiple of two print “Fizz” instead of the number and for the multiples of three print “Buzz”. For numbers that are multiples of both two and three print “FizzBuzz”.
'''
b = int(input("number"))
if b%2==0 and b%3==0:
    print("FizzBuzz")
elif b%2==0:
    print("Fizz")
elif b%3==0:
    print("Buzz")
'''
#  Python program to check whether an alphabet is a vowel.
'''
c = input("Enter the data")

vowel = ["A","E","I","O","U","a","e","i","o","u"]
if c in vowel:
    print("true")
else:
    print("false")
'''

# Python program to check whether an alphabet is a consonant.
'''
d = input("Data please: ")
consonant =['A','E','I','O','U','a','e','i','o','u']

if d not in consonant:
    print("True")
else:
    print("False")
'''

# Python program to convert the month name to the number of days.
'''
month = input("Enter month: ").lower()

if month == "january":
    print("Number of days: 31")
elif month == "february":
    print("Number of days: 28/29")
elif month == "march":
    print("Number of days: 31")
elif month == "april":
    print("Number of days: 30")
elif month == "may":
    print("Number of days: 31")
elif month == "june":
    print("Number of days: 30")
elif month == "july":
    print("Number of days: 31")
elif month == "august":
    print("Number of days: 31")
elif month == "september":
    print("Number of days: 30")
elif month == "october":
    print("Number of days: 31")
elif month == "november":
    print("Number of days: 30")
elif month == "december":
    print("Number of days: 31")
else:
    print("Invalid month")

'''
# Python program to check whether a triangle is equilateral or not. An equilateral triangle is a triangle in which all three sides are equal.

a = 10
b=10
c=10

if a==b==c:
    print("equilateral triangle and True")
else:
    print("Non equilateral triangle")

# Python program to check whether a triangle is scalene or not. A scalene triangle is a triangle that has three unequal sides.
x=10
y=12
z=14

if x!=y!=z:
    print("scalene triangle and  True")
else:
    print("non scalene triangle")

# Python program to check whether a triangle is isosceles or not. An isosceles triangle is a triangle with (at least) two equal sides.

d=12
e=10
f=10

if d==e or d==f or e==f:
    print("true")
else:
    print("False")

# Python program that reads month and returns season for that month.
'''
month = input("month name: ")

if month=="feb" or month=="mcr" or month=="april" or month=="may":
    print("summer")
elif month=="june" or month=="july" or month=="aug" or month=="sept":
    print("rainy")
elif month=="jan" or month=="octo" or month=="nove" or month=="dece":
    print("winter")
else:
    print("please valid month")
'''
# Python program to check whether the input number is a float or not if yes then round up the number to 2 decimal places.

g=65.3698

if type(g)==float:
    print(round(g,2))
else:
    print("not a float")

# Python program to check whether the input number is divisible by 12 or not.

k = 125
if k%12==0:
    print("True")
else:
    print("false")


# Python program to check whether the input number is a square of 6 or not.
import math
num = 65

if num==6**2:
    print("True")
else:
    print("false")

# Python program to check whether the input number is a cube of 3 or not.

num1 =26

if num1==3**3:
    print("True")
else:
    print("False")

#  Python program to check whether two numbers are equal or not.

A=22
B=88

if A==B:
    print("both are equal")
else:
    print("both are not equal")

#  Python program to check whether two numbers are equal or not.

X=2+6j

if type(X)==complex:
    print("True")
else:
    print("false")

# Python program to check whether the given input is Boolean type or not.

t=56

if type(t)==bool:
    print("True")
else:
    print("false")
