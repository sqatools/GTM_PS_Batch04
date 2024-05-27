'''
if(condition)
   code
else:
   code
'''
'''
a=50
b=40
if a<b:
    print("the statement is true")
else:
    print("the statement is false")

print("*"*50)
number=int(input("Enter the number:"))
if number>0:
  print("The number is positive")
else:
  print("The number is negative")

print("*"*50)
num=int(input("Enter the number:"))
if num%3==30:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")

marks=int(input("enter the marks:"))
if marks<40:
    print("Fail")
elif marks>=40-50:
    print("Grade c")
elif marks>=51-60:
    print("Grade B")
elif marks>=61-70:
    print("Grade A")
elif marks>=71-80:
    print("Grade A+")
elif marks>=81-90:
    print("Grade A++")
elif marks>=91-100:
    print("Excellent")

print('-'*50)
num=int(input("Enter the number:"))
if num%11==0:
    print("Number is divisible by 11")
    print(num**2)
else:
    print("number is not divisible by 11")


num=14
if num%2==0:
    print("number is even")
else:
    print("number is odd")

print('_'*50)

num=int(input("enter the number:"))
count=0
for i in range(2,num):
 if num%i==0:
   count+=1
if count>0:
     print("number is prime")
else:
     print("number is not prime")
    '''

print('_'*50)

Fib=[0,1,1,2,3,4,5,6,7,8,9]
num=int(input("enter the number:"))
if num in Fib:
    print("number is Fibannoci")
else:
    print("Number is not fibbanoci")

# program for authentication of name and  pwd
name=input("enter the username")
password=input("enter the password")
if name==password:
    print("Authentication is right")
else:
    print("Authentication is wrong")








