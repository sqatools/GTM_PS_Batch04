#Program to check if a number is divisible by 3 - directly assigning value
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

#Program to check if a number is divisible by 3 - user assigning value
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

#Program to get all numbers divided by 3 between 1 to 30

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
#If-else program to assign grades as per total marks

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

##---------------simply chained comparison
##############marks > 35 and <=45 by simply chained comparison 35 < marks <=45 #############


marks = int(input("Enter the marks : "))
if marks < 35:
    print("failed")
elif 35 < marks <= 55:
    print("Grade C")
elif 55 < marks <=65:
    print("grade B")
elif 65 < marks <=85:
    print("grade A")
elif 85 < marks <= 95:
    print("grade A+")
elif 95 < marks <=100:
    print("Excellent")
else:
    print("not a valid mark")


#Python program to check number is divided by 3 and 5

num=int(input("enter a number :"))
if (num%3==0 and num%5==0):
    print("The number is divisible by 3 and 5 ")
else:
    print("The number is not divisible by 3 and 5")

#enter a number :30
#The number is divisible by 3 and 5

#enter a number :5
#The number is not divisible by 3 and 5

#### to print the number also we can do the below method.
num = int(input("Enter a number : "))

if num%3==0 and num%5==0:
    print(f"{num} is  divisible by 3 and 5")
else:
    print(f"{num} is not divisible by 3 and 5")

#Enter a number : 31
#31 is not divisible by 3 and 5

print("-"*80)


# Python program to print the square of the number if the num is divisible by 11

num = int(input("enter a value:"))
if(num%11==0):
    print(num**2)
else:
    print("not divisible by 11")

#Python program to check given number is odd or even

n1= int(input("enter a value:"))
if(n1%2==0):
    print("given value is even")
else:
    print("given value is odd")

#### to print number also we can use f"{num} is odd"

num2 = int(input("Enter a value : "))
if num2%2==0:
    print (f"{num2} is even number")
else:
    print (f"{num2} is an odd number")




#authentication of username and password. The name and password of the user should be the same to be valid

name = input("Enter User Name : ")
password = input("Enter valid password : ")
if(name==password):
    print("valid details")
else:
    print("Invalid details entered,Please enter valid details")


#validate user_id in the list of user_ids. Take a user id to validate user_id.

user_ids = [2,4,6,8,6,9]
user_id = int(input("Enter user id : "))
if user_id in user_ids:
    print("valid userid entered")
else:
    print("invalid userid entered")


#square or cube if the given number is divided by 2 or 3 respectively.

num = int(input("Enter a number : "))
if (num%2==0):
    print(num**2 :square)
elif(num%3==0):
    print(num**3 : cube)
else:
    print("not divisible by 2 or 3")



#Python nested If else program to describe the interview process

round1 = input("Enter the selection status for first round : ")
round2 = input("Enter the selection status for second round : ")

if round1 == "pass":
    print("congrats you are selected in first round interview")
    if round2 == "pass":
        print("congrats you are selected and will get the offer letter soon through mail")
    else:
        print("sorry,you have not cleared round 2")
else:
    print("Better luck next time")


#15)Determine whether a number is available in the list

list1 = [22,33,49,34,65,67,12,25]
num = int(input("Enter a number: "))

if num in list1:
    print("num is available in the list")  #this will print on;y the message
else:
    print("num is not available in the list") #num is not available in the list

########

list1 = [22,33,49,34,65,67,12,25]
num = int(input("Enter a number: "))

if num in list1:
    print(f"{num} is available in the list")  #this will print the number also along with the message to print
else:
    print(f"{num} is not available in the list")  #30 is not available in the list



#find the largest number among three numbers

num1 =int(input("Enter first number : "))
num2 =int(input("Enter second number : "))
num3 = int(input("Enter Third number : "))

if num1>num2:
    if num1>num3:
        print(f"{num1} is greater")
    else:
        print(f"{num3} is greater")
else:
    if num2>num3:
        print(f"{num2} is greater")
    else:
        print(f"{num3} is greater")


#Python program to check any person eligible to vote or not
#age > 18+ : eligible
#age < 18: not eligible

age = int(input("Enter the age :"))
if age>=18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")



#Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
#Input = Enter marks: 45
#Output = Pass

marks = int(input("Enter the marks :"))

if marks> 35:
    print("passed the exam")
else:
    print("Filed the exam")


# Python program to check whether the given number is positive or not.
#Input = 20
#Output = True

num4 = int(input("Enter a value : "))
if num4>0:
    print("true")
else:
    print("false")

#Python program to check whether the given number is negative or not.

num5 = int(input("Enter a value : "))
if num5<0:
    print("true")
else:
    print("false")

#Python program to check whether the given number is positive or negative and even or odd.
#Input = 26
#Output = The given number is positive and even


