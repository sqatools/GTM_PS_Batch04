#1 Python program to check given number is divided by 3 or not.
'''a = 31
if a%3 ==0  :
    print("a is divisble by 3")
else:
    print("a is not divisible by 3")
'''

'''
a = int(input("enter the number:"))
if a%3 == 0:
    print("a is divisble by 3")
else:
    print("a is not divisble by 3")
'''
'''
#2). If else program to assign grades as per total marks
marks = int(input("enter the number"))
if marks < 40:
    print("Fail")
elif marks>=40 and marks <=50:
    print("Grade c")
elif marks>=50 and marks <=60:
    print("Grade B")
elif marks>=60 and marks <=70:
    print("Grade A")
elif marks>=70 and marks <=80:
    print("Grade A+")
elif marks>=80 and marks <=90:
    print("Grade A++")
elif marks>=90 and marks <=100:
    print("Grade Excellent")
else:
    print("Invalid Marks")
'''
'''
#3)
a =int(input("enter the number"))
if a%3 ==0 and a%5==0:
    print("it is divisble")
else:
    print("it is not divisible")
'''

'''
#4)
a = float(input("enter the number"))
if a % 11 == 0:
    print(a**2)
else:
    print("not divisble")
'''

"""
#5)
a = int(input("enter the number"))
if a % 2 == 0:
    print("even number")
else:
    print("odd number")
"""

#6). If else program to get all the numbers divided by 3 from 1 to 30.
'''
for i in range(1,31):
    if i % 3 == 0:
        print(i,end ="-")
'''


#7). Python program to validate user_id in the list of user_ids.
'''
user_id = [1,2,3,4,5,6]
user = int(input("enter the input value :"))
if user in user_id:
    print("yes")
else:
    print("No")
'''

#8). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
'''
a= int(input("enter the value"))
if a % 2==0:
    print("square of number:" ,a**2)
elif a % 3 == 0:
    print("cube of number:", a**3)
'''

#9).  Python program to describe the interview process.
'''
round1 = input("enter the value")
round2=  input("enter the value ")
if round1=="pass":
    print("round1 is clear")
    if round2=="pass":
        print("second round is clear")
    else:
        print("not selected")
else:
    print("try next time")
'''
'''
#10). Python program to determine whether a given number is available in the list of numbers or not.
list =[1,2,34,5,6]
a= int(input("enter the value"))
if a in list:
    print("available")
else:
    print("not available")
 '''
'''
#6).  Python program to check given number is a prime number or not.
n= int(input("enter the value"))
count=0
for i in range(1,n):
    if n%i==0:
        count+=1
if count>0:
    print("not a prime number")
else:
    print('its a prime number ')
'''
'''
# Take input through the user
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
'''

#8)Python program to check a given number is part of the Fibonacci series from 1 to 10.
'''
n = [0,1,1,2,3,5,8]
a= int(input("enter the value"))
if a in n:
    print("it is a part of series ")
else:
    print("its not a part of series")
'''
'''
#Program to check the authentication of username and password
name= input("enter the name ")
password=input("enter the password")
if name==password:
    print("valid")
else:
    print("invalid")
    
'''
'''
#13). Python program to determine whether a
#given number is available in the list of numbers or not.

n=[1,2,3,4,5,6]
a= int(input("enter the value"))
if a in n:
    print("available")
else:
    print("not available")
'''
'''
#14)Python program to find the largest number among three numbers.

n1= int(input("enter the 1st number"))
n2= int(input("enter the 2nd number"))
n3= int(input("enter the 3rd number"))

if n1>n2:
    if n1>n3:
        print("n1 is largest")
    else:
        print("n3 is largest")
else:
    if n2>n3:
        print("n2 is largest")
    else:
        print("n3 is largest")
'''
'''
#15)Python program to check any person eligible to vote or not
age= int(input("enter the value"))
if age>=18:
    print("eligible")

else:
    print("not eligible")
'''
'''
#Python program to check whether a number is palindrome.
doubt
n= 121
a= str(n)
if n== int(a[::-1]):
    print("palindrome")
else:
    print("not palindrome")
'''
'''
#Check whether the string is palindrome or not.
n= "jaj"
a= str(n)
if n== (a[::-1]):
    print("palindrome")
else:
    print("not palindrome")
'''
"""
#19)Python program to check whether the given number is positive or not.
n= int(input("enter the value"))
if n>0:
    print("positive")
else:
    print("not positive")
"""

'''
#20)Python program to check whether the given number is negative or not.
n= int(input("enter the value"))
if n<0:
    print("negative")
else:
    print("not negative")
'''

#21). Python program to check
#whether the given number is positive or negative and even or odd.
'''
n= int(input("enter the value"))
if n>0:
    if n%2==0:
        print("positive and even")
    else:
        print("positive and odd")
else:
    if n%2==0:
        print("even and negative")
    else:
        print("odd and negative")
 '''
#24)Python program to check whether the given character is lowercase or not.
'''
a= input("enter the character")
if a.islower():
    print("True")
else:
    print("False")
    
'''
'''
a= input("enter the character")
if a.isupper():
    print("True")
else:
    print("False")
'''
'''
#25)Python program to check whether the given number is an integer or not.
a= 54
if type(a)==int:
    print("it is an integer")
else:
    print("not an integer")
'''
'''
#26)Python program to check whether the given number is float or not.
a= 32
if type(a)== float:
    print("it is a float")
else:
    print("it is not a float")
'''
'''
#27)Python program to check whether the given input is a string or not.
a= 11111
if type(a)== str:
    print("its a string")
else:
    print("not a string")
'''
'''
#28)Python program to print all the numbers from 10-15 except 13
for i in range(10,16):
    if i!=13:
        print(i)
'''
'''
29). Python program to find the electricity bill. 
According to the following conditions:
Up to 50 units rs 0.50/unit
Up to 100 units rs 0.75/unit
Up to 250 units rs 1.25/unit
above 250 rs 1.50/unit
an additional surcharge of 17% is added to the bill
'''
'''
#31).  Python Python program to check whether the input number
#if a multiple of two print “Fizz” instead of the number
#and for the multiples of three print “Buzz”.
#For numbers that are multiples of both two and three print “FizzBuzz”.
num = int(input("Enter a number: "))

if num%2 == 0 and num%3 == 0:
    print("FizzBuzz")
elif num%2 == 0:
    print("Fizz")
elif num%3 == 0:
    print("Buzz")
    
 '''
'''
#32)Python program to check whether an alphabet is a vowel.
n= input("enter the character")
char= ['a','e','i','o','u','A','E','I','O','U']
if n in char:
    print("vowel")
else:
    print("consonant")
'''

#33)Python program to check whether an alphabet is a consonant.
char = input("Enter a character: ")
vowel = ["A","E","I","O","U","a","e","i","o","u"]

if char not in vowel:
    print("consonant")
else:
    print("vowel")