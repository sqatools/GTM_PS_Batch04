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

#10). Python program to determine whether a given number is available in the list of numbers or not.
list =[1,2,34,5,6]
a= int(input("enter the value"))
if a in list:
    print("available")
else:
    print("not available")