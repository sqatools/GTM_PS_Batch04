#

word = input("Enter the words :")
combination = 0
character = len(word)

while character>0:
    combination+=character
    character -=1

print("Total combination without repetaation: ",combination)


# how to display those combination word in print statement

# Python program to generate random numbers.

import random
c = 0
for i in range(25):
    print(random.random())   # how to get sum of output
    c+=i
print('#'*100)
print("Total",c)
#  Python program to generate a random string with a specific length.
'''
import string
import random

n = int(input("Enter the string :"))

results = ''.join(random.choices(string.ascii_letters,k=n))

print("The random generated string are: ",str(results))
'''

# Python program to get the current date.

from datetime import datetime

dt = datetime.now()

print("Current date is: ",dt)

#Python program to get the current date.
'''
num = int(input("Enter the number : "))

print(f"Binary form of {num} is",'{0:b}'.format(int(num))) # why we used "f" here and is the use of taht "f"?

name = input("Enter the name : ")
loc = input("Enter the location : ")
age = int(input("Enter the age : "))

print(f'my Name is {name} , I am from {loc} and I {age} years old')
'''

# Python program to find the sum of natural numbers.

'''
num = int(input("Eeter the number: "))
total = 0

for i in range(1,num+1):
    total+=i
print("total",total)
'''

# Python program to find the sum of natural numbers.
'''
num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

if num1>num2:
    smaller = num2
else:
    smaller = num1

for i in range(i,smaller+1):
    if((num1%i==0)and(num2%i==0)):
        hcf=i

print(f"H.C.F of {num1} and {num2}:{hcf}")


if num1>num2:
    greater = num1
else:
    greater = num2

while(True):
    if((greater % num1 == 0)and (greater % num2 ==0 )):
        lcm = greater
        break
    greater+=1

print(f"L.C.M is {num1} and {num2}: {lcm}")
'''

# Python program to find the square root of a number.


import math

n = 256

print(math.sqrt(n))

# Python program to calculate the volume of a sphere.
# Formula = (4/3*pi*r^2)
'''
r = int(input("Enter the number: "))

volume = 4/3*(3.14*r**2)

print("Volume of sphere",volume)
'''
# Python program to perform mathematical operations on two numbers.

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
operation = input("Enter operation of your choice: ")

if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "/":
    print(num1/num2)
elif operation == "*":
    print(num1*num2)
else:
    print("Invalid operation")
