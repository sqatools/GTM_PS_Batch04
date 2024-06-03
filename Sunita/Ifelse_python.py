#1).  Python program to check given number is divided by 3 or not.

num=15
if num%3==0:
    print(num," is divisible by 3")
else:
    print(num," is not divisible by 3")

#2). If else program to get all the numbers divided by 3 from 1 to 30.
print("*"*50)
for i in range(1,31):
    if i%3==0:
        print(i, " is divisible by 3")

"""
#3). If else program to assign grades as per total marks.
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks

print("*"*50)
marks=int(input("Enter the marks : "))
if marks>100:
    print("Marks should not be greater than 100 ")
elif 40<marks<=50:
    print("Grade C")
elif 50<marks<=60:
    print("Grade B")
elif 60<marks<=70:
    print("Grade A")
elif 70<marks<=80:
    print("Grade A+")
elif 80<marks<=90:
    print("Grade A++")
elif 90<marks<=100:
    print("Grade Excellent")
else:
    print("OOPS! failed")

#4).  Python program to check the given number divided by 3 and 5.
print("*"*50)
num=25
if num%3==0 and num%5==0:
    print(num," is divisible by 3 and 5")
else:
    print(num," is not divisible by 3 and 5")

#5). Python program to print the square of the number if it is divided by 11.
print("*"*50)
num=111
if num%11==0:
    print(num,"is divisible by 11")
    print(num**2,"is the square of",num)
else:
    print(num, "is not divisible by 11")

#6).  Python program to check given number is a prime number or not.
print("*"*50)

num=int(int(input("Enter any integer number : ")))
count=0
for i in (1,num):
    if num%i==0:
        count +=1
if count>0:
       print(i,"is not a prime number")
else:
    print(i,"is prime number")

#7). Python program to check given number is odd or even.

num=int(input("Enter any integer number : "))
if num%2==0:
    print(num, "is an even number")
else:
    print(num, "is odd number")

#8). Python program to check a given number is part of the Fibonacci series from 1 to 10.

fib=0,1,1,2,3,5,8,13,21,34
num=int(input("Enter any integer number : "))
if num in fib:
    print(num,"is part of the Fibonacci series")
else:
    print(num, "is not part of the Fibonacci series")

#9). Python program to check authentication with the given username and password.

username=input("Enter username :")
password=input("Enter Password :")
if username==password:
    print("Successful login")
else:
    print("login failed")
    
"""

#10). Python program to validate user_id in the list of user_ids.

user_ids=[1,2,345,67,8,91,23,4]
user_id=int(input("Enter any integer number : "))
if user_id in user_ids:
    print(user_id,"in the list of user_ids")
else:
    print(user_id, "is not in the list of user_ids")





