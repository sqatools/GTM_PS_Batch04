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
"""
n=int(input("enter the number"))
count=0
for i in range(2,n):
  if n % i == 0 :
    count += 1
if count>0:
    print("it is not a prime number")
else:
    print("it is a prime number")
"""
#9). Python program to check authentication with the given username and password.
"""
username=input("enter your username")
password=input("enter your password")

"""
"""
29). Python program to find the electricity bill. According to the following conditions:
Up to 50 units rs 0.50/unit
Up to 100 units rs 0.75/unit
Up to 250 units rs 1.25/unit
above 250 rs 1.50/unit
an additional surcharge of 17% is added to the bill
Input = 350
Output = 438.75
"""
"""
n=int(input("enter the bill amount"))
bill=0
if 0<n<=50:
    bill=n*.5
elif 50<n<=100:
    bill=n*.5 + (n-50)*.75
elif 100<n<=250:
    bill=50*.5 + 50*.75 + (n-100)*1.25
else:
    bill=50*.5 + 50*.75 + 150*1.25 + (n-250)*1.5
print(bill+bill*.17)
"""
total_unit = int(input("Total units Consumed="))
bill_amount = 0

# If each unit we will add to rate amount in total bill amount
for bill_unit in range(1, total_unit+1):
    if bill_unit <= 50:
        bill_amount = bill_amount + 0.50
    elif bill_unit > 50 and bill_amount <= 100:
        bill_amount = bill_amount + 0.75
    elif bill_unit > 100 and bill_amount <= 250:
        bill_amount = bill_amount + 1.25
    elif bill_unit > 250:
        bill_amount = bill_amount + 1.5

# Addition 17% surcharge on total bill amount
bill_amount_sur = bill_amount + bill_amount * (17/100)
print("Bill amount with surcharge :", bill_amount_sur)