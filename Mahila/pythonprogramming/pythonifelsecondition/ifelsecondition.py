#1)Program to check if a number is divisible by 3 - directly assigning value
"""
a=30
if (a%3==0):
    print("a is divisible by 3")  #a is divisible by 3
else:
    print("a is not divisible by 3")


a=40
if (a%3==0):
    print("a is divisible by 3")  #a is not divisible by 3
else:
    print("a is not divisible by 3")

print("-"*50)

#2)Program to check if a number is divisible by 3 - user assigning value
#for user assigning value we need to use the function ###input###

n1 = int(input("please enter value : "))    # please enter value : 30           #divisible by 3
if (n1%3==0):
    print("divisible by 3")
else:
    print("not divisible by 3")


num = int(input("Please enter number :"))    #Please enter number : 40   #Number is not divisible by 3
if num%3 == 0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")

print("-"*50)

#3)Program to get all numbers divided by 3 between 1 to 30

for n in range(1,31):
    if n%3==0:
        print(n,end=",")  #print output horizontally - 3 6 9 12 15 18 21 24 27 30

for n in range(1,31):
    if n%3==0:
        print(n)      #print output vertically as below
#--------------------------------------------------
#3
#6
#9
#12
#15
#18
#21
#24
#27
#30

print("_"*70)
#4)If-else program to assign grades as per total marks

#Condition for grades:
#Marks less than 40: Fail
#Marks between 40-50: Grade C
#Marks between 51-60: Grade B
#Marks between 61-70: Grade A
#Marks between 71-80: Grade A+
#Marks between 81-90: Grade A++
#Marks between 91-100: Excellent

marks =int(input("enter the marks :"))
if(marks < 40):
    print("fail")
elif(marks>=40 and marks<=50):
    print("Grade C")
elif(marks>50 and marks<=60):
    print("Grade B")
elif(marks>60 and marks<=70):
    print("Grade A")
elif (marks>70 and marks<=80):
    print("Grade A+")
elif(marks>80 and marks<=90):
    print("Grade A++")
elif(marks>90 and marks<=100):
    print("Grade Excellent")
else:
    print("invalid marks entered")

#5)Python program to check number is divided by 3 and 5

num=int(input("enter a number :"))
if (num%3==0 and num%5==0):
    print("The number is divisible by 3 and 5 ")
else:
    print("The number is not divisible by 3 and 5")

#enter a number :30
#The number is divisible by 3 and 5

#enter a number :5
#The number is not divisible by 3 and 5

print("-"*80)

#6)print given number is prime or not
#prime number is dividible by 1 and itself


num =  int(input("Enter a number: "))
# Create count variable
count = 0
# Iterate over numbers
for i in range(2,num):
# Check for division
    if num%i == 0:
    # Add 1 to the count variable
        count += 1
# Check for prime number
if count > 0:
# Print output
    print("It is not a prime number")
else:
#Print output
    print("It is a prime number")

#7) Python program to print the square of the number if the num is divisible by 11

num = int(input("enter a value:"))
if(num%11==0):
    print(num**2)
else:
    print("not divisible by 11")

#8)Python program to check given number is odd or even

n1= int(input("enter a value:"))
if(n1%2==0):
    print("given value is even")
else:
    print("given value is odd")

#9)Python program to check a given number is part of the Fibonacci series from 1 to 10.

# Fibonacci series- a type series where each number is the sum of the two that precede it. It starts from 0 and 1 usually. The Fibonacci sequence is given by 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(type(fib))
# Take input through the user
num = int(input("Enter a number: "))
# Check for number in fibonacci series
if num in fib:
# Print output
    print("It is a part of the series")
else:
# Print output
    print("It is not a part of the series")

"""
def fib(n):
    a=0
    b=1
    print(a)
    print(b)

    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
fib(10)