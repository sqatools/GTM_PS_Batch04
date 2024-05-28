# Python program to check given number is divided by 3 or not.
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
#3). If else program to assign grades as per total marks
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
a =int(input("enter the number"))
if a%3 ==0 and a%5==0:
    print("it is divisble")
else:
    print("it is not divisible")
'''

'''
a = float(input("enter the number"))
if a % 11 == 0:
    print(a**2)
else:
    print("not divisble")
'''

"""
a = int(input("enter the number"))
if a % 2 == 0:
    print("even number")
else:
    print("odd number")
"""

#2). If else program to get all the numbers divided by 3 from 1 to 30.
for i in range(1,31):
    if i % 3 == 0:
        print(i)


#6).  Python program to check given number is a prime number or not.
