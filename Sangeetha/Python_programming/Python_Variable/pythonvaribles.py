"""""""""
a = 1
b = 2
print(a + b)

#################
a = 10
b = 20
print(a - b)

#########
a = 15
b = 25
print(a * b)

##########
str1 = "SQATOOLS"
print("SQATOOLS" * 5)

##############
str1 = "sangeetha"
print("\nsangeetha" * 5)

##################
a = 40
b = 50
c = 30
print("Average: ",(a+b+c)/3)

#############################
num1 = 9
print("square of 9 :", 9**2)
print("cube of 9 :", 9**3)

"""
"""

list = [55,34,67,89,10]
list.sort()
print(list)
median =(len(list))/2
print("median : ", list[int(median)])

"""
"""

#(a2 + b2 = c2)

import math
side1 = 3
side2 = 4
hype=side1**2 + side2**2
side3=math.sqrt(hype)
print (side3)

import random

for i in range(5):
    print(random.random())
"""
"""

import datetime

date=datetime.datetime.now()
 print(date.strftime(" %y %M %d "))

"""

num = int(input("Enter a number: "))

reverse = str(num)

print("Reverse: ",reverse[::-1])


