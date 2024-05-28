''''# Python program to check for the anagram. print the iteration
word = input("Enter the words :")
combination = 0
character = len(word)

while character>0:
    combination+=character
    print(combination)
    character -=1

print("Total combination without repetaation: ",combination)
#  Python program to generate random numbers. sum of random value ---0.00###
import random
sum_val = 0
for i in range(25):
    val = random.random()
    print(val)
    sum_val += val

print("sum value  :", sum_val)

#  Python program to generate random numbers. sum of random value ---10,12,14 ###

import random
sum_val = 0
for i in range(5):
    val = random.randint(30, 50)
    print(val)
    sum_val += val

print("sum value  :", sum_val)

'''
import re

i =1
while i <=3:
    print(i,end=" ")
    i +=1
    print(i,end=" ")
    i += 1
    print(i, end="")

list = [1,2,3,4,5,6,7,8]
print(list[7:5:-1])


a =10
for i in range(1,6):
    a=a*i
    print(a)

print(a)

print("9"*100)
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

email = 'example@eaxmple.com'

if re.match(pattern,email):
    print("Valid email")

else:
    print("InValid email")


print("7"*100)


num =a= 153

rev = 0
while a>0:
    rem=a%10
    rev=rev+rem**3
    a=a//10

if num==rev:
    print("yes")

else:
    print("no")
print(rev)

from datetime import datetime

dt = datetime.now()
print(dt.strftime("%Y %b %d"))

num1=a1=5

fact = 1

while a1>0:
    fact*=a1
    a1-=1

print(f'factorial of {num1} : {fact}')


num2 = 5678

reverse = str(num2)

print("reverse of ", reverse[::-1])
'''

num1=0
num2=1

count=0

print("the sequence of :",end=" ")
while count <50:
    print(num1,end=" ")
    n=num1+num2
    num1=num2
    num2=n
    count+=1

'''
print("&"*100)

n=int(input("Number"))
sum_val =0
for i in range(1,n+1):
    if i%2==0:
        continue
    sum_val+=1

print(i,end=" ")
print(sum_val,end="")


import random
sum_val = 0
for i in range(5):
    val = random.randint(30, 50)
    print(val)
    sum_val += val