num6 = int(input("Enter a value :"))
if num6>0:
    if num6%2==0:
        print(f"{num6} is even")
    else:
        print(f"{num6} is odd")
else:
    if num6 % 2 == 0:
        print(f"{num6} is even")
    else:
        print(f"{num6} is odd")


#Python program to print the largest number from two numbers.
#Input:
#25, 63
#Output = 63

a=25
b=63

if a>b:
    print (f"{a} is greater")
else:
    print (f"{b} is greater")


#Check whether the number is an integer or not

num7 = 3

if (type(num7) == int):
    print("Given value is an integer")
else:                                          #Given value is an integer
    print("Given value is not integer")

#
str7 = "A"

if (type(str7) == int):
    print("Given value is an integer")
else:                                            #Given value is not integer
    print("Given value is not integer")



#given number is float or not

num9 = 45.5

if type(num9) == float:
    print("Given number is float")
else:                                            #Given number is float
    print("Given number is not float")


#Python program to check whether the given input is a string or not.
#Input = ‘sqatools’
#Output = True

str1 = "sqatools"

if type(str1) == str:
    print("True")
else:
    print("false")



#leap year

year = int(input("Enter the year: "))

if (year%100 != 0 or year%400 == 0) and year%4 == 0:  #Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years, if they are exactly divisible by 400
    print("The year given is a leap year.")
else:
    print("The year given is not a leap year.")



#Python Python program to check whether the input number if a multiple of two print “Fizz” instead of the number and for the multiples of three print “Buzz”. For numbers that are multiples of both two and three print “FizzBuzz”.

num = int(input("Enter a number: "))

if num%2 == 0 and num%3 == 0:
    print("FizzBuzz")
elif num%2 == 0:
    print("Fizz")
elif num%3 == 0:
    print("Buzz")
else:
    print("Entered number is not divisible by 3 or 2")


#alphabet is a vowel

alphabet = input("Enter a character: ")
vowels = ["A", "E", "I", "O" , "U" , "a", "e" , "i" , "o" , "u"]

if alphabet in vowels:
    print("Given char is a vowel")                         #if in##########
else:
    print("Given char is not a vowel")



#Program to check whether an alphabet is a consonant

alphabet = input("Enter a character: ")
vowels = ["A", "E", "I", "O" , "U" , "a", "e" , "i" , "o" , "u"]

if alphabet not in vowels:                                  ######## if not in #########
    print("Given char is consonant")
else:
    print("Given char is not consonant")




#Python program to convert the month name to the number of days

month = input ("Enter the month : ")

if month=="january":
    print("number of days 31")
elif month=="february":
    print("number of days 28 or 29")
elif month=="march":
    print("number of days 31")
elif month=="april":
    print("number of days 30")
elif month=="may":
    print("number of days 31")
elif month=="june":
    print("number of days 30")
elif month=="july":
    print("number of days 31")
elif month=="august":
    print("number of days 30")
elif month=="september":
    print("number of days 31")
elif month=="october":
    print("number of days 30")
elif month=="november":
    print("number of days 31")
elif month=="december":
    print("number of days 30")
else:
    print("invalid month entered")

# Python program to check whether a triangle is equilateral or not. An equilateral triangle is a triangle in which all three sides are equal.
#Input:
#Enter the length of the sides of the triangle
#A=10
#B=10
#C=10
#Output = True

side1 = int(input("Enter side1 :"))
side2 = int(input("Enter side2 :"))
side3 = int(input("Enter side3 :"))

if side1==side2==side3:
    print("True : Given triangle is an equilateral")
else:
    print("false : given triangle is not an equilateral triangle")


#Python program to check whether a triangle is scalene or not. A scalene triangle is a triangle that has three unequal sides

side1 = int(input("Enter side1 :"))
side2 = int(input("Enter side2 :"))
side3 = int(input("Enter side3 :"))

if side1 != side2 != side3:
    print("True : given triangle is scalene triangle ")
else:
    print("false : given triangle is not scalene triangle")



#program to check whether a triangle is isosceles or not. An isosceles triangle is a triangle with (at least) two equal sides

side1 = int(input("Enter side1 :"))
side2 = int(input("Enter side2 :"))
side3 = int(input("Enter side3 :"))

if side1==side2 or side2==side3 or side3==side1:
    print("True : Given triangle is isosceles triangle")
else:
    print("false : Given triangle is not an isosceles triangle")


#In this python if else program, we will read month and returns season for that month.

#Condition for the season:
#Summer – February, March, April, May
#Rainy – June, July, August, September
#Winter – Octomber, November, December, January



month = input("Enter a month : ")

if month == "February" or month == "March" or month == "April" or month == "May":
    print("Summer")
elif month == "June" or month == "July" or month == "August" or month == "September":
    print("Rainy")
else:
    print("Winter")

"""
