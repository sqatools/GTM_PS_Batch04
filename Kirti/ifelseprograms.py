# ************************************ 1
print("if else programs and for loop programs")

a = 30
if a%3 == 0:
    print("Number is divisible by 3")
else :
    print("Number is not divisible by 3")

# ************************************ 2

print("_"*30)

print("Program to get all numbers divided by 3 between 1 to 30")


for i in range(1,30):
    if 1%3 == 0:
        print(i)

# ************************************ 3

print("_ marks "*30)

marks = 41

if marks< 40 :
    print("FAIL")
elif 40 <= marks <= 50:
    print("Grade C")
elif 50 <= marks <= 60:
    print("Grade B")
elif 60 <= marks >= 70:
    print("Grade A")
elif 70 <= marks >= 80:
    print("Grade A+")
elif 80 <= marks >= 90:
    print("Grade A++")
elif 90 <= marks >= 100:
    print("Excelent")
else :
    print("INVALID")
# ************************************ 4 Python program to check the given number divided by 3 and 5.



print("_"*50)

print("Python program to print the square of the number if it is divided by 11")

a = 22

if a%11 == 0:
    print("Square of number divided by 11 is :", a**2)
# ************************************ 5

print("_"*50)
print(" Python program to check given number is a Even or odd")

a = 3

if a%2 ==0:
    print("Given number is even")
else :
    print("Given Number is odd",a)
# ************************************ 6

print("_"*50)
print("program to check the given number is divisible by 3 and 7")

a = 22

if a%3 == 0 and a%7 ==0 :
    print("Number is divisible by 3 and 7 both",a)
else :
    print("Number is not divisible by 3 and 7 both")

# ************************************ 7
print("_"*50)
print("interview process")

r1 = "pass"
r2 = "Fail"

if r1 == "pass" :
    print("Eligible for round 2")
    if r2 == "pass":
        print("Congrats placed")
    else:
        print("Better luck next time")

else :
    print("Not eligible for round 2")


# if r2 == "pass" :
#     print("Congrats placed")
# else :
#     print("Better luck next time")

# ************************************ 8
print("_"*50)

#palamdrome program

pal = ['M','A','D','A','M']

A1 = (pal[-1],pal[-2],pal[-3],pal[-4],pal[-5])
B1 = (pal[0],pal[1],pal[2],pal[3],pal[4])

if A1 == B1 :
    print("The given string is palamdrome :",pal[-1],pal[-2],pal[-3],pal[-4],pal[-5])
else :
    print("The given string is not a palandrome :",pal[0],pal[1],pal[2],pal[3],pal[4])

## Question fot this program what is str2 = str1[::-1] ? -1 : : -1

print("_"*50)
# check if number is postive or negative
#num = int(input("Enter a Number :"))

#if num >0 :
#    print("True the given number is positive :", num)
#else :
#    print("False the given number is negative :", num)

#print("_"*50)

# checking how to tak user input

import cffi

# v1 = (input("Enter any letter :"))
#
# num = int(input("Enter a Number :"))  ## When i was tring user input it was not working properly
# need keyboard shortcut for commenting the code


#if (num >0 and num%2==0) : will this not work ?

#WAP the given number is positive or negative and even or odd.

'''
a1 = int(input("Enter the number :"))

if a1 > 0 :
    if a1%2 == 0 :
        print("The numebr is postive and even")
    else :
        print("The Number is positve and Odd")
else :
    if a1%2 != 0 :
        print("The number is negative and odd")
    else :
        print("Number is negative and even")
'''

print("_"* 50)
# WAP to print the largest number from two numbers.

a1 = 20
b1 = 30

if a1>b1 :
    print("The gratest number is :",a1)
else :
    print("The gratest numner is :", b1)

print("_"*50)
# WAP to print the largest number from two numbers. through input from user
'''
a1 = int(input("Enter the first number :"))

print(a1)

b1 = int(input("Enter the second number :"))

print(b1)

if a1>b1 :
    print("The first number is greater :", a1)
else :
    print("The second number is grater :",b1)
'''

print("_"*50)
#WAP to check whether the input is a string

X1 = "KIRTI"

if type(input) == type("str"): # need to reexecute this
    print("The input value is String :",X1)
else : # when i did not write the else statemt then program was not working
    print("Input value is not a string", X1)

print("_"*50)
#WAP  to print all the numbers from 10-15 except 13

'''K = 10,11,12,13,14,15

for k in range(1,6,1) : # how does this works
    print(K)
'''
for i in range(10,16,1):
    if i!=13 :
        print(i)

print("_"*50)

''' Python program to find the electricity bill. According to the following conditions:
Up to 50 units rs 0.50/unit
Up to 100 units rs 0.75/unit
Up to 250 units rs 1.25/unit
above 250 rs 1.50/unit
an additional surcharge of 17% is added to the bill

logic if unit  is between 0 to 50 
'''
'''
unit = 350

#for unit in range(0,251,1): can we do it with range ?
if unit <=50 :
        total_amount = ((unit*50)*17/100) 
        print("The bill amount is",total_amount)
elif unit <=100 :
        total_amount = ((unit*0.75)*17/100)
        print("The bill amount is",total_amount)
elif unit <=250 :
        total_amount = ((unit*1.25)*17/100)
        print("The bill amount is",total_amount)
elif unit >250 :
        total_amount = ((unit*1.50) * 17 / 100)
        print("The bill amout is ",total_amount) '''

print("_"*50)
#Python Python program to check whether the input number if a multiple of two print “Fizz” instead of the number and for the multiples of three print “Buzz”. For numbers that are multiples of both two and three print “FizzBuzz”.

'''num = int(input("Enter the number :")) # error in solution out put


if num%2 == 0:
    print("Fizz")
elif num%3 == 0:
    print("Buzz")
elif num%2 == 0 and num%3 == 0:
    print("FizzBuzz") '''

print("_"*50)

a = 8
if a%3 == 0 and a%5 == 0:
    print("The Number is divided by 5 and  3")
else :
    print("The Numebr is not divided by 5 and 3")

# Python program to print the square of the number if it is divided by 11.
print("_"*50)
q = 22

if q%11 == 0:
    print("Number divided by 11 and its square is :", q**2)
else :
    print("Number is not divided by 11")


print("_"*50)

#Check a number is part of the Fibonacci series

fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print("Fibonacy seris is : ",fibo)

num2 = int(input("Enter the Number"))

if num2 in fibo :
    print("The number is part of the Fibonacci series")
else :
    print(" Number is part of the Fibonacci series")

print("_"*50)

# Python program to accept two numbers and mathematical operations from users and perform mathematical operations according to it.

n1 = int(input("Enter the fist number :"))

n2 = int(input("Ente the second number :"))

Operation = input("Enter the operation to be performed :")  # how direct input works?

if Operation == "+" :
    print(n1+n2)
elif Operation == "_" :
    print(n1-n2)
elif Operation == "/" :
    print(n1/n2)
elif Operation == "*" :
    print(n1*n2)
else :
    print("Invalid input")

print("_"*50)
