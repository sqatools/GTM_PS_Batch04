n = 50

result ='even' if n%2==0 else 'odd'

print(result)


n1= 66

n2 = [59,60,61,62,63]

result1 = "True" if n1 in n2 else "false"

print(result1)

#  Python program to check given number is divided by 3 or not.

a=34

if a%3==0:
    print("divisible by 3")
else:
    print("not divisible by 3")

#  If else program to get all the numbers divided by 3 from 1 to 30.
c=1
for c in range(1,31):
    if c%3==0:
        print(c,end=" ")


print("$"*10)
# If else program to assign grades as per total marks.
'''
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks
'''

marks = 30

if marks>100:
    print("invalid marks")
elif 30 < marks <= 40:
    print("pass with grade c")
elif 40 < marks <= 50:
    print("pass with grade b")
elif 50<marks<=60:
    print("pass with grade a")
elif 60<marks<=70:
    print("pass with grade a+")
elif 70<marks<=80:
    print("pass with grade a++")
elif 80<marks<=90:
    print("pass with grade a+++")
elif 90<marks<=100:
    print("pass with grade excellent")
else:
    print("student failed")

# Python program to check the given number divided by 3 and 5.

n3 = 45

if n3%3==0 and n3%5==0:
    print("divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")

#  Python program to print the square of the number if it is divided by 11.
'''
num = input("Enter the number")

if int(num)%11==0:
    print('divisible by 11: ',(int(num))**2)
else:
    print("not divisible")
'''
# Python program to check given number is a prime number or not.
'''
num2=int(input("enter the number"))
count=0

for i in range(2,num2):
    if num2%i==0:
        count+=1



if count>0:
    print("not a prime")
else:

    print("prime")
'''
# Python program to check given number is odd or even.
'''
s=int(input("Enter the number: "))

if s%2==0:
    print("even")
else:
    print("Odd")
'''

# Python program to check a given number is part of the Fibonacci series from 1 to 10.
'''
def fabi():

    num1 = int(input("Enter the number: "))

    num2 = int(input("number2: "))

    count =1

    print("The Sequence is :",end=" ")
    while count<10:
        print(num1,end=" ")
        num3=num1+num2
        num1=num2
        num2=num3
        count+=1
fabi()
new=[0,1,1,2,3,5,8,13,21,34,]
h=22
if h in new:
    print("It is part series")
else:
    print("not a part series")
'''

# Python program to check authentication with the given username and password.
'''
username=input("Enter username: ")
password=input("Enter password: ")

if username==password:
    print("valid")
else:
    print("invalid")

'''
# Python program to validate user_id in the list of user_ids.
'''
id_lst=[1,2,3,4,5,6,7,8,9]
id_l=int(input("Enter the ID: "))

if id_l in id_lst:
    print("Yes is there")
else:
    print("No not there")
'''

# Print a square or cube of the given number
'''
num = int(input("number: "))
if num%2==0:
    print("square: ",num**2)
elif num%3==0:
    print("cube",num**3)
else:
    print("other than: ",num**2)

# Python program to describe the interview process.
r1=input("Enter the  data1: ")
r2=input("Enter the data2: ")

if r1=="passed":
    print("congrats your 1st round is clear")
    if r2=="passed":
        print("congrats your 2nd round is clear,you are plced")
    else:
        print("failed in 2rd round ,please try next time ")
else:
    print("failed in 1st round ,please try next time ")

'''
# Python program to determine whether a given number is available in the list of numbers or not.
'''
lst=[56,2,15,1,41,6,23,2,5,26,2,42,9]

m=int(input("enter the data"))

if m in lst:
    print(f" {m} is present")
else:
    print(f" {m} is not present")

# Python program to find the largest number among three numbers.

num1 =int(input("number1: "))
num2=int(input("number2: "))
num3=int(input("number3: "))

if num1>num2:
    if num1>num3:
        print(f"{num1} is greater")
    else:
        print(f"{num3} is greater")

else:
    if num2>num3:
        print(f'{num2} is greater')
    else:
        print(f'{num3} is greater')

# Python program to check any person eligible to vote or not
# age > 18+ : eligible
# age < 18: not eligible

user=int(input("Enter the information: "))

if user>18:
    print("User is eligible to vote")
else:
    print("user not eligible for vote")
'''
# Python program to check whether any given number is a palindrome.
# Input: 121
# Output: palindrome
'''
num = int(input("Enter the number: "))
rev = 0

while num>0:
    rem =n%10
    rev =rev*10+rem
    num=num//10

if num==rev:
    print(f"{num} is palinadrome")
else:
    print(f"{num} is not palinadrome")

m =121
h = str(m)
if m==int(h[::-1]):
    print(f"{h} is palinadrome2")
else:
    print(f"{h} not palinadrome2")
'''
# Python program to check if any given string is palindrome or not.
# Input: ‘jaj’
# output = palindrome

str = "jaj"
if str==str[::-1]:
    print(f"{str} is palinodrome")
else:
    print(f"{str} is Not palinodrome")

# Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.

marks1 = 34


if marks1>35:
    print(f" student is passed with {marks1} in the exam ")
else:
    print(f" student failed with {marks1} in the exam")

# Python program to check whether the given number is positive or not.

d =9

if d>0:
    print("True")
else:
    print("False")

#  Python program to check whether the given number is negative or not.

e=-45
if e<0:
    print("True")
else:
    print("False")

# Python program to check whether the given number is positive or negative and even or odd.

num = int(input("Enter the Number: "))

if num>0:
    if num%2==0:
        print("The given number is positive and even")
    else:
        print("the given number is positive and odd")
else:
    if num%2==0:
        print("The given number is negitive and even")
    else:
        print("the given number is negitive and odd")

# Python program to print the largest number from two numbers.

x = 69
x1 =61

if x>x1:
    print(f'{x}is largest')
else:
    print(f'{x1} is largest')

# Python program to check whether a given character is uppercase or not.

st = "A"
if st.isupper():
    print("is true")
else:
    print("is false")