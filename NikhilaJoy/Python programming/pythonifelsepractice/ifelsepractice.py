"""
#1).  Python program to check given number is divided by 3 or not.

n=input("enter the value")
if int(n) % 3 == 0:
    print(n,"is divisible by 3")
else:
    print("not divisible by 3")

"""
#2). If else program to get all the numbers divided by 3 from 1 to 30.
"""
print("_"*50)

for i in range(1,31):
    if i % 3 ==0:
        print(i)
"""
#3.If else program to assign grades as per total marks.
"""
marks=int(input("enter the mark"))

if marks < 40:
    print("Fail")
elif 40 < marks <= 50:
    print("grade c" )
elif 50 < marks <= 60:
    print("grade B")
elif 60 < marks <= 70:
    print("grade A")
elif 70 < marks <= 80:
    print("grade A+")
elif 80 < marks <= 90:
    print("grade A++")
elif 90 < marks <= 100:
    print("Excellent")
else:
    print("Invalid Mark")
"""
#4).  Python program to check the given number divided by 3 and 5.
"""
n=int(input("enter the number"))
if n % 3 ==0 and n % 5 ==0:
    print ("number divided by 3 and 5")
else:
    print("number is not divided by 3 and 5")
"""
#5). Python program to print the square of the number if it is divided by 11.
"""
n= int(input("enter the number"))
if n % 11 == 0:
    print(n**2)
else:
    print("not divided by 11")
"""
#6).  Python program to check given number is a prime number or not.

#9). Python program to check authentication with the given username and password.

username=input("enter your username")
password=input("enter your password")