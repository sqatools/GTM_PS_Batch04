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

#### to print the number also we can do the below method.
num = int(input("Enter a number : "))

if num%3==0 and num%5==0:
    print(f"{num} is  divisible by 3 and 5")
else:
    print(f"{num} is not divisible by 3 and 5")

#Enter a number : 31
#31 is not divisible by 3 and 5

print("-"*80)


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

#### to print number also we can use f"{num} is odd"

num2 = int(input("Enter a value : "))
if num2%2==0:
    print (f"{num2} is even number")
else:
    print (f"{num2} is an odd number")




#10)authentication of username and password. The name and password of the user should be the same to be valid

name = input("Enter User Name : ")
password = input("Enter valid password : ")
if(name==password):
    print("valid details")
else:
    print("Invalid details entered,Please enter valid details")


#11)validate user_id in the list of user_ids. Take a user id to validate user_id.

user_ids = [2,4,6,8,6,9]
user_id = int(input("Enter user id : "))
if user_id in user_ids:
    print("valid userid entered")
else:
    print("invalid userid entered")


#12)square or cube if the given number is divided by 2 or 3 respectively.

num = int(input("Enter a number : "))
if (num%2==0):
    print(num**2 :square)
elif(num%3==0):
    print(num**3 : cube)
else:
    print("not divisible by 2 or 3")



#14)Python nested If else program to describe the interview process

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



#16)find the largest number among three numbers

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


"""

#Python program to check any person eligible to vote or not
#age > 18+ : eligible
#age < 18: not eligible

age = int(input("Enter the age :"))
if age>18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